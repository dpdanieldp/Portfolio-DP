# Write a function, which takes a non-negative integer (seconds) as input
# and returns the time in a human-readable format (HH:MM:SS)
#
# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)


def make_readable(seconds):
    hours_ret = seconds // 3600
    minutes_ret = (seconds - hours_ret * 3600) // 60
    seconds_ret = seconds - hours_ret * 3600 - minutes_ret * 60

    list_str = [str(hours_ret), str(minutes_ret), str(seconds_ret)]

    for i in range(3):
        if len(list_str[i]) == 1:
            list_str[i] = "0" + list_str[i]

    return f"{list_str[0]}:{list_str[1]}:{list_str[2]}"
