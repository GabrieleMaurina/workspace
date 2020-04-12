-module(controller).
-export([start/1, sieve/1]).

start(N) ->
  init(),
  register(first, spawn(controller, sieve, [primes(N)])),
  server_loop().

server_loop() ->
  receive
    {new, N} -> io:format("You asked for: ~p~n", [N]), first ! {new, N}, server_loop();
    {res, R} -> {client, 'amora@gabriele-Dell-System-XPS-L702X'} ! {result, R}, server_loop();
    {quit} -> io:format("I'm closing ...~n"), exit(whereis(first), kill), ok
  end.

sieve([]) -> ok;
sieve([P]) -> sieve_loop(P, first);
sieve([P|Ps]) -> sieve_loop(P, spawn_link(controller, sieve, [Ps])).

sieve_loop(P, Next) ->
  receive
    {new, N} ->
      case N == P of
        true -> server ! {res,{N, true}};
        false ->
          case N rem P of
            0 -> server ! {res,{N, false}};
            _ -> Next ! {pass, N}
          end
          end;
    {res, R} -> server ! {res, R};
    {pass, N} ->
      case whereis(first) == self() of
        true -> server ! {res, {N, true}};
        false ->
          case Next == first andalso N > P * P of
            true -> first ! {res, {N, error}};
            false ->
              case P > N of
                true -> first ! {res, {N, true}};
                false ->
                  case N == P of
                    true -> first ! {res, {N, true}};
                    false ->
                      case N rem P of
                        0 -> first ! {res, {N, false}};
                        _ -> Next ! {pass, N}
                      end
                  end
              end
          end
      end
  end, sieve_loop(P, Next).

primes(N) -> lists:reverse(primes(N, 2, [])).

primes(N, T, Ps) when T > N -> Ps;
primes(N, T, Ps) ->
  case lists:any(fun(P) -> T rem P == 0 end, Ps) of
    true -> primes(N, T+1, Ps);
    false -> primes(N, T+1, [T|Ps])
  end.

init() ->
  case whereis(server) of
    undefined -> erlang:set_cookie(node(), sieves),
		register(server, self());
    _ -> ok
  end.
