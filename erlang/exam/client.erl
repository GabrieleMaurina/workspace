-module(client).
-export([is_prime/1, close/0]).

is_prime(N) ->
  init(),
  send({new, N}),
  receive
    {result, {N, error}} -> io:format("~p is uncheckable, too big value.~n", [N]);
    {result, {N, B}} -> io:format("is ~p prime? ~p~n",[N, B])
  end.

close() ->
  init(),
  send({quit}),
  io:format("The service is closed!!!~n").

send(Data) -> {server, 'sif@gabriele-Dell-System-XPS-L702X'} ! Data.

init() -> case whereis(client) of
      undefined -> set_cookie(), reg();
      _ -> ok end.

set_cookie() -> erlang:set_cookie(node(),sieves).

reg() -> register(client, self()).
