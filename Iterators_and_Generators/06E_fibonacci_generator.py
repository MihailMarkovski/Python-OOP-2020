def fibonacci():
    n1 = 0
    n2 = 1
    while True:
        yield n1
        n3 = n1 + n2
        n1 = n2
        n2 = n3


generator = fibonacci()
for i in range(100):
    print(next(generator))
