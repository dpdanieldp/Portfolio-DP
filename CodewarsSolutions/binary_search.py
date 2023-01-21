# Write a function for binary searching x in a given sorted list
# and return index of x in given list or return False

from typing import List, Union


def search(x: int, lst: List[int]) -> Union[bool, int]:
    start = 0
    end = len(lst) - 1
    while start <= end:
        mid_idx = (start + end) // 2
        if lst[mid_idx] == x:
            return mid_idx
        if lst[mid_idx] < x:
            start = mid_idx + 1
        elif lst[mid_idx] > x:
            end = mid_idx - 1
    return False


if __name__ == "__main__":
    given_lst = list(range(23, 1876523, 3))
    print(search(56, given_lst))
