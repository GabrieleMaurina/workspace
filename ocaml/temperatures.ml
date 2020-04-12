module Temperatures =
struct
	let c = 0
	let f = 1
	let k = 2

	let names = ["Celsius";"Fahrenheit";"Kelvin"]

	let cf x = x *. 9.0 /. 5.0 +. 32.0
	let ck x = x +. 273.15
	let fc x = x -. 32.0 *. 5.0 /. 9.0
	let fk x = x +. 459.67 *. 5.0 /. 9.0
	let kc x = x -. 273.15
	let kf x = x *. 9.0 /. 5.0 -. 459.67

	let id x = x

	let converters =[[id;cf;ck];
		[fc;id;fk];
		[kc;kf;id]]

	let convert x = List.map (fun l -> List.map (fun f -> f x) l) converters

	let convertScale x s = List.map (fun f -> f x) (List.nth converters s)
end
