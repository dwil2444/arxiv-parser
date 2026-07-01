ROOT_DIR := $(shell pwd)
HOSTNAME := $(shell hostname)

PYTHON ?= $(shell test -x .venv/bin/python && echo .venv/bin/python || which python)
PIP := $(PYTHON) -m pip

CAT ?= cs
KEYWORDS ?= keywords.txt
TIMEOUT ?= 30

.PHONY: help install parse parse-keywords

help:
	@echo "Available commands:"
	@echo "  make install"
	@echo "  make parse KEYWORD=saliency CAT=cs TIMEOUT=30"
	@echo "  make parse-keywords KEYWORDS=keywords.txt CAT=cs TIMEOUT=30"

install:
	$(PIP) install -r requirements.txt

parse:
	@test -n "$(KEYWORD)" || (echo "KEYWORD is required. Example: make parse KEYWORD=saliency CAT=cs"; exit 1)
	$(PYTHON) main.py --keyword="$(KEYWORD)" --cat="$(CAT)" --timeout="$(TIMEOUT)"

parse-keywords:
	$(PYTHON) main.py --keywords="$(KEYWORDS)" --cat="$(CAT)" --timeout="$(TIMEOUT)"
