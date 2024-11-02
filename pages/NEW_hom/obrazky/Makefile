default: t2_hasse.pdf component2.pdf component1.pdf

.PRECIOUS: %.eps

%.pdf: %.eps
	epstopdf $(*F).eps

%.eps: %.ps
	ps2eps $(*F).ps -f -l

%.ps: %.dvi
	dvips -o $@ $(*F).dvi

%.dvi: %.tex
	latex $(*F)


