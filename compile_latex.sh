#!/bin/bash

python trim_authors.py
pdflatex -interaction=nonstopmode -shell-escape main.tex
makeglossaries "main"
bibtex main
pdflatex -interaction=nonstopmode -shell-escape main.tex
pdflatex -interaction=nonstopmode -shell-escape main.tex

echo "LaTeX compilation completed."
