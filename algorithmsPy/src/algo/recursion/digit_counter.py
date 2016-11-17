'''
Created on Nov 18, 2016

@author: vvy
'''
from __builtin__ import int

def __count_digits(n):
    if n<10:
        return 1
    else:
        return 1+count_digits(n/10)
        
def count_digits(n):
    if isinstance(n, int):
        return __count_digits(n)
    else:
        return -1