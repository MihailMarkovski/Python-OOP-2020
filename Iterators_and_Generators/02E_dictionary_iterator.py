class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx == len(self.dictionary):
            raise StopIteration()
        current_idx = self.idx
        self.idx += 1
        current_key = list(self.dictionary)[current_idx]
        return current_key, self.dictionary[current_key]


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
