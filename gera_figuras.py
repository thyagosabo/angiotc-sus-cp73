#!/usr/bin/env python3
"""Figuras do manuscrito (ABC) e do suplemento, a partir de output/ e das constantes do modelo.

Uso: python3 gera_figuras.py  -> figuras/fig1-capacidade-uf.png, fig2-preco-x-delta.png,
     fig-central.png, figS1-tornado.png (PNG 300 dpi + PDF vetorial).
Constantes replicam analise_final.py (C_CATE, C_PCI, Δ dos ensaios, revascularização); as faixas por
estrato vêm de output/out-limiar-por-estrato.csv e a capacidade de output/out-capacidade-canais-uf.csv.
"""
import pathlib, pandas as pd, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

OUT = pathlib.Path("figuras"); OUT.mkdir(exist_ok=True)
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 8, "axes.spines.top": False, "axes.spines.right": False,
                     "axes.titlesize": 9, "axes.titleweight": "bold", "axes.labelsize": 8, "legend.fontsize": 7,
                     "xtick.labelsize": 7, "ytick.labelsize": 7, "figure.dpi": 110})
CM = 1 / 2.54
DARK, MID, LIGHT, ACC, RED = "#1f3b4d", "#5b7c8d", "#c9d3d9", "#0b7a75", "#a63d40"

# ---- constantes do modelo (analise_final.py) ----
C_CATE, C_CATE_AIH = 730.14, 772.80
C_PCI, C_CRM = 7713.3, 25904.4
C_ADIT, C_MIX, C_ERGO, C_ECO, C_CINT = 0.0, 185.46, 32.20, 196.39, 786.83
PRECOS = [("R$ 196 (proxy TC tórax)", 196.41), ("R$ 550 (demandante)", 550.00), ("R$ 623 (microcusteio 2022 corrigido)", 622.54),
          ("R$ 1.312 (saúde suplementar)", 1311.95)]
FIRST = [("CAPP", 100 * (51 / 245 - 66 / 243)), ("PROMISE", -4.1), ("Foy (estável)", -2.9), ("Foy (13 ensaios)", -2.6),
         ("CRESCENT-I", -1.0), ("SCOT-HEART 20 m", 100 * (401 - 409) / 2073), ("SCOT-HEART 5 a", 100 * (502 - 491) / 2073),
         ("CRESCENT-II", 1.4), ("PRECISE", 4.1)]
GATE = [("CONSERVE", 89.0 - 23.0), ("Reis 2022", 100 * (105 / 105 - 32 / 115)), ("DISCHARGE", 100 * (1708 / 1753 - 404 / 1808)),
        ("CAD-MAN", 100 * (162 / 162 - 24 / 167))]
LO, HI = min(d for _, d in FIRST if not _.startswith("SCOT")), max(d for _, d in FIRST)   # −6,3 a +4,1
GLO, GHI = GATE[0][1], GATE[-1][1]                                                          # 66,0 a 85,6
# filtro: só exames = Δ·C_CATE; com revascularização = + crédito (DISCHARGE −3,8/100; CONSERVE −5,0/100, só angioplastia)
F_LO, F_HI = GLO * C_CATE / 100, GHI * C_CATE / 100
F_REV = sorted([GATE[2][1] * C_CATE / 100 + 3.8 * C_PCI / 100, GATE[0][1] * C_CATE / 100 + 5.0 * C_PCI / 100])

cap = pd.read_csv("output/out-capacidade-canais-uf.csv", index_col=0)
est = pd.read_csv("output/out-limiar-por-estrato.csv")
def row(nome): return est[est.comparador_premissa.str.contains(nome, regex=False)].iloc[0]


