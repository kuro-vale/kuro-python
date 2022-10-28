# https://www.codewars.com/kata/5f9f43328a6bff002fa29eb8/python

import math


def approx_equals(a, b):
    return math.isclose(a, b, abs_tol=0.001)
