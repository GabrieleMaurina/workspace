note
	description: "Summary description for {GRASS}."
	author: ""
	date: "$Date$"
	revision: "$Revision$"

class
	GRASS

inherit

	FOOD
		redefine
			out
		end
create
	make
feature
	make(q:INTEGER)
		do
			weight := q
		end

	out: STRING
		do
			Result := "a bunch of grass (" + weight.out + "kg)"
		end

	consume (q: INTEGER)
		require
			enough: q < weight
		do
			weight := weight - q
		ensure
			correct: old weight = weight + q
			non_negative: weight >= 0
		end

	grow (q: INTEGER)
		do
			weight := weight + q
		end

	weight: INTEGER

end
