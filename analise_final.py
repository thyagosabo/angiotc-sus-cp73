#!/usr/bin/env python3
"""Reproduz todas as tabelas numéricas da contribuição à CP 73/2026.

Entradas: cnes/EQ*.dbc (06/2026), data-v2/dac_sia_g*.csv, data/dac_sih.csv,
sigtap/tb_procedimento.txt, IBGE (população 2025, IPCA).
Saídas: output/out-*.csv e um resumo no stdout, seção por seção do documento.

Recusa-se a rodar com cobertura parcial: exige 27 UFs e 12 competências no SIA.
"""
import glob, os, sys, json, urllib.request
import numpy as np, pandas as pd, datasus_dbc, dbfread

OUT = "output"; os.makedirs(OUT, exist_ok=True)
UFS = "AC AL AM AP BA CE DF ES GO MA MG MS MT PA PB PE PI PR RJ RN RO RR RS SC SE SP TO".split()

# ---- códigos, declarados uma vez (Apêndice A) ----------------------------
FUNC = {"0211020060": "Teste ergometrico", "0205010016": "Ecocardiografia de estresse",
        "0208010025": "Cintilografia perfusao - estresse", "0208010033": "Cintilografia perfusao - repouso",
        "0208010076": "Cintilografia camaras - esforco"}
CATE = "0211020010"
OCI_SCC = {"0902010034": "OCI aval diag inicial SCC", "0902010042": "OCI progressao I SCC",
           "0902010050": "OCI progressao II SCC"}
ANGIO = ["0406030014", "0406030022", "0406030030", "0406030049", "0406030065", "0406030073"]
REVASC = ["0406010927", "0406010935", "0406010943", "0406010951"]
GE64, SUB64, GEN, HEMO = ["29", "30"], ["26", "27", "28"], ["11"], "10"

# ---- parâmetros do modelo -------------------------------------------------
PRECOS = [("TC torax + contraste (proxy SIGTAP)", 196.41), ("Demandante", 550.00),
          ("Microcusteio 2022 corrigido", 622.54), ("CBHPM 2026", 1311.95)]
# Δ de cateterismo TOTAL por 100, extraídos das publicações primárias (Apêndice B)
FIRSTLINE = [("CAPP", 100 * (51 / 245 - 66 / 243)), ("PROMISE", -4.1), ("Foy estavel", -2.9),
             ("Foy 13", -2.6), ("CRESCENT-I", -1.0), ("CRESCENT-II", 1.4), ("PRECISE", 4.1)]
GATE = [("CONSERVE", 89.0 - 23.0), ("Reis 2022", 100 * (105 / 105 - 32 / 115)),
        ("DISCHARGE", 100 * (1708 / 1753 - 404 / 1808)), ("CAD-MAN", 100 * (162 / 162 - 24 / 167))]
SCOT = [("SCOT-HEART 6m", -1.2), ("SCOT-HEART 5a", 0.5)]  # aditivo: sem crédito de episódio


def ibge(agregado, periodo, variavel, loc):
    import gzip
    u = f"https://servicodados.ibge.gov.br/api/v3/agregados/{agregado}/periodos/{periodo}/variaveis/{variavel}?localidades={loc}"
    r = urllib.request.urlopen(urllib.request.Request(u, headers={"Accept-Encoding": "gzip"}), timeout=60)
    raw = r.read()
    if raw[:2] == b"\x1f\x8b": raw = gzip.decompress(raw)
    return json.loads(raw)[0]["resultados"][0]["series"]


def populacao():
    S = {'Acre': 'AC', 'Alagoas': 'AL', 'Amazonas': 'AM', 'Amapá': 'AP', 'Bahia': 'BA', 'Ceará': 'CE',
         'Distrito Federal': 'DF', 'Espírito Santo': 'ES', 'Goiás': 'GO', 'Maranhão': 'MA', 'Minas Gerais': 'MG',
         'Mato Grosso do Sul': 'MS', 'Mato Grosso': 'MT', 'Pará': 'PA', 'Paraíba': 'PB', 'Pernambuco': 'PE',
         'Piauí': 'PI', 'Paraná': 'PR', 'Rio de Janeiro': 'RJ', 'Rio Grande do Norte': 'RN', 'Rondônia': 'RO',
         'Roraima': 'RR', 'Rio Grande do Sul': 'RS', 'Santa Catarina': 'SC', 'Sergipe': 'SE', 'São Paulo': 'SP',
         'Tocantins': 'TO'}
    s = ibge(6579, 2025, 9324, "N3[all]")  # fixado em 2025, não -1
    return pd.Series({S[x["localidade"]["nome"]]: int(x["serie"]["2025"]) for x in s if x["localidade"]["nome"] in S})


