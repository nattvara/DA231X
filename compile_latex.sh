#!/bin/bash

python trim_authors.py
pdflatex -interaction=nonstopmode main.tex
makeglossaries "main"
bibtex main
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex

echo "LaTeX compilation completed."
