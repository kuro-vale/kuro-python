# https://www.codewars.com/kata/5f70c883e10f9e0001c89673/python

def flip(d, a):
    if d == 'L':
        a.sort(reverse=True)
        return a
    elif d == 'R':
        a.sort()
        return a
    else:
        return "Please enter a valid direction ('L' or 'R')"
