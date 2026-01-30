#!/bin/bash

clear
latexmk -C

yes "" | pdflatex --shell-escape bibliography.tex
bibtex bibliography   
yes "" | pdflatex --shell-escape bibliography.tex
yes "" | pdflatex --shell-escape bibliography.tex