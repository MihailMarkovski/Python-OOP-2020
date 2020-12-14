def squares(n):
    return (x ** 2 for x in range(1, n + 1))
    # for num in range(1, n + 1):
    #     yield num ** 2


print(list(squares(5)))
