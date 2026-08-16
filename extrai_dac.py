#!/usr/bin/env python3
"""Extrai a via diagnostica de DAC do SIA/SIH por estabelecimento.

Stream: baixa 1 arquivo -> filtra -> agrega -> apaga o bruto.
Pico de disco = 1 arquivo, nao 97GB.

IMPORTANTE: enumera o diretorio FTP em vez de construir nomes.
UFs grandes (SP, MG, RJ, RS) tem arquivos PARTICIONADOS (PASP2501a/b/c/d.dbc).
Construir nome sem sufixo perde silenciosamente ~40% da populacao do pais.

Saida: dac_{sia,sih}[_grupo].csv  (sistema, uf, competencia, cnes, procedimento, qtd, valor)
"""
import os, re, sys, csv, subprocess, tempfile
import datasus_dbc, dbfread

FTP = "ftp://ftp.datasus.gov.br/dissemin/publicos"
UFS = "AC AL AM AP BA CE DF ES GO MA MG MS MT PA PB PE PI PR RJ RN RO RR RS SC SE SP TO".split()

# Codigos conferidos contra SIGTAP 202608 (tb_procedimento.txt), nao de memoria.
SIA_CARDIO = {
    "0211020060": "teste_ergometrico",
    "0205010016": "eco_estresse",
    "0208010025": "cintilo_perfusao_estresse",
    "0208010033": "cintilo_perfusao_repouso",
    "0208010076": "cintilo_camaras_esforco",
    "0211020010": "cateterismo_cardiaco",      # NAO 0211020036 (= eletrocardiograma)
    "0211020036": "eletrocardiograma",         # contexto de volume
}
# Grupo 0206 inteiro (tomografia) = proxy de capacidade revelada.
# Nao existe codigo de angioTC de coronarias no SIGTAP; por isso o grupo todo.
SIA_PREFIX = ("0206",)
SIH_PREFIX = ("0406",)                         # cirurgia do aparelho circulatorio
SIH_EXTRA = {"0211020010"}                     # cateterismo faturado em AIH

CFG = {  # sistema -> (pasta, prefixo, col_proc, col_cnes, col_qtd, col_valor)
    "SIA": ("SIASUS", "PA", "PA_PROC_ID", "PA_CODUNI", "PA_QTDAPR", "PA_VALAPR"),
    "SIH": ("SIHSUS", "RD", "PROC_REA",   "CNES",      None,        "VAL_TOT"),
}


def lista_remota(pasta, pref, ano, ufs):
    """Enumera o FTP e devolve os nomes REAIS, incluindo particoes a/b/c/d."""
    out = subprocess.run(["curl", "-sS", "--max-time", "180",
                          f"{FTP}/{pasta}/200801_/Dados/"],
                         capture_output=True, text=True).stdout
    pat = re.compile(rf"{pref}([A-Z]{{2}}){ano % 100:02d}(\d{{2}})[a-z]?\.dbc")
    achados = sorted({m.group(0) for m in pat.finditer(out) if m.group(1) in ufs})
    vistos = {pat.match(f).group(1) for f in achados}
    faltando = set(ufs) - vistos
    if faltando:
        print(f"!! ATENCAO: sem arquivos {ano} para {sorted(faltando)}", file=sys.stderr)
    return achados


def processa(dbc, col_proc, col_cnes, col_qtd, col_valor, alvo):
    dbf = dbc[:-4] + ".dbf"
    agg = {}
    try:
        datasus_dbc.decompress(dbc, dbf)
        for r in dbfread.DBF(dbf, encoding="latin-1", load=False):
            p = str(r.get(col_proc, "")).strip()
            if not alvo(p):
                continue
            k = (str(r.get(col_cnes, "")).strip(), p)
            q, v = agg.get(k, (0.0, 0.0))
            agg[k] = (q + (num(r.get(col_qtd)) if col_qtd else 1),
                      v + num(r.get(col_valor)))
    except Exception as e:
        print(f"!! FALHOU {os.path.basename(dbc)}: {e}", file=sys.stderr)
        return None                                    # None != {} : erro, nao "vazio"
    finally:
        for f in (dbc, dbf):
            if os.path.exists(f):
                os.remove(f)
    return agg


def num(v):
    try:
        return float(str(v).strip() or 0)
    except ValueError:
        return 0.0


def roda(sistema, ano, out, ufs=None):
    pasta, pref, c_proc, c_cnes, c_qtd, c_val = CFG[sistema]
    ufs = ufs or UFS
    alvo = ((lambda p: p in SIA_CARDIO or p.startswith(SIA_PREFIX)) if sistema == "SIA"
            else (lambda p: p in SIH_EXTRA or p.startswith(SIH_PREFIX)))
    arquivos = lista_remota(pasta, pref, ano, ufs)
    print(f"{sistema} {ano}: {len(arquivos)} arquivos a processar", flush=True)

    falhas = []
    with open(out, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["sistema", "uf", "competencia", "cnes", "procedimento", "qtd", "valor"])
        for i, nome in enumerate(arquivos, 1):
            uf, mes = nome[2:4], nome[6:8]
            tmp = os.path.join(tempfile.gettempdir(), nome)
            r = subprocess.run(["curl", "-sS", "--max-time", "1800", "-o", tmp,
                                f"{FTP}/{pasta}/200801_/Dados/{nome}"],
                               capture_output=True, text=True)
            if r.returncode != 0 or not os.path.exists(tmp) or os.path.getsize(tmp) == 0:
                print(f"!! DOWNLOAD FALHOU {nome}", file=sys.stderr)
                falhas.append(nome)
                continue
            agg = processa(tmp, c_proc, c_cnes, c_qtd, c_val, alvo)
            if agg is None:
                falhas.append(nome)
                continue
            for (cnes, p), (q, v) in agg.items():
                w.writerow([sistema, uf, f"{ano}{mes}", cnes, p, q, round(v, 2)])
            fh.flush()
            print(f"[{i}/{len(arquivos)}] {nome}: {len(agg)} pares", flush=True)

    if falhas:
        print(f"\n!! {len(falhas)} ARQUIVOS PERDIDOS: {falhas}", file=sys.stderr)
    else:
        print(f"\nOK: {len(arquivos)} arquivos, nenhuma perda.")


if __name__ == "__main__":
    sistema, ano = sys.argv[1], int(sys.argv[2])
    ufs = sys.argv[3].split(",") if len(sys.argv) > 3 else None
    sufixo = f"_{sys.argv[4]}" if len(sys.argv) > 4 else ""
    os.makedirs("data", exist_ok=True)
    roda(sistema, ano, f"data/dac_{sistema.lower()}{sufixo}.csv", ufs)
