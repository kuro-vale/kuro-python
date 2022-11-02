# https://www.codewars.com/kata/5b853229cfde412a470000d0/python

def twice_as_old(dad_years_old, son_years_old):
    return abs(dad_years_old - son_years_old * 2)


if __name__ == '__main__':
    print(twice_as_old(36, 7))
