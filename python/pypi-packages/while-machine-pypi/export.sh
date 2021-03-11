#!/usr/bin/env bash

mkdir while-machine
cp ~/workspace/while-machine/while_machine.py while-machine/
cp ~/workspace/while-machine/README.md while-machine/
cp setup.py while-machine/

cd while-machine
	python -m pip install --upgrade twine setuptools wheel --user
	python setup.py sdist bdist_wheel
	python -m twine upload dist/*
cd ..

rm -rf while-machine
