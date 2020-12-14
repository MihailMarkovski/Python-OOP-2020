def cache(func):
    log = {}

    def wrapper(n):
        if n not in log:
            res = func(n)
            log[n] = res
            return res
        return log[n]

    wrapper.log = log
    return wrapper


# def cache(func): NOT WORKING AS EXPECTED
#     def wrapper(n):
#         value = func(n)
#         wrapper.log[n] = value
#         return value
#
#     wrapper.log = {}
#     return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(2)
print(fibonacci.log)
fibonacci(4)
print(fibonacci.log)
