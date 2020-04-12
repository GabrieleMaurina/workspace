let sin x n =
	let rec fact n = if n <= 1 then 1 else n * fact (n-1)
	in
	let rec sin_rec c = if c >= n then 0.0 else x**float(2*c+1) /. float(fact(2*c+1)) -. sin_rec (c+1)
	in sin_rec 0;;
print_endline(string_of_float(sin (3.14 /. 3.0) 8));;
