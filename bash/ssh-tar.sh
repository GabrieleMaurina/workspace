#!/usr/bin/env bash

ssh -J cazzola@denver.cs.colostate.edu cazzola@smith.cs.colostate.edu "tar czf - /s/smith/b/nobackup/malref82/FLiRTS2/Testing/gabriele/$1" | tar xvzf - -C $2
