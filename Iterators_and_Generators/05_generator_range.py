def genrange(start, end):
    return (x for x in range(start, end + 1))
    # for x in range(start, end + 1):
    #     yield x


print(list(genrange(1, 10)))
