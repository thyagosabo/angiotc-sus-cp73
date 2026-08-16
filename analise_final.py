#!/usr/bin/env python3
"""Fecha a analise nacional: demanda (SIA+SIH) x banda de capacidade (CNES).

Roda com dados parciais ou completos — sempre declara a cobertura no cabecalho.
Saidas: 4 CSVs + resumo no stdout para a secao 4 da contribuicao a CP 73/2026.
"""
import glob, os, sys, json, urllib.request
import datasus_dbc, dbfread, pandas as pd

ANO = 2025
COMPET_CNES = "202606"

COMPARADORES = {
    "0211020060": "Teste ergometrico",
    "0205010016": "Ecocardiografia de estresse",
    "0208010025": "Cintilografia perfusao - estresse",
    "0208010033": "Cintilografia perfusao - repouso",
    "0208010076": "Cintilografia camaras - esforco",
    "0211020010": "Cateterismo cardiaco",
}
UFS = "AC AL AM AP BA CE DF ES GO MA MG MS MT PA PB PE PI PR RJ RN RO RR RS SC SE SP TO".split()


def carrega_sia():
    fs = glob.glob("data/dac_sia*.csv")
    if not fs:
        sys.exit("sem data/dac_sia*.csv — rode extrai_dac.py primeiro")
    d = pd.concat([pd.read_csv(f, dtype={"procedimento": str, "cnes": str}) for f in fs],
                  ignore_index=True)
    return d


def capacidade_cnes():
    """Banda: teto = TC disponivel ao SUS; piso = TC + hemodinamica no mesmo CNES."""
    rows = []
    for f in sorted(glob.glob("cnes/EQ*.dbc")):
        uf, dbf = os.path.basename(f)[2:4], f[:-4] + ".dbf"
        if not os.path.exists(dbf):
            datasus_dbc.decompress(f, dbf)
        d = pd.DataFrame(iter(dbfread.DBF(dbf, encoding="latin-1")))
        d["UF"] = uf
        rows.append(d)
    eq = pd.concat(rows, ignore_index=True)
    eq["QT_USO"] = pd.to_numeric(eq.QT_USO, errors="coerce").fillna(0)
    sus = eq[(eq.IND_SUS == "1") & (eq.QT_USO > 0)]
    tc = sus[(sus.TIPEQUIP == "01") & (sus.CODEQUIP == "11")]
    hemo = set(sus[(sus.TIPEQUIP == "01") & (sus.CODEQUIP == "10")].CNES)
    cap = tc.groupby("UF").agg(teto_estab=("CNES", "nunique"), teto_equip=("QT_USO", "sum"))
    cap["piso_estab"] = tc[tc.CNES.isin(hemo)].groupby("UF").CNES.nunique()
    cap = cap.fillna(0).astype(int)
    cap["pct_piso"] = (100 * cap.piso_estab / cap.teto_estab).round(1)
    return cap


def populacao():
    u = ("https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/-1"
         "/variaveis/9324?localidades=N3[all]")
    S = {'Acre':'AC','Alagoas':'AL','Amazonas':'AM','Amapá':'AP','Bahia':'BA','Ceará':'CE',
         'Distrito Federal':'DF','Espírito Santo':'ES','Goiás':'GO','Maranhão':'MA',
         'Minas Gerais':'MG','Mato Grosso do Sul':'MS','Mato Grosso':'MT','Pará':'PA',
         'Paraíba':'PB','Pernambuco':'PE','Piauí':'PI','Paraná':'PR','Rio de Janeiro':'RJ',
         'Rio Grande do Norte':'RN','Rondônia':'RO','Roraima':'RR','Rio Grande do Sul':'RS',
         'Santa Catarina':'SC','Sergipe':'SE','São Paulo':'SP','Tocantins':'TO'}
    try:
        j = json.load(urllib.request.urlopen(u, timeout=45))
        s = j[0]["resultados"][0]["series"]
        return pd.Series({S[x["localidade"]["nome"]]: int(list(x["serie"].values())[0])
                          for x in s if x["localidade"]["nome"] in S})
    except Exception as e:
        print(f"!! IBGE indisponivel ({e}) — seguindo sem denominador", file=sys.stderr)
        return pd.Series(dtype=int)


