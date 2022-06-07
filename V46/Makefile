all: build/main.pdf

# hier Python-Skripte:
build/magn.pdf: data_scripts/scripts/magn.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/scripts/magn.py

build/probe.pdf: data_scripts/scripts/probe.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/scripts/probe.py

build/mass2.pdf: data_scripts/scripts/mass2.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/scripts/mass2.py

build/mass3.pdf: data_scripts/scripts/mass3.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/scripts/mass3.py

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: build/magn.pdf build/probe.pdf	build/mass2.pdf build/mass3.pdf

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
