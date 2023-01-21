# This time the input is a sequence of course-ids that are formatted in the following way:
#
# name-yymm
# The return of the function shall first be sorted by yymm, then by the name (which varies in length).
from typing import List


def sort_me(courses: List[str]) -> List[str]:
    dates = [element.split("-")[1] for element in courses]
    dates_names_dct = {}
    for date in set(dates):
        dates_names_dct[date] = sorted([element.split("-")[0] for element in courses if date in element])

    lst_to_ret = []
    for date in sorted(list(dates_names_dct.keys())):
        for name in dates_names_dct[date]:
            lst_to_ret.append(name + "-" + date)

    return lst_to_ret


print(sort_me(["aeb-1305", "site-1305", "play-1215", "web-1304", "site-1304", "beb-1305"]))
