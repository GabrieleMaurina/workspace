#!/usr/bin/env bash
scp -r -oProxyCommand="ssh -q -W %h:%p cazzola@denver.cs.colostate.edu" cazzola@smith.cs.colostate.edu:/s/smith/b/nobackup/malref82/FLiRTS2/Testing/gabriele/$1 $2
