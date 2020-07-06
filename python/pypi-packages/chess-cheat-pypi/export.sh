#!/usr/bin/env bash

mkdir chess-cheat
cp -r ~/workspace/chess-cheat/src/* chess-cheat
rm -rf chess-cheat/**/__pycache__
cp ~/workspace/chess-cheat/README.md chess-cheat
cp ~/workspace/chess-cheat/model/model.pb chess-cheat/chess_cheat_utils
cp setup.py MANIFEST.in chess-cheat

cd chess-cheat
	python -m pip install --upgrade twine setuptools wheel --user
	python setup.py sdist bdist_wheel
	python -m twine upload dist/*
cd ..

rm -rf chess-cheat
