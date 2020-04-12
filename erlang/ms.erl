-module(ms).
-export([start/1, to_slave/2, stop/0, master/1, slave/1]).

start(N) -> case whereis(master) of
	undefined -> register(master, spawn(ms, master, [N]));
	Pid -> io:format("Master already started with pid: ~p\n", [Pid])
	end.

to_slave(Msg, N) -> whereis(master) ! {Msg, N}.

stop() -> exit(whereis(master), stopped).

master(N) ->
	io:format("Master with pid: ~p, spawned\n", [self()]),
	process_flag(trap_exit, true),
	master_receive(slaves(N)).

master_receive(S) -> receive
	{Msg, N} -> lists:nth(N, S) ! {Msg}, master_receive(S);
	{'EXIT', Pid, Why} -> master_receive(respawn(Pid, S, [], 1))
	end.

respawn(Pid, [Pid|Tail], Head, N) ->
	New = spawn_link(ms, slave, [N]),
	io:format("Slave ~p, with pid ~p, died and was replaced by ~p.\n", [N, Pid, New]),
	lists:reverse([New|Head], Tail);
respawn(Pid, [E|Tail], Head, N) -> respawn(Pid, Tail, [E|Head], N+1).

slaves(N) when N > 0 -> [spawn_link(ms, slave, [N])|slaves(N-1)];
slaves(_) -> void.

slave(N) -> io:format("Slave ~p, with pid ~p, spawned\n", [N, self()]), slave_receive(N).

slave_receive(N) -> receive
	{die} -> io:format("Slave ~p, with pid ~p, was killed\n", [N, self()]), exit(killed);
	{Msg} -> io:format("Slave ~p, with pid ~p, received: ~p\n", [N, self(), Msg]), slave_receive(N)
	end.
