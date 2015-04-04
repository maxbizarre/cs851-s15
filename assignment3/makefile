all:
	pdflatex main.tex 
	bibtex main.aux
	pdflatex main.tex 
	pdflatex main.tex 
	mv main.pdf masroor.pdf

clean:
	rm masroor.pdf *.aux *.log *.toc *.bbl
	

