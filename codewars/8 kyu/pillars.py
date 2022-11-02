# https://www.codewars.com/kata/5bb0c58f484fcd170700063d/python

def pillars(num_pill, dist, width):
    result = 0
    dist *= 100
    for i in range(1, num_pill):
        result += dist
    for i in range(1, num_pill - 1):
        result += width
    return result


if __name__ == '__main__':
    print(pillars(11, 15, 30))
