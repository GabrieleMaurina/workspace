-module(client).
-export([start/0, loop/0, send/3]).

start() -> register(cli, spawn(client,loop,[])).

loop() -> receive
	{Pid, Node, Msg} ->
		io:format("~p   ###   ~p   ###   ~p~n", [Pid, Node, Msg])
	end, loop().

send(Pid, Node, Msg) -> {Pid, Node} ! {cli, node(), Msg}.
