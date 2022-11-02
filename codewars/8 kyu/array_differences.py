# https://www.codewars.com/kata/5b73fe9fb3d9776fbf00009e/python

def sum_of_differences(arr):
    return max(arr) - min(arr) if arr else 0


if __name__ == '__main__':
    print(sum_of_differences([1, 2, 10]))