def fig1():
    d = cap.sort_values("ge64_por_mi", ascending=True)
    y = np.arange(len(d))
    fig, (a, b) = plt.subplots(1, 2, figsize=(17 * CM, 12 * CM), sharey=True, gridspec_kw={"width_ratios": [1.6, 1]}, constrained_layout=True)
    cols = [DARK if r > 0 else (RED if e == 0 else MID) for r, e in zip(d.ready, d.ge64_equip)]
    a.barh(y, d.ge64_por_mi, color=cols, height=0.72)
    for i, (uf, r) in enumerate(d.iterrows()):
        txt = f"{int(r.ge64_equip)} equip. em {int(r.ge64_estab)} estab. · {int(r.ready)} pronto(s)" if r.ge64_equip > 0 else "nenhum ≥64 canais confirmado"
        a.text(r.ge64_por_mi + 0.08, i, txt, va="center", fontsize=6, color=RED if r.ge64_equip == 0 else ("#333" if r.ready > 0 else MID))
    a.set_yticks(y); a.set_yticklabels(d.index)
    dens = 1e6 * cap.ge64_equip.sum() / cap.populacao.sum()
    a.axvline(dens, color=ACC, ls="--", lw=0.9); a.text(dens + 0.06, len(d) - 0.4, f"média nacional {dens:.2f}/mi".replace(".", ","), color=ACC, fontsize=6.3)
    a.set_xlim(0, 9.2); a.set_xlabel("Tomógrafos ≥64 canais por milhão de habitantes")
    cv1 = cap.ge64_por_mi.std() / cap.ge64_por_mi.mean(); cv2 = cap.all_tc_por_mi.std() / cap.all_tc_por_mi.mean()
    a.set_title("A. ≥64 canais confirmados: 432 em 315 estabelecimentos (piso: 74,6% dos\nestabelecimentos ainda sob código genérico); 79 prontos; coef. de variação " + f"{cv1:.2f}".replace(".", ","), loc="left", fontsize=7.2)
    b.barh(y, d.all_tc_por_mi, color=LIGHT, height=0.72)
    for i, (uf, r) in enumerate(d.iterrows()):
        b.text(r.all_tc_por_mi + 0.4, i, f"{r.all_tc_por_mi:.1f}".replace(".", ","), va="center", fontsize=6, color="#555")
    b.set_xlim(0, 36); b.set_xlabel("Todos os tomógrafos, por milhão")
    b.set_title("B. Parque total (3.953);\ncoef. de variação " + f"{cv2:.2f}".replace(".", ","), loc="left", fontsize=7.2)
    fig.suptitle("Capacidade tomográfica compatível com angioTC por UF (CNES 06/2026)", fontsize=9, fontweight="bold")
    a.legend(handles=[Patch(color=DARK, label="UF com ≥1 estabelecimento pronto (≥64 canais + hemodinâmica + produção coronariana em 2025)"),
                      Patch(color=MID, label="≥64 canais confirmados, sem estabelecimento pronto"), Patch(color=RED, label="nenhum ≥64 canais confirmado (AP, PI, TO)")],
             loc="upper left", bbox_to_anchor=(-0.06, -0.14), frameon=False, fontsize=6.2, handlelength=1.1, labelspacing=0.5)
    fig.savefig(OUT / "fig1-capacidade-uf.png", dpi=300); fig.savefig(OUT / "fig1-capacidade-uf.pdf"); plt.close(fig)


