.PHONY: slides

default: slides

slides:
	python build-slides.py code-slides/[012345679]*.py
