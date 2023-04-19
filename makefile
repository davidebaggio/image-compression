all: install exe

install:
	python3 -m pip install opencv-python
	python3 -m pip install matplotlib
	python3 -m pip install numpy

exe:
	python3 -B ./DCTpy/src/main.py
