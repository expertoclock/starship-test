# Starship Test

Test repository for [Starship](https://starship.rs/) prompt configuration.

## Stack
- Python 3.12+
- Node.js (tooling)
- Docker (deployment)

## Setup
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m src.main

## Test
pip install -r requirements-dev.txt && pytest tests/ -v
