# This time we want to write calculations using functions and get the results. Let's have a look at some examples:
#
# seven(times(five())) # must return 35
# four(plus(nine())) # must return 13
# eight(minus(three())) # must return 5
# six(divided_by(two())) # must return 3
# Requirements:
#
# There must be a function for each number from 0 ("zero") to 9 ("nine")
# There must be a function for each of the following mathematical operations:
#  plus, minus, times, dividedBy (divided_by in Ruby and Python)
# Each calculation consist of exactly one operation and two numbers
# The most outer function represents the left operand, the most inner function represents the right operand
# Division should be integer division. For example, this should return 2, not 2.666666...:
# eight(divided_by(three()))


# Using eval() is intentional since for this task I can trust input data


def zero(operation=None):
    if operation is None:
        return "0"
    return eval("0" + operation["op"] + operation["num"])


def one(operation=None):
    if operation is None:
        return "1"
    return eval("1" + operation["op"] + operation["num"])


def two(operation=None):
    if operation is None:
        return "2"
    return eval("2" + operation["op"] + operation["num"])


def three(operation=None):
    if operation is None:
        return "3"
    return eval("3" + operation["op"] + operation["num"])


def four(operation=None):
    if operation is None:
        return "4"
    return eval("4" + operation["op"] + operation["num"])


def five(operation=None):
    if operation is None:
        return "5"
    return eval("5" + operation["op"] + operation["num"])


def six(operation=None):
    if operation is None:
        return "6"
    return eval("6" + operation["op"] + operation["num"])


def seven(operation=None):
    if operation is None:
        return "7"
    return eval("7" + operation["op"] + operation["num"])


def eight(operation=None):
    if operation is None:
        return "8"
    return eval("8" + operation["op"] + operation["num"])


def nine(operation=None):
    if operation is None:
        return "9"
    return eval("9" + operation["op"] + operation["num"])


def plus(number):
    return {"op": "+", "num": number}


def minus(number):
    return {"op": "-", "num": number}


def times(number):
    return {"op": "*", "num": number}


def divided_by(number):
    return {"op": "//", "num": number}
