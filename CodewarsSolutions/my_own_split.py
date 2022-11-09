# Quite recently it happened to me to join some recruitment interview,
# where my first task was to write own implementation of built-in split function. It's quite simple, is it not?
# However, there were the following conditions:
#
# the function cannot use, in any way, the original split or rsplit functions,
# the new function must be a generator,
# it should behave as the built-in split, so it will be tested that way -- think of split() and split('')
# This Kata will control if the new function is a generator and if it's not using the built-in split method,
# so you may try to hack it, but let me know if with success, or if something would go wrong!


import re


def my_very_own_split(string, delimiter=None):
    if delimiter == "":
        raise ValueError
    if string == "":
        string = " "
        delimiter = " "
    if delimiter is None:
        delimiter = " "
        string = re.sub(r"\s+", " ", string)
    if string[-len(delimiter)] != delimiter:
        string += delimiter
    while string:
        word = string[: string.index(delimiter)]
        yield word
        string = string.replace(word + delimiter, "", 1)
