all: build/main.pdf

# hier Python-Skripte:
build/hangle.pdf: data_scripts/scripts/hangle.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/scripts/hangle.py

build/hvarangle27.pdf: data_scripts/scripts/hvarangle27.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/scripts/hvarangle27.py

build/hvarangle37.pdf: data_scripts/scripts/hvarangle37.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/scripts/hvarangle37.py

build/hvarangle74.pdf: data_scripts/scripts/hvarangle74.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/scripts/hvarangle74.py

build/hvarangle86.pdf: data_scripts/scripts/hvarangle86.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/scripts/hvarangle86.py

build/h3ring.pdf: data_scripts/scripts/h3ring.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/scripts/h3ring.py

build/h6ring.pdf: data_scripts/scripts/h6ring.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/scripts/h6ring.py

build/h9ring.pdf: data_scripts/scripts/h9ring.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/scripts/h9ring.py

build/h2dia.pdf: data_scripts/scripts/h2dia.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/scripts/h2dia.py

build/h2varangle.pdf: data_scripts/scripts/h2varangle.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/scripts/h2varangle.py

build/2c1b.pdf: data_scripts/scripts/2c1b.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/scripts/2c1b.py

build/10c9b.pdf: data_scripts/scripts/10c9b.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/scripts/10c9b.py

build/2c1b10.pdf: data_scripts/scripts/2c1b10.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/scripts/2c1b10.py

build/2c1b16.pdf: data_scripts/scripts/2c1b16.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/scripts/2c1b16.py

build/10c9b10.pdf: data_scripts/scripts/10c9b10.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/scripts/10c9b10.py

build/10c9b16.pdf: data_scripts/scripts/10c9b16.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/scripts/10c9b16.py

build/10c9b75.pdf: data_scripts/scripts/10c9b75.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/scripts/10c9b75.py

build/10c9b375.pdf: data_scripts/scripts/10c9b375.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/scripts/10c9b375.py

build/10c9b625.pdf: data_scripts/scripts/10c9b625.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/scripts/10c9b625.py

build/5075.pdf: data_scripts/scripts/5075.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/scripts/5075.py

build/50single.pdf: data_scripts/scripts/50single.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/scripts/50single.py

build/75single.pdf: data_scripts/scripts/75single.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/scripts/75single.py

build/1316.pdf: data_scripts/scripts/1316.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/scripts/1316.py

build/h3ring2.pdf: data_scripts/scripts/h3ring2.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/scripts/h3ring2.py

build/h210.pdf: data_scripts/scripts/h210.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/scripts/h210.py

build/h216.pdf: data_scripts/scripts/h216.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/scripts/h216.py

build/h2plot.pdf: data_scripts/scripts/h2plot.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python data_scripts/scripts/h2plot.py


# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: build/hangle.pdf build/hvarangle27.pdf build/hvarangle37.pdf build/h2plot.pdf build/hvarangle74.pdf build/hvarangle86.pdf build/h3ring.pdf build/h3ring2.pdf build/h6ring.pdf build/h9ring.pdf build/h2dia.pdf build/h2varangle.pdf build/2c1b.pdf build/10c9b.pdf build/2c1b10.pdf build/2c1b16.pdf build/10c9b10.pdf build/10c9b16.pdf build/10c9b75.pdf build/10c9b375.pdf build/10c9b625.pdf build/5075.pdf build/50single.pdf build/75single.pdf build/1316.pdf build/h210.pdf build/h216.pdf
   
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