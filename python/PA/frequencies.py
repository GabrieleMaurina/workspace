import re
from collections import Counter

text = 'So do all who live to see such times. But that is not for them to decide. All we have to decide is what to do with the time that is given to us. There are other forces at work in this world Frodo, besides the will of evil. Bilbo was meant to find the Ring. In which case, you were also meant to have it. And that is an encouraging thought.'

def freq(s, min = 3):
	return [x for x in sorted(dict(Counter([w.lower() for w in re.split(r'[^\w]+', s) if w != ''])).items(), key=lambda x:x[1], reverse=True) if x[1] >= min]
	
if __name__ == '__main__':
	print(freq(text))