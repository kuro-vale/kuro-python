# https://www.codewars.com/kata/5ae62fcf252e66d44d00008e/python

def expression_matter(a, b, c):
    return max([a * b * c,
                a + b + c,
                (a + b) * c,
                a * (b + c)
                ])


if __name__ == '__main__':
    print(expression_matter(5, 3, 1))
