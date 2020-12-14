class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.number == 0:
            raise StopIteration()
        if self.idx == len(self.sequence):
            self.idx = 0
        current_idx = self.idx
        self.idx += 1
        self.number -= 1
        return self.sequence[current_idx]


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