def fig2():
    fig, (a, b) = plt.subplots(1, 2, figsize=(17 * CM, 10 * CM), sharey=True, gridspec_kw={"width_ratios": [1.2, 1]}, constrained_layout=True)
    x = np.linspace(-8, 6, 50)
    a.axvspan(LO, HI, color="#eef2f4", zorder=0, label="faixa de Δ observada em primeira linha (−6,3 a +4,1)")
    for C, lab, c in [(C_CINT, "cintilografia (R$ 787)", DARK), (C_MIX, "mix médio do SIA (R$ 185)", MID), (C_ADIT, "adoção aditiva (R$ 0)", ACC)]:
        a.plot(x, C + x * C_CATE / 100, color=c, lw=1.6, label=f"C_substituído = {lab}")
    marks = [("CAPP −6,3", LO), ("PROMISE −4,1", -4.1), ("Foy −2,9 / −2,6", -2.75), ("CRESCENT-I −1,0", -1.0),
             ("SCOT-HEART −0,4 / +0,5", 0.07), ("CRESCENT-II +1,4", 1.4), ("PRECISE +4,1", 4.1)]
    for n, d in marks:
        a.axvline(d, color="#999", lw=0.5, ls=":", zorder=0)
        a.text(d, -85, n, rotation=90, fontsize=5.6, ha="center", va="bottom", color="#444")
    a.set_xlim(-8, 6); a.set_xlabel("Δ de cateterismo total por 100 pacientes (positivo = evitados)")
    a.set_ylabel("Preço de neutralidade da angioTC (R$)"); a.set_title("A. Primeira linha:\nP = C_substituído + Δ·C_CATE/100", loc="left", fontsize=8)
    a.legend(loc="upper left", frameon=False, fontsize=6.4)
    xg = np.linspace(60, 96, 30)
    b.plot(xg, xg * C_CATE / 100, color=DARK, lw=1.6, label="C_CATE = R$ 730,14 (SIA 2025)")
    b.plot(xg, xg * C_CATE_AIH / 100, color=DARK, lw=0.9, ls="--", label="C_CATE = R$ 772,80 (AIH)")
    off = {"CONSERVE": (0.6, -70), "Reis 2022": (-11.2, 175), "DISCHARGE": (0.6, -70), "CAD-MAN": (0.6, -50)}
    for n, d in GATE:
        P = d * C_CATE / 100; dx, dy = off[n]
        b.plot(d, P, "o", color=ACC, ms=4.5, zorder=3)
        lab = f"{n}: Δ {d:.1f} → R$ {P:.0f}".replace(f"{d:.1f}", f"{d:.1f}".replace(".", ","))
        if n == "Reis 2022":
            b.annotate(lab, xy=(d, P), xytext=(d + dx, P + dy), fontsize=6, ha="left", va="center", arrowprops=dict(arrowstyle="-", color="#777", lw=0.6))
        else:
            b.text(d + dx, P + dy, lab, fontsize=6, ha="left" if dx > 0 else "right", va="center")
    b.set_xlim(60, 96); b.set_xlabel("Δ de cateterismo total por 100 pacientes")
    b.set_title("B. Filtro pré-cateterismo (exame prévio cancela):\nP = Δ·C_CATE/100", loc="left", fontsize=8)
    b.legend(loc="upper left", frameon=False, fontsize=6.4)
    for ax in (a, b):
        for lab, P in PRECOS[:3]:
            ax.axhline(P, color=RED if P == 550 else "#777", lw=0.9 if P == 550 else 0.6, ls="--", zorder=0)
        ax.set_ylim(-100, 1000); ax.axhline(0, color="#000", lw=0.5)
    b.text(95.6, PRECOS[0][1] + 12, PRECOS[0][0], fontsize=6, color="#555", ha="right", va="bottom")
    b.text(95.6, PRECOS[1][1] - 30, PRECOS[1][0], fontsize=6, color=RED, ha="right", va="top")
    b.text(60.4, PRECOS[2][1] + 12, PRECOS[2][0], fontsize=6, color="#555", ha="left", va="bottom")
    b.text(95.6, 300, "R$ 1.312 (saúde suplementar): fora da escala", fontsize=6, color="#555", ha="right", va="top")
    fig.savefig(OUT / "fig2-preco-x-delta.png", dpi=300); fig.savefig(OUT / "fig2-preco-x-delta.pdf"); plt.close(fig)