def ipca_fator():
    a = float(list(ibge(1737, "202012", 2266, "N1[all]")[0]["serie"].values())[0])
    b = float(list(ibge(1737, "202607", 2266, "N1[all]")[0]["serie"].values())[0])
    return b / a


def cnes():
    rows = []
    for f in sorted(glob.glob("cnes/EQ*.dbc")):
        dbf = f[:-4] + ".dbf"
        if not os.path.exists(dbf): datasus_dbc.decompress(f, dbf)
        d = pd.DataFrame(iter(dbfread.DBF(dbf, encoding="latin-1"))); d["UF"] = os.path.basename(f)[2:4]; rows.append(d)
    eq = pd.concat(rows, ignore_index=True)
    eq["QT_USO"] = pd.to_numeric(eq.QT_USO, errors="coerce").fillna(0)
    return eq[(eq.IND_SUS == "1") & (eq.QT_USO > 0) & (eq.TIPEQUIP == "01")]


def gini_w(x, w):
    o = np.argsort(x); x, w = np.asarray(x)[o], np.asarray(w)[o]
    cw = np.cumsum(w) / w.sum(); cx = np.cumsum(x * w) / (x * w).sum()
    return 1 - np.sum((cw[1:] - cw[:-1]) * (cx[1:] + cx[:-1]))


