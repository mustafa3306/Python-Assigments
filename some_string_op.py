""" this function aims to replace the first letter of the given word with the 
last letter"""


def front_back(word):
    if len(word) <= 1:
        return word
    else:
        return word[len(word)-1] + word[1:(len(word)-1)] + word[0]


front_back("a")

"""this function removes the specified letter"""


def missing_char(word, n):
    name = list(word)
    name.pop(n)
    return "".join(name)
