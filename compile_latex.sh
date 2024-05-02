#!/bin/bash

makeglossaries "main" && \
pdflatex -interaction=nonstopmode main.tex && \
bibtex main && \
pdflatex -interaction=nonstopmode main.tex && \
pdflatex -interaction=nonstopmode main.tex

echo "LaTeX compilation completed."
