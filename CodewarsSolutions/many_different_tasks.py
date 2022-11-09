# Write a function that prints all prime numbers in range 1-n


def print_prime(n):
    for num in range(1, n + 1):
        if all(num % i != 0 for i in range(2, num)):
            print(num)


# Write a sort function to sort numbers in list. Do not use built-in sort()


def my_sort(array):
    sorted_lst = []
    while array:
        lowest = min(array)
        sorted_lst.append(lowest)
        array.remove(lowest)
    return sorted_lst


# Write a function to print elements from Fibonacci series up to n-th element


def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a)
        a, b = b, a + b


# Write a function to print elements from list in reversed order


def reversed(array):
    while array:
        print(array[-1])
        del array[-1]


#  Write a function to check if word is a palindrome or not


def if_palindrome(word):
    return True if word.lower() == word[::-1].lower() else False


# Write a function to print set of duplicates in list


def duplicates(array):
    print(set([x for x in array if array.count(x) > 1]))


# Write a function to print number of words in given sentence


def count_words(sentence):
    print(len(sentence.split()))


# Write a function for binary searching x in a given sorted list and return index of x in given list or return False

given_list = list(range(500, 10000))


def search(x, given_array):
    if len(given_array) > 0:
        low_idx = 0
        up_idx = len(given_array) - 1

        while up_idx >= 0:

            mid_idx = (low_idx + up_idx) // 2
            if given_array[mid_idx] == x:
                return mid_idx
            else:
                if given_array[mid_idx] < x:
                    low_idx = mid_idx + 1
                elif given_array[mid_idx] > x:
                    up_idx = mid_idx - 1

        return False
    else:
        return "Given array is empty."
