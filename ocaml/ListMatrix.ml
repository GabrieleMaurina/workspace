module ListMatrix =
struct
	let zeroes m n =
		let rec build v = function
			0 -> []
			| 1 -> [v()]
			| n -> [v()] @ build v (n-1)
		in build (fun () -> build (fun () -> 0) n) m

	let identity n =
		let rec build s = 
			let rec build1 s1 = if s1 = 0 then [] else [if s = s1 then 1 else 0] @ (build1 (s1-1))
			in if s = 0 then [] else [build1 n] @ build (s-1)
		in build n

	let init n =
		let rec b = function
			0 -> []
			| s ->
				let rec b1 = function
					0 -> []
					| s1 -> [n * (n-s) + (n-s1) + 1] @ b1 (s1-1)
			 	in [b1 n] @ b (s-1)
		in b n

	let transpose = function
		[] -> []
		| l -> let s1 = List.length l
			in let s2 = List.length (List.hd l)
			in let rec b x acc =
				let rec b1 y acc1 = if y >= s1 then acc1 else b1 (y+1) (acc1 @ [List.nth (List.nth l y) x])
				in if x >= s2 then acc else b (x+1) (acc @ [b1 0 []])
			in b 0 []

	let ( * ) m1 m2 = false
end
