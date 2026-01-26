#!/bin/bash

clear
latexmk -C

yes "" | pdflatex --shell-escape Bibliography.tex
bibtex Bibliography   
yes "" | pdflatex --shell-escape Bibliography.tex
yes "" | pdflatex --shell-escape Bibliography.tex