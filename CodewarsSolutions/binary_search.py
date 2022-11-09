#  Write a function for binary searching x in a given sorted list
#  and return index of x in given list or return False

given_list = list(range(23, 1876523, 3))


def search(x, given_array):
    if len(given_array) == 0:
        return "Given array is empty."
    start = 0
    end = len(given_array) - 1
    while start <= end:
        mid_idx = (start + end) // 2
        if given_array[mid_idx] == x:
            return mid_idx
        else:
            if given_array[mid_idx] < x:
                start = mid_idx + 1
            elif given_array[mid_idx] > x:
                end = mid_idx - 1
    return False


print(search(56, given_list))
