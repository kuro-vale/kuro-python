# https://www.codewars.com/kata/5c374b346a5d0f77af500a5a/python

def elevator(left, right, call):
    left_distance = abs(left - call)
    right_distance = abs(right - call)
    if left_distance < right_distance:
        return "left"
    else:
        return "right"
