# Write an algorithm that takes an array and moves all the zeros to the end,
# preserving the order of the other elements.
#
# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
from typing import List


def move_zeros(array: List[int]) -> List[int]:
    zeros_count = array.count(0)
    array = [e for e in array if e != 0]
    array.extend([0 for _ in range(zeros_count)])
    return array
