import re
from collections import Counter

class String2(str):
    def palindrome(self):
        s = re.sub('\W', '', self.lower())
        return s == s[::-1]
    def __sub__(self, s):
        if type(s) is not String2:
            raise ValueError('Parameter must be of type String2.')
        return re.sub('[' + ''.join(set(s)) + ']', '', self)
    def anagram(self, words):
        counters = [Counter(w) for w in words]
        self_counter = Counter(self)
        return len([c for c in counters if c == self_counter])

if __name__ == '__main__':
    print(String2('Do geese see God?').palindrome(), String2('Rise to vote, sir.').palindrome())
    print(String2('Walter Cazzola') - String2('abcwxyzaaabc'))
    try:
        print(String2('asdf') - 'as')
    except ValueError as e:
        print(e)
    print(String2('aab').anagram(['aba', 'abb', 'abc', 'aab', 'cbaa']))
