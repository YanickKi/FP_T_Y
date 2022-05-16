all: build/main.pdf

# hier Python-Skripte:
#build/plot.pdf: plot.py matplotlibrc header-matplotlib.tex | build
#	TEXINPUTS=$$(pwd): python plot.py

build/TEM00.pdf: data_scripts/scripts/TEM00.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/scripts/TEM00.py

build/polarisation.pdf: data_scripts/scripts/polarisation.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/scripts/polarisation.py

build/wavelength.pdf: data_scripts/scripts/wavelength.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/scripts/wavelength.py
	
data_scripts/data/cavity.txt: data_scripts/scripts/cavity.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/scripts/cavity.py

build/stabilitaet.pdf: data_scripts/scripts/stabilitaet.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/scripts/stabilitaet.py

# hier weitere Abhängigkeiten für build/main.pdf deklarieren: 
build/main.pdf: build/TEM00.pdf build/polarisation.pdf build/wavelength.pdf data_scripts/data/cavity.txt build/stabilitaet.pdf

build/main.pdf: FORCE | build
	  TEXINPUTS=build: \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	main.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
