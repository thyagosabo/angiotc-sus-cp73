#!/usr/bin/env python3
"""Markdown -> HTML -> PDF (Chrome headless). Uso: python3 gera_pdf.py contribuicao-cp73.md

Sem dados pessoais e sem imagens de pessoas (regra do formulário da CP). Tabelas largas
rolam? Não em PDF — por isso o CSS reduz a fonte das tabelas e usa A4 retrato com margens curtas.
"""
import subprocess, sys, os, pathlib, markdown

src = pathlib.Path(sys.argv[1]); html_path = src.with_suffix(".html"); pdf_path = src.with_suffix(".pdf")
body = markdown.markdown(src.read_text(encoding="utf-8"), extensions=["tables", "fenced_code", "sane_lists"])
CSS = """
@page { size: A4; margin: 16mm 14mm 16mm 14mm; }
html { font-family: -apple-system, "Helvetica Neue", Arial, sans-serif; font-size: 10.2pt; line-height: 1.38; color: #111; }
body { margin: 0; }
h1 { font-size: 16pt; margin: 0 0 6pt; line-height: 1.2; }
h2 { font-size: 13pt; margin: 16pt 0 6pt; border-bottom: 1px solid #999; padding-bottom: 2pt; page-break-after: avoid; }
h3 { font-size: 11pt; margin: 12pt 0 4pt; page-break-after: avoid; }
p, li { text-align: left; }
table { border-collapse: collapse; width: 100%; font-size: 8.4pt; margin: 6pt 0 8pt; page-break-inside: auto; }
th, td { border: 1px solid #bbb; padding: 2.5pt 4pt; vertical-align: top; }
th { background: #eee; }
tr { page-break-inside: avoid; }
code { font-family: Menlo, monospace; font-size: 8.6pt; background: #f3f3f3; padding: 0 2px; }
pre { background: #f3f3f3; padding: 6pt; font-size: 8.6pt; overflow: hidden; white-space: pre-wrap; }
blockquote { border-left: 3px solid #999; margin: 6pt 0; padding: 2pt 10pt; color: #222; }
hr { border: 0; border-top: 1px solid #bbb; margin: 12pt 0; }
"""
html = f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>{src.stem}</title><style>{CSS}</style></head><body>{body}</body></html>'
html_path.write_text(html, encoding="utf-8")
chrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
subprocess.run([chrome, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                f"--print-to-pdf={pdf_path.resolve()}", html_path.resolve().as_uri()], check=True,
               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=120)
print(pdf_path, os.path.getsize(pdf_path) // 1024, "KB")
