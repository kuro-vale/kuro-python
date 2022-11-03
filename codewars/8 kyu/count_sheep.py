# https://www.codewars.com/kata/5b077ebdaf15be5c7f000077/python

def count_sheep(n):
    sheep = ""
    for i in range(1, n + 1):
        sheep += f"{i} sheep..."
    return sheep


if __name__ == '__main__':
    print(count_sheep(2))
