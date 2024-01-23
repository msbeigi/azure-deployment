install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv test_*.py

format:
	black *.py

run:
	python *.py

lint:
	pylint --disable=R,C,E1120,W3101 *.py

all: install test lint format