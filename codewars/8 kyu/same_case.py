# https://www.codewars.com/kata/5dd462a573ee6d0014ce715b/python

def same_case(a, b): 
    if (a.isupper() and b.isupper()) or (a.islower() and b.islower()):
        return 1
    elif not a.isalpha() or not b.isalpha():
        return -1
    else: 
        return 0