def main():
    sia = carrega_sia()
    ufs_ok = sorted(sia.uf.unique())
    meses = sorted(sia.competencia.unique())
    completo = len(ufs_ok) == 27 and len(meses) == 12
    print("=" * 78)
    print(f"COBERTURA SIA: {len(ufs_ok)}/27 UFs, {len(meses)}/12 competencias "
          f"-> {'COMPLETO' if completo else 'PARCIAL — NAO EXTRAPOLAR'}")
    if not completo:
        print(f"  faltando UFs: {sorted(set(UFS) - set(ufs_ok))}")
    print("=" * 78)

    # --- 1. demanda: comparadores realizados no SUS -------------------------
    comp = sia[sia.procedimento.isin(COMPARADORES)].copy()
    comp["nome"] = comp.procedimento.map(COMPARADORES)
    nac = comp.groupby("nome").agg(qtd=("qtd", "sum"), valor=("valor", "sum"),
                                   estab=("cnes", "nunique")).sort_values("qtd", ascending=False)
    nac["r$_medio"] = (nac.valor / nac.qtd).round(2)
    nac.to_csv("output/out-demanda-nacional.csv")
    print("\n### 1. COMPARADORES REALIZADOS NO SUS (SIA " + str(ANO) + ")")
    print(nac.to_string(float_format=lambda x: f"{x:,.2f}"))
    tot_func = nac.loc[[i for i in nac.index if "Cateterismo" not in i], "qtd"].sum()
    print(f"\n  investigacao funcional nao invasiva (total): {tot_func:,.0f}")
    if "Teste ergometrico" in nac.index:
        print(f"  share do teste ergometrico: "
              f"{100*nac.loc['Teste ergometrico','qtd']/tot_func:.1f}%")

    # --- 2. capacidade: banda ----------------------------------------------
    cap = capacidade_cnes()
    pop = populacao()
    if len(pop):
        cap["populacao"] = pop
        cap["teto_por_mi"] = (1e6 * cap.teto_equip / cap.populacao).round(2)
        cap["piso_por_mi"] = (1e6 * cap.piso_estab / cap.populacao).round(2)
    cap.to_csv("output/out-capacidade-banda-uf.csv")
    print(f"\n### 2. BANDA DE CAPACIDADE (CNES {COMPET_CNES})")
    print(f"  TETO  — estabelecimentos com TC disponivel ao SUS: {cap.teto_estab.sum():,}"
          f"  ({cap.teto_equip.sum():,} equipamentos)")
    print(f"  PISO  — TC + hemodinamica no mesmo CNES:           {cap.piso_estab.sum():,}"
          f"  ({100*cap.piso_estab.sum()/cap.teto_estab.sum():.1f}% do teto)")
    zero = sorted(cap[cap.piso_estab == 0].index)
    print(f"  UFs com PISO = 0: {zero if zero else 'nenhuma'}")

    # --- 3. demanda x capacidade por UF ------------------------------------
    dem = comp[comp.procedimento != "0211020010"].groupby("uf").qtd.sum().rename("exames_func")
    cate = comp[comp.procedimento == "0211020010"].groupby("uf").qtd.sum().rename("cateterismo")
    m = cap.join(dem).join(cate).fillna(0)
    m["exames_por_tc_ano"] = (m.exames_func / m.teto_equip).round(1)
    m.to_csv("output/out-demanda-x-capacidade-uf.csv")
    print("\n### 3. DEMANDA FUNCIONAL POR TOMOGRAFO-SUS (proxy de pressao)")
    cols = [c for c in ["teto_equip", "piso_estab", "exames_func", "cateterismo",
                        "exames_por_tc_ano"] if c in m.columns]
    print(m.sort_values("exames_por_tc_ano")[cols].to_string(float_format=lambda x: f"{x:,.0f}"))

    # --- 4. SIH: desfecho invasivo -----------------------------------------
    if os.path.exists("data/dac_sih.csv"):
        sih = pd.read_csv("data/dac_sih.csv", dtype={"procedimento": str, "cnes": str})
        ang = sih[sih.procedimento.str.startswith("0406030")]
        rev = sih[sih.procedimento.str.startswith("040601093")]
        inv = pd.concat([ang, rev])
        out = pd.DataFrame({
            "angioplastia_qtd": ang.groupby("uf").qtd.sum(),
            "angioplastia_r$": ang.groupby("uf").valor.sum(),
            "revasc_qtd": rev.groupby("uf").qtd.sum(),
            "revasc_r$": rev.groupby("uf").valor.sum(),
            "estab_invasivos": inv.groupby("uf").cnes.nunique(),
        }).fillna(0)
        out.to_csv("output/out-sih-invasivo-uf.csv")
        print(f"\n### 4. REDE INVASIVA (SIH {ANO})")
        print(f"  angioplastia coronariana: {ang.qtd.sum():,.0f} proc | "
              f"R$ {ang.valor.sum()/1e6:,.0f} mi | {ang.cnes.nunique()} estab")
        print(f"  revascularizacao miocardica: {rev.qtd.sum():,.0f} proc | "
              f"R$ {rev.valor.sum()/1e6:,.0f} mi | {rev.cnes.nunique()} estab")
        print(f"  rede invasiva total: {inv.cnes.nunique()} estabelecimentos "
              f"vs {cap.teto_estab.sum():,} com TC-SUS "
              f"(razao 1:{cap.teto_estab.sum()/inv.cnes.nunique():.1f})")
        print(f"  UFs sem nenhum procedimento invasivo: "
              f"{sorted(set(UFS) - set(inv.uf.unique()))}")

    print("\nCSVs: out-demanda-nacional.csv, out-capacidade-banda-uf.csv, "
          "out-demanda-x-capacidade-uf.csv, out-sih-invasivo-uf.csv")


if __name__ == "__main__":
    main()
