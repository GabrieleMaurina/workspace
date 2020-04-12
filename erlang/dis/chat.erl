-module(chat).
-export([start/0,send/2,loop/0]).

start() -> register(c, spawn(chat, loop, [])).

send(Node, Msg) -> {c, Node} ! {node(), Msg}, ok.

loop() -> receive {Node, Msg} -> io:format("~p     #####     ~p~n", [Node, Msg]) end, loop().
