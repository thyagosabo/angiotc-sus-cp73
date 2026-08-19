#!/usr/bin/env python3
"""Pacote de submissão ABC: python3 gera_submissao.py -> submissao-abc/

- pagina-titulo.docx     título/autores/correspondência (a parte identificada)
- manuscrito-cego.docx   resumos + corpo + refs, sem autores e sem figuras embutidas
- suplemento.docx        material suplementar (sem autores)
- carta-apresentacao.docx
- fig-central.jpg, fig1.jpg, fig2.jpg, figS1.jpg (300 dpi, via sips)
Requer pandoc e macOS (sips). Fonte da verdade continua sendo os .md.
"""
import pathlib, re, subprocess

OUT = pathlib.Path("submissao-abc"); OUT.mkdir(exist_ok=True)
t = pathlib.Path("manuscrito-abc.md").read_text()

i = t.index("## Resumo")
titulo, corpo = t[:i], t[i:]
j, k = corpo.index("## Declarações"), corpo.index("## Legendas")
titulo += "\n" + corpo[j:k]                                        # declarações vão na página de título
corpo = corpo[:j] + corpo[k:]
corpo = re.sub(r"!\[[^\]]*\]\([^)]*\)\n*", "", corpo)              # figuras vão em arquivos separados
corpo = re.sub(r"\^([0-9][0-9,–\-– ]*)\^", r"^^\1^^", corpo)   # ^n^ -> sobrescrito pandoc (^...^)
corpo = corpo.replace("^^", "^")

def pandoc(md_text, dest):
    subprocess.run(["pandoc", "-f", "markdown+superscript", "-t", "docx", "-o", str(dest)],
                   input=md_text, text=True, check=True)
    print(dest)

pandoc(titulo, OUT / "pagina-titulo.docx")
pandoc("# Onde a angiotomografia coronariana gera valor no Sistema Único de Saúde? Capacidade instalada, limiar orçamentário e o caso do filtro pré-cateterismo\n\n" + corpo,
       OUT / "manuscrito-cego.docx")
pandoc(pathlib.Path("manuscrito-suplemento.md").read_text(), OUT / "suplemento.docx")
pandoc(pathlib.Path("carta-apresentacao.md").read_text(), OUT / "carta-apresentacao.docx")

for src, dst in [("fig-central", "figura-central"), ("fig1-capacidade-uf", "figura-1"),
                 ("fig2-preco-x-delta", "figura-2"), ("figS1-tornado", "figura-S1")]:
    subprocess.run(["sips", "-s", "format", "jpeg", "-s", "formatOptions", "95",
                    f"figuras/{src}.png", "--out", str(OUT / f"{dst}.jpg")],
                   check=True, stdout=subprocess.DEVNULL)
    print(OUT / f"{dst}.jpg")