def central():
    fig, (a, b) = plt.subplots(1, 2, figsize=(18 * CM, 12.5 * CM), gridspec_kw={"width_ratios": [1.0, 1.45]}, constrained_layout=True)
    fig.suptitle("Onde a angiotomografia coronariana gera valor no SUS?", fontsize=10.5, fontweight="bold")
    # A — capacidade
    d = cap.sort_values("ge64_por_mi", ascending=True)
    cols = [DARK if r > 0 else (RED if e == 0 else MID) for r, e in zip(d.ready, d.ge64_equip)]
    a.barh(np.arange(len(d)), d.ge64_por_mi, color=cols, height=0.75)
    for i, (uf, r) in enumerate(d.iterrows()):
        a.text(r.ge64_por_mi + 0.08, i, (f"{int(r.ready)}" if r.ready > 0 else ("sem ≥64" if r.ge64_equip == 0 else "0")), va="center", fontsize=5.6,
               color=DARK if r.ready > 0 else (RED if r.ge64_equip == 0 else MID))
    a.set_yticks(np.arange(len(d))); a.set_yticklabels(d.index, fontsize=5.8)
    a.set_xlim(0, 7.2); a.set_xlabel("Tomógrafos ≥64 canais por milhão de hab.\n(número ao lado = estabelecimentos prontos)", fontsize=6.8)
    a.set_title("A. Capacidade (CNES 06/2026): 432 tomógrafos\n≥64 canais (piso) em 315 estabelecimentos;\n79 prontos; 12 UFs sem nenhum pronto", loc="left", fontsize=7.2)
    a.legend(handles=[Patch(color=DARK, label="UF com estabelecimento pronto\n(≥64 + hemodinâmica + produção coronariana)"),
                      Patch(color=MID, label="≥64 confirmado, sem estabelecimento pronto"), Patch(color=RED, label="nenhum ≥64 confirmado (AP, PI, TO)")],
             loc="upper left", bbox_to_anchor=(-0.1, -0.13), frameon=False, fontsize=5.6, handlelength=1.1, labelspacing=0.5)
    # B — preço de neutralidade por estrato
    rows = [("Sem protocolo: aditiva (R$ 0)", row("adocao aditiva")),
            ("Baixa: ergometria (R$ 32)", row("teste ergometrico")),
            ("PICO submetido: mix do SIA (R$ 185)", row("mix medio")),
            ("Intermediária: eco de estresse (R$ 196)", row("ecocardiografia")),
            ("Intermediária c/ protocolo:\ncintilografia (R$ 787)", row("cintilografia"))]
    labels = [r[0] for r in rows] + ["Filtro pré-cateterismo\n(exame prévio cancela)"]
    so = [(r.P_lo_so_exames, r.P_hi_so_exames) for _, r in rows] + [(F_LO, F_HI)]
    com = [(r.P_lo_com_revasc, r.P_hi_com_revasc) for _, r in rows] + [tuple(F_REV)]
    y = np.arange(len(labels))[::-1]
    b.axvspan(-330, 30, color="#f6ecec", zorder=0)
    b.text(-320, len(labels) - 0.35, "aditiva: teto R$ 30", fontsize=6, color=RED, va="center")
    for yi, (l1, h1), (l2, h2) in zip(y, so, com):
        b.barh(yi + 0.19, h1 - l1, left=l1, height=0.34, color="white", edgecolor=DARK, hatch="////", lw=0.8)
        b.barh(yi - 0.19, h2 - l2, left=l2, height=0.34, color=DARK)
        b.text(max(h1, h2) + 12, yi, f"{l1:.0f} a {h1:.0f} | {l2:.0f} a {h2:.0f}".replace("-", "−"), va="center", fontsize=5.6, color="#333")
    b.axvline(550, color=RED, lw=1, ls="--"); b.text(540, len(labels) - 0.3, "R$ 550\n(demandante)", color=RED, fontsize=6, ha="right", va="center")
    b.set_ylim(-0.7, len(labels) - 0.1)
    b.axvline(622.54, color="#666", lw=0.8, ls="--"); b.text(632, len(labels) - 0.3, "R$ 623\n(microcusteio)", color="#555", fontsize=6, ha="left", va="center")
    b.axvline(0, color="#000", lw=0.5)
    b.set_yticks(y); b.set_yticklabels(labels, fontsize=6.2); b.set_xlim(-330, 1150)
    b.set_xlabel("Preço de neutralidade da angioTC (R$)", fontsize=6.8)
    b.set_title("B. Preço de neutralidade por estrato e posição no percurso:\no que a angioTC substitui e onde entra decidem o sinal", loc="center", fontsize=7.2)
    b.legend(handles=[Patch(facecolor="white", edgecolor=DARK, hatch="////", label="só exames e cateterismo (Δ de cateterismo dos ensaios)"),
                      Patch(color=DARK, label="incluindo a revascularização observada nos ensaios")],
             loc="upper left", bbox_to_anchor=(0.0, -0.13), frameon=False, fontsize=5.6, handlelength=1.1, labelspacing=0.5)
    fig.savefig(OUT / "fig-central.png", dpi=300); fig.savefig(OUT / "fig-central.pdf"); plt.close(fig)


