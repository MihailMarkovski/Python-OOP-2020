class Calculator:
    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        result = 1
        for n in args:
            result *= n
        return result

    @staticmethod
    def divide(*args):
        result = args[0]
        for n in args[1:]:
            result /= n
        return result

    @staticmethod
    def subtract(*args):
        result = args[0]
        for n in args[1:]:
            result -= n
        return result
