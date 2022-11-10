# https://www.codewars.com/kata/5a3fe3dde1ce0e8ed6000097/python

def century(year):
    return (year / 100).__ceil__()


if __name__ == '__main__':
    print(century(101))