def tornado():
    def P1(C=C_CINT, dc=(LO + HI) / 2, dr=(2.7 + 4.0) / 2, cr=C_PCI, cc=C_CATE): return C + dc * cc / 100 - dr * cr / 100
    def P2(dc=GATE[2][1], dr=-3.8, cr=C_PCI, cc=C_CATE): return dc * cc / 100 - dr * cr / 100
    C_MIXREV = (3.75 * C_PCI + 0.27 * C_CRM) / 4.02   # mix de revascularização do PRECISE (≈93% angioplastia)
    P1b, P2b = P1(), P2()
    e = lambda s: s.replace("$", "\\$")   # evita mathtext do matplotlib entre dois "$"
    v1 = [(e("C_substituído: R$ 0 (aditiva)\n→ R$ 787 (cintilografia)"), P1(C=0), P1(C=C_CINT)),
          ("Δ_revasc: 0 → +4,0/100 (PRECISE)", P1(dr=0), P1(dr=4.0)),
          ("Δ_CATE: −6,3 (CAPP) → +4,1 (PRECISE)", P1(dc=LO), P1(dc=HI)),
          (e("C_revasc: R$ 7.713 (angioplastia)\n→ R$ 8.935 (mix do PRECISE)"), P1(cr=C_PCI), P1(cr=C_MIXREV)),
          (e("C_CATE: R$ 730 (SIA) → R$ 773 (AIH)"), P1(cc=C_CATE), P1(cc=C_CATE_AIH))]
    v2 = [("Δ_CATE: 66,0 (CONSERVE)\n→ 85,6 (CAD-MAN)", P2(dc=GLO), P2(dc=GHI)),
          ("Δ_revasc: 0 → −5,0/100 (CONSERVE)", P2(dr=0), P2(dr=-5.0)),
          (e("C_revasc: R$ 7.713 → R$ 8.935"), P2(cr=C_PCI), P2(cr=C_MIXREV)),
          (e("C_CATE: R$ 730 → R$ 773"), P2(cc=C_CATE), P2(cc=C_CATE_AIH))]
    fig, axes = plt.subplots(2, 1, figsize=(16 * CM, 12.5 * CM), gridspec_kw={"height_ratios": [1.2, 1]}, constrained_layout=True)
    for ax, vals, base, title in [(axes[0], v1, P1b, e(f"A. Primeira linha, intermediária com protocolo (cintilografia)\nCaso-base R$ {P1b:.0f}: Δ_CATE −1,1; Δ_revasc +3,35; C_revasc angioplastia")),
                                  (axes[1], v2, P2b, e(f"B. Filtro pré-cateterismo (DISCHARGE)\nCaso-base R$ {P2b:.0f}: Δ_CATE 75,1; Δ_revasc −3,8; C_revasc angioplastia"))]:
        vals = sorted(vals, key=lambda t: abs(t[2] - t[1]))
        y = np.arange(len(vals))
        for yi, (lab, lo, hi) in zip(y, vals):
            ax.barh(yi, min(lo, hi) - base, left=base, color=MID, height=0.55)
            ax.barh(yi, max(lo, hi) - base, left=base, color=DARK, height=0.55)
            lab_v = f"{min(lo,hi):.0f} a {max(lo,hi):.0f}" if abs(hi - lo) >= 1 else e(f"{base:.0f} (efeito < R$ 1)")
            ax.text(max(lo, hi) + 10, yi, lab_v.replace("-", "−"), ha="left", va="center", fontsize=6.2)
        ax.axvline(base, color="#000", lw=0.7); ax.axvline(550, color=RED, lw=0.9, ls="--")
        ax.set_yticks(y); ax.set_yticklabels([v[0] for v in vals], fontsize=6.2)
        ax.set_xlabel(e("Preço de neutralidade (R$); tracejado vermelho = R$ 550"), fontsize=7); ax.set_title(title, loc="left", fontsize=7.4)
        lo_all = min(min(v[1], v[2]) for v in vals); hi_all = max(max(v[1], v[2]) for v in vals)
        ax.set_xlim(lo_all - 60, hi_all + 120)
    fig.savefig(OUT / "figS1-tornado.png", dpi=300); fig.savefig(OUT / "figS1-tornado.pdf"); plt.close(fig)
    return P1b, P2b


if __name__ == "__main__":
    fig1(); fig2(); central(); p1, p2 = tornado()
    print("figuras em", OUT, "| tornado casos-base:", round(p1, 1), round(p2, 1), "| filtro:", round(F_LO), round(F_HI), [round(v) for v in F_REV])
