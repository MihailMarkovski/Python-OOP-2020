class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx == self.count:
            raise StopIteration()
        current_num = self.step * self.idx
        self.idx += 1
        return current_num


numbers = take_skip(10, 5)
for number in numbers:
    print(number)


numbers = take_skip(2, 6)
for number in numbers:
    print(number)
