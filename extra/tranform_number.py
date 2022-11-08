# This program return the minimum count of moves to transform a number to 1
# For example:
# min_moves(4) returns 2: 4 -> 2 -> 1
# min_moves(15) returns 5: 15 -> 16 -> 8 -> 4 -> 2 -> 1
def min_moves(n):
    n = int(n)
    moves = 0
    while n != 1:
        if n % 2 == 0:
            moves += 1
            n /= 2
        elif (n - 1) / 2 % 2 == 0 or (n - 1) / 2 == 1:
            moves += 1
            n -= 1
        elif (n + 1) / 2 % 2 == 0 or (n + 1 / 2 == 1):
            moves += 1
            n += 1
    return moves


if __name__ == '__main__':
    print(min_moves(str(10 ** 309 - 1)))
