# Get factor groups
# Example print(factor_groups(36))
# {(4, 9), (6, 6), (1, 36), (2, 18), (3, 12)}
def factor_groups(num):
    factor_groups = set()
    for i in range(1, num):
        if num % i == 0:
            tuple_ = (i,int(num/i))
            sorted_tuple = tuple(sorted(tuple_))
            factor_groups.add(sorted_tuple)
    return factor_groups
  
# Get factor tree
# example print(factor_tree(32))
# [2, 2, 2, 2, 2, 1]
import math
def factor_tree(num):
    tree_numbers = []
    tmp = 1
    for i in range(2, num + 1):
        if num % i == 0:
            tree_numbers.append(i)
            tmp = num // i
            break
    if math.prod(tree_numbers) == num:
        tree_numbers.append(1)
        return tree_numbers
    else:
        tree_numbers.extend(factor_tree(tmp))
        return tree_numbers