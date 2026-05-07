PYTHON ?= python3
VENV_DIR := .venv
VENV_PYTHON := $(VENV_DIR)/bin/python
PIP := $(VENV_PYTHON) -m pip
SCRIPT := iptu - Copia.py

DEPS := selenium openpyxl

.PHONY: help venv install run setup clean

help:
	@echo "Targets disponiveis:"
	@echo "  make setup    - cria a venv e instala dependencias"
	@echo "  make run      - executa o sistema"
	@echo "  make install  - instala/atualiza dependencias"
	@echo "  make clean    - remove a venv"

venv:
	@if [ ! -d "$(VENV_DIR)" ]; then \
		$(PYTHON) -m venv "$(VENV_DIR)"; \
	fi

install: venv
	@$(PIP) install --upgrade pip
	@$(PIP) install $(DEPS)

setup: install

run: install
	@"$(VENV_PYTHON)" "$(SCRIPT)"

clean:
	@rm -rf "$(VENV_DIR)"