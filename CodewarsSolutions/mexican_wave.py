# Task
# In this simple Kata your task is to create a function that turns a string into a Mexican Wave.
# You will be passed a string and you must return that string in an array
# where an uppercase letter is a person standing up.
# Rules
#  1.  The input string will always be lower case but maybe empty.
#
#  2.  If the character in the string is whitespace then pass over it as if it was an empty seat
# Example
# wave("hello") => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
from typing import List


def wave(people: str) -> List[str]:
    str_list = list(people)
    idxs_without_spaces = [i for i, c in enumerate(people) if not c.isspace()]
    wave_lst = []
    for i in idxs_without_spaces:
        wave = str_list.copy()
        wave[i] = wave[i].upper()
        wave_lst.append("".join(wave))
    return wave_lst
