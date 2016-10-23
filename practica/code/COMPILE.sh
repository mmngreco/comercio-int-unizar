#!/bin/bash

jupyter nbconvert --to latex --template revtex_nocode.tplx analysis.ipynb --config /Users/mmngreco/Documents/comercio-int-unizar/practica/code/jupyter_nbconvert_config.py
pdflatex analysis.tex
bibtex analysis.aux
pdflatex analysis.tex
pdflatex analysis.tex

rm *.bbl *.aux *.blg *.log *.out *Notes.bib #*.tex
