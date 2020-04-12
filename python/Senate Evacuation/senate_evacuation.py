from string import ascii_uppercase as ALPHABET

T = int(input())

for i in range(T):
	N = int(input())
	P = sorted([[int(x), y]for x, y in zip(input().split(), ALPHABET)], reverse=True)
	plan = []
	
	def extract_one():
		global P
		if len(P):
			first = P[0][1]
			P[0][0] -= 1
			if P[0][0] == 0:
				del P[0]
			P = sorted(P, reverse=True)
			return first
		return ''
	
	while len(P): plan.append(extract_one() + extract_one())
	print('Case #{}: {}'.format(i + 1, ' '.join(plan)))