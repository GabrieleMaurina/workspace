-module(count).
-export([d1/0, d2/0, d3/0, tot/0, start/0, server/1]).

start() ->
	case whereis(server) of
		undefined ->
			register(interface, self()),
			register(server, spawn(count, server, [dict:new()])),
			io:format("Server started: ~p\n", [whereis(server)]);
		Pid -> io:format("Server already started: ~p\n", [Pid])
	end.

send(S) -> whereis(server) ! {S},
	io:format("Service requested: ~p\n", [S]),
	receive {Res} -> io:format("Server response: ~p\n", [Res]) end.

d1() -> send(d1).
d2() -> send(d2).
d3() -> send(d3).
tot() -> send(tot).

server(Count) ->
	receive
		{tot} ->
			whereis(interface) ! {dict:to_list(Count)},
			server(dict:update_counter(tot, 1, Count));
		{S} ->
			whereis(interface) ! {S},
			server(dict:update_counter(S, 1, Count))
	end.
