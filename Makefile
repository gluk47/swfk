VERSION = `egrep 'Version\s*(.*)' swfk.tex | cut -d' ' -f2 | tr -d "\\\n\f\r"`

OUTPUT = target

dist : clean
	latex --output-directory=$(OUTPUT) swfk.tex
	makeindex $(OUTPUT)/swfk.idx
	latex --output-directory=$(OUTPUT) swfk.tex
	dvipdf $(OUTPUT)/swfk.dvi $(OUTPUT)/swfk-$(VERSION).pdf
	zip $(OUTPUT)/swfk.zip $(OUTPUT)/swfk-$(VERSION).pdf

test :
	#@./check.py ch1.tex
	#@./check.py ch2.tex
	#@./check.py ch3.tex
	#@./check.py ch4.tex
	#@./check.py ch5.tex
	#@./check.py ch6.tex
	#@./check.py ch7.tex
	#@./check.py ch8.tex
	#@./check.py ch9.tex
	#./check.py appendixa.tex
	#./check.py appendixb.tex
	./check.py appendixc.tex
	./check.py appendixd.tex

clean :
	@rm -f *~
