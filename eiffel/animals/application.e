note
	description: "animals application root class"
	date: "$Date$"
	revision: "$Revision$"

class
	APPLICATION

inherit

	ARGUMENTS

create
	make

feature {NONE} -- Initialization

	make
			-- Run application.
		local
			a: ANIMAL
			c: COW
			g: GRASS
			f: FOOD
		do
			create c
			create g.make (20)
			a := c
			f := g
			print (a.out + " is going to eat: " + f.out + "%N")
			c.eat (g)
			c.eat (g)
			c.eat (g)
		end

end
