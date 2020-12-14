def print_rhombus(size):
    for i in range(1, size + 1):
        print(' ' * (size - i) + '* ' * i)

    for i in range(size - 1, 0, -1):
        print(' ' * (size - i) + '* ' * i)


n = int(input())
print_rhombus(n)

# def create_row(n, i):
#     return ' ' * (n - i) + '* ' * i
#
#
# def print_rhombus(n):
#     for i in range(1, n + 1):
#         print(create_row(n, i))
#
#     for i in range(n - 1, 0, -1):
#         print(create_row(n, i))
