let fibo n =
	let rec fibo_fast c f s = if c = n then f else fibo_fast (c+1) (f+s) f
	in fibo_fast 0 1 1;;
print_endline(string_of_int(fibo(read_int())));;
