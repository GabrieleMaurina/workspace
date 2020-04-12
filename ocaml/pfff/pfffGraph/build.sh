#!/usr/bin/env bash

rm -f pfffGraph.exe
dune build pfffGraph.exe
mv _build/default/pfffGraph.exe ./
rm -rf _build .merlin
rm -f dune-project
