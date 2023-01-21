# Have the function QuestionsMarks(str) take the str string parameter,
# which will contain single digit numbers, letters, and question marks,
# and check if there are exactly 3 question marks between every pair of two numbers that add up to 10.
# If so, then your program should return the string true, otherwise it should return the string false.
# If there aren't any two numbers that add up to 10 in the string, then your program should return false as well.
#
# For example: if str is "arrb6???4xxbl5???eee5" then your program should return true because
# there are exactly 3 question marks between 6 and 4, and 3 question marks between 5 and 5 at the end of the string.


def QuestionsMarks(strParam: str) -> bool:
    digits_idxs = [i for i, c in enumerate(strParam) if c.isdigit()]
    if len(digits_idxs) < 2:
        return False
    start = 0
    lst_start = []
    lst_stop = []
    for i in range(1, len(digits_idxs)):
        if int(strParam[digits_idxs[start]]) + int(strParam[digits_idxs[i]]) == 10:
            lst_start.append(digits_idxs[start])
            lst_stop.append(digits_idxs[i])
        start += 1
    if len(lst_start) < 1:
        return False
    for start, stop in zip(lst_start, lst_stop):
        if strParam[(start + 1) : stop].count("?") != 3:
            return False
    return True
