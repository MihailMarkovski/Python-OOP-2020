class vowels:
    def __init__(self, string):
        self.string = string
        self.vowels = 'AaEeOoYyUuIi'
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.string):
            raise StopIteration()
        current_idx = self.index
        self.index += 1
        if self.string[current_idx] in self.vowels:
            return self.string[current_idx]
        else:
            return self.__next__()


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
