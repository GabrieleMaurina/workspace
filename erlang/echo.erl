-module(echo).
-export([start/0, print/1, stop/0, server/1]).

start() ->
	case whereis(server) of
		undefined ->
			Server = spawn(echo, server, [self()]),
			register(server, Server),
			io:format("Server started: ~p\n", [Server]);
		Pid -> io:format("Server already running: ~p\n", [Pid])
	end.

print(Msg) ->
	whereis(server) ! {msg, Msg},
	io:format("Msg sent: ~p\n", [Msg]),
	receive {msg, Res} -> io:format("Msg received: ~p\n", [Res]) end.

stop () ->
	whereis(server) ! {stop},
	io:format("Server asked to stop\n", []),
	receive {stop, Res} -> io:format("~p\n", [Res]) end.

server(Pid) ->
	receive
		{msg, Msg} -> Pid ! {msg, Msg}, server(Pid);
		{stop} -> Pid ! {stop, "Server stopped"}, exit("Stopped")
	end.
