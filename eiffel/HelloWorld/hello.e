note
	description: "HelloWorld application root class"
class
	HELLO

create
	make

feature {NONE} -- Initialization

	make
			-- Run application.
		do
			--| Add your code here
			print ("Hello Eiffel World!%N")
			my_feature(10)
		end


	my_feature (a: INTEGER)
		require
			grater_than: a > 5
		local
			exc: EXCEPTIONS
		do
			print ("my feature " + a.out + "%N")
			create exc
			exc.raise("HOLAAA")
		ensure
			less_than: a < 12
		end
end
