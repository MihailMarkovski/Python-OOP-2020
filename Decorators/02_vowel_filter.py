def vowel_filter(function):
    def wrapper():
        result = function()
        vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
        return [l for l in result if l in vowels]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
