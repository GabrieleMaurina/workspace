#!/usr/bin/env bash

rm -f graph.exe
dune build graph.exe
mv _build/default/graph.exe ./
rm -rf _build .merlin
rm -f dune-project