def main():
    sia = pd.concat([pd.read_csv(f, dtype={"procedimento": str, "cnes": str}) for f in glob.glob("data-v2/dac_sia_g*.csv")], ignore_index=True)
    if sia.uf.nunique() != 27 or sia.competencia.nunique() != 12:
        sys.exit(f"COBERTURA PARCIAL: {sia.uf.nunique()}/27 UFs, {sia.competencia.nunique()}/12 competencias — NAO EXTRAPOLAR")
    sih = pd.read_csv("data/dac_sih.csv", dtype={"procedimento": str, "cnes": str})
    sus = cnes(); pop = populacao(); fator = ipca_fator()
    print(f"COBERTURA: SIA 27/27 UFs, 12/12 competencias | IPCA 12/2020->07/2026 = {fator:.4f}\n")

    # ================= §2 CAPACIDADE =================
    tc = sus[sus.CODEQUIP.isin(GE64 + SUB64 + GEN)]
    ge = tc[tc.CODEQUIP.isin(GE64)]; sub = tc[tc.CODEQUIP.isin(SUB64)]; gen = tc[tc.CODEQUIP.isin(GEN)]
    geS, subS, genS = set(ge.CNES), set(sub.CNES), set(gen.CNES)
    print("### 2.1 estratificacao")
    for n, df in [("compativel >=64 (29+30)", ge), ("  64 canais (29)", ge[ge.CODEQUIP == "29"]),
                  ("  128 canais (30)", ge[ge.CODEQUIP == "30"]), ("incompativel <64 (26-28)", sub),
                  ("nao declarado (11)", gen)]:
        print(f"  {n:<28} {df.CNES.nunique():>5} estab {df.QT_USO.sum():>6.0f} equip")
    print(f"  {'TOTAL':<28} {len(geS | subS | genS):>5} estab {tc.QT_USO.sum():>6.0f} equip")
    print(f"  sobreposicao >=64 & <64: {len(geS & subS)} | 64 & 128: {len(set(ge[ge.CODEQUIP=='29'].CNES) & set(ge[ge.CODEQUIP=='30'].CNES))}")
    recl = geS | subS; tot = len(recl | genS)
    print(f"\n### 2.2 reclassificacao: >=1 reclassificado {len(recl)} ({100*len(recl)/tot:.1f}%) | integral {len(recl-genS)} ({100*len(recl-genS)/tot:.1f}%) | ainda cod 11 {len(genS)} ({100*len(genS)/tot:.1f}%) | ambos {len(recl & genS)}")

    hemo = set(sus[sus.CODEQUIP == HEMO].CNES)
    coron = set(sih[sih.procedimento.isin(ANGIO + REVASC)].cnes)
    print(f"\n### 2.3 estratos: >=64 {len(geS)} | +hemo {len(geS & hemo)} | +coron {len(geS & coron)} | READY {len(geS & hemo & coron)}")

    cap = pd.DataFrame({"ge64_equip": ge.groupby("UF").QT_USO.sum(), "ge64_estab": ge.groupby("UF").CNES.nunique(),
                        "sub64_estab": sub.groupby("UF").CNES.nunique(), "gen_estab": gen.groupby("UF").CNES.nunique()}).reindex(UFS).fillna(0).astype(int)
    cap["ready"] = [len(set(ge[ge.UF == u].CNES) & hemo & coron) for u in cap.index]
    cap["populacao"] = pop; cap["ge64_por_mi"] = (1e6 * cap.ge64_equip / cap.populacao).round(2)
    cap["all_tc_por_mi"] = (1e6 * tc.groupby("UF").QT_USO.sum().reindex(UFS).fillna(0) / cap.populacao).round(2)
    cap.to_csv(f"{OUT}/out-capacidade-canais-uf.csv")
    print(f"\n### 2.4 densidade >=64: {1e6*ge.QT_USO.sum()/pop.sum():.2f}/mi | zero >=64: {sorted(cap[cap.ge64_equip==0].index)} | zero ready ({(cap.ready==0).sum()}): {sorted(cap[cap.ready==0].index)}")
    print(f"  SP: {cap.loc['SP','ge64_equip']} equip, {cap.loc['SP','ready']} ready | DF {cap.loc['DF','ge64_por_mi']}/mi")
    print(f"  CV >=64 {cap.ge64_por_mi.std()/cap.ge64_por_mi.mean():.2f} vs todos {cap.all_tc_por_mi.std()/cap.all_tc_por_mi.mean():.2f} | Gini pop {gini_w(cap.ge64_por_mi, cap.populacao):.2f} vs {gini_w(cap.all_tc_por_mi, cap.populacao):.2f}")
    tcload = sia[sia.procedimento.str.startswith("0206") & (sia.procedimento != "0206010095")].qtd.sum()
    print(f"  carga TC (0206 exc PET): {tcload/1e6:.1f} mi | por equip: {tcload/tc.QT_USO.sum():,.0f} (parque) / {tcload/gen.QT_USO.sum():,.0f} (cod 11)")

    # ================= §3 CENARIO ATUAL =================
    f = sia[sia.procedimento.isin(FUNC)]
    q = f.groupby("procedimento").qtd.sum(); v = f.groupby("procedimento").valor.sum()
    Ne = q["0211020060"] + q["0208010025"] + q["0205010016"] + q["0208010076"]; Ve = v.sum()
    print(f"\n### 3.1 episodios: ergo {q['0211020060']:,.0f} | cintilo {q['0208010025']:,.0f} (rep {q['0208010033']:,.0f}, liq {q['0208010025']-q['0208010033']:,.0f}) | eco {q['0205010016']:,.0f} | camaras {q['0208010076']:,.0f}")
    print(f"  total {Ne:,.0f} epis | R$ {Ve/1e6:.1f} mi | R$ {Ve/Ne:.2f}/epis | procedimentos {q.sum():,.0f} (+{100*(q.sum()/Ne-1):.0f}%)")
    print(f"  gasto: ergo {100*v['0211020060']/Ve:.1f}% | cintilo {100*(v['0208010025']+v['0208010033'])/Ve:.1f}% | eco {100*v['0205010016']/Ve:.1f}%")
    C_EP = Ve / Ne
    cate = sia[sia.procedimento == CATE]; C_CATE = cate.valor.sum() / cate.qtd.sum()
    print(f"  cateterismo: {cate.qtd.sum():,.0f} | R$ {cate.valor.sum()/1e6:.1f} mi | R$ {C_CATE:.2f}")
    g = f[f.procedimento.isin(["0208010025", "0208010033"])].pivot_table(index=["cnes", "competencia"], columns="procedimento", values="qtd", aggfunc="sum").fillna(0)
    print(f"  por CNES-mes: estresse>repouso {(g['0208010025']-g['0208010033']).clip(lower=0).sum():,.0f} | repouso>estresse {(g['0208010033']-g['0208010025']).clip(lower=0).sum():,.0f}")

    oci = sia[sia.procedimento.isin(OCI_SCC)]
    zer = f[f.valor == 0].groupby("procedimento").qtd.sum().reindex(FUNC.keys()).fillna(0)
    pago = f[f.valor > 0]; qp = pago.groupby("procedimento").qtd.sum().reindex(FUNC.keys()).fillna(0)
    Nl = qp["0211020060"] + qp["0208010025"] + qp["0205010016"] + qp["0208010076"]; Vl = pago.valor.sum()
    No, Vo = oci.qtd.sum(), oci.valor.sum()
    print(f"\n### 3.2.1 OCI SCC: {No:,.0f} epis | R$ {Vo/1e6:.2f} mi | R$ {Vo/No:.2f} | {oci.cnes.nunique()} estab | {oci.uf.nunique()} UFs | {100*No/(Nl+No):.2f}%")
    for c, n in OCI_SCC.items(): print(f"    {c} {n:<28} {oci[oci.procedimento==c].qtd.sum():>7,.0f}")
    print(f"  zerados: ergo {zer['0211020060']:.0f} + estr {zer['0208010025']:.0f} + rep {zer['0208010033']:.0f} + eco {zer['0205010016']:.0f} = {zer.sum():.0f}")
    print(f"  legacy (valor>0): {Nl:,.0f} epis R$ {Vl/Nl:.2f} | ponderado {Nl+No:,.0f} R$ {(Vl+Vo)/(Nl+No):.2f} | delta intercepto +{(Vl+Vo)/(Nl+No)-C_EP:.2f}")
    print(f"  3.1 - legacy = {Ne-Nl:.0f} = zerados por estresse {zer['0211020060']+zer['0208010025']+zer['0205010016']:.0f}")
    o26 = sia[sia.procedimento == "0902010026"]; print(f"  OCI 0902010026 (nao examinada): {o26.qtd.sum():,.0f} epis")

    ang = sih[sih.procedimento.isin(ANGIO)]; rev = sih[sih.procedimento.isin(REVASC)]
    print(f"\n### 3.4 SIH: angioplastia {ang.qtd.sum():,.0f} R$ {ang.valor.sum()/1e6:,.0f} mi {ang.cnes.nunique()} estab | revasc {rev.qtd.sum():,.0f} R$ {rev.valor.sum()/1e6:,.0f} mi {rev.cnes.nunique()} estab | rede {len(coron)}")

    # ================= §4 LIMIAR =================
    C_CINT = (v["0208010025"] + v["0208010033"]) / q["0208010025"]
    subst = [("mix medio SIA", C_EP), ("mix NATS", 316.76), ("cintilografia", C_CINT)]
    print(f"\n### 4.3 delta necessario (C_CATE={C_CATE:.2f}; cintilo R$ {C_CINT:.2f})")
    print(f"  {'preco':<38}" + "".join(f"{s[0]:>16}" for s in subst))
    for pn, P in PRECOS:
        print(f"  {pn:<38}" + "".join(f"{(P-C)*100/C_CATE:>16.1f}" for _, C in subst))
    lo, hi = min(d for _, d in FIRSTLINE), max(d for _, d in FIRSTLINE)
    print(f"\n### 4.4 faixa primeira linha {lo:+.1f} a {hi:+.1f}")
    for sn, C in subst:
        print(f"  {sn:<16} P = R$ {C+lo*C_CATE/100:7.2f} a R$ {C+hi*C_CATE/100:7.2f}")
    print(f"  SCOT-HEART (aditivo, sem credito): " + " | ".join(f"{n} R$ {d*C_CATE/100:.2f}" for n, d in SCOT))
    print(f"\n### 4.5 gatekeeping (limiar R$550: {550*100/C_CATE:.1f} | R$622,54: {622.54*100/C_CATE:.1f})")
    for n, d in sorted(GATE, key=lambda x: x[1]):
        P = d * C_CATE / 100; print(f"  {n:<11} d={d:5.1f}  P=R$ {P:7.2f}  vs 622,54: {P-622.54:+.2f}  | C_CATE 772,80: R$ {d*772.80/100:.2f}")
    print(f"\n### IPCA: 452,05 x {fator:.4f} = R$ {452.05*fator:.2f}")

    pd.DataFrame([(pn, P) + tuple((P - C) * 100 / C_CATE for _, C in subst) for pn, P in PRECOS],
                 columns=["preco", "R$"] + [f"delta_nec_{s[0]}" for s in subst]).to_csv(f"{OUT}/out-limiar-por-preco-e-substituto.csv", index=False)
    pd.DataFrame(FIRSTLINE + SCOT + GATE, columns=["ensaio", "delta_por_100"]).to_csv(f"{OUT}/out-delta-ensaios.csv", index=False)
    print(f"\nCSVs em {OUT}/")


if __name__ == "__main__":
    main()
