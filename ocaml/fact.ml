let rec fact n = if n <= 1 then 1 else n * fact(n-1);;
let main() = print_endline("fact(10)="^string_of_int(fact 10));;
main();;
