.PHONY: slides

default: slides

slides:
	python build-slides.py code-slides/*.py
