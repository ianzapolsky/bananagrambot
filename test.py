from itertools import chain, combinations

class Bananagrambot:


    def __init__(self, init_min_length):
        self.words = self.read_words('words.txt')
        self.min_length = init_min_length

    def find_words(self, letters):
        return filter(lambda word : sorted(word) == sorted(letters), self.words)

    def find_packings(self, words, letters):
        if len(letters) == 0:
            return True
        elif len(letters) < self.min_length:
            return False
        else:
            for p in self.powerset(letters):
                if self.find_packings(words, p)





    def powerset(self, iterable):
        s = list(iterable)
        return list(
            filter(lambda c : len(c) >= self.min_length,
                map(''.join,
                    chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))
                )
            )
        )

    # TODO: optimize by sorting all the words in the dictionary here
    def read_words(self, fname):
        with open(fname) as f:
            return f.read().splitlines()

if __name__ == '__main__':

    bb = Bananagrambot(3)

    words, leftover = bb.find_packings([], 'cat')

