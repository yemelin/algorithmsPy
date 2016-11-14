'''
Created on Nov 15, 2016

@author: vvy
'''
# used in every implementation, thus simplifies the code
def __base(n):
    return -1 if n<0 else n

# iterative version
def fib(n):
    if (n<2):
        return __base(n)
    prev2 = 0
    prev1 = 1
    s = 0
    while n>1:
        s = prev2 + prev1
        prev2 = prev1
        prev1 = s
        n-=1
    return s

# dumb recursion, calculates values multiple times    
def dumbFibRec(n):
    return __base(n) if (n<2) else dumbFibRec(n-1)+dumbFibRec(n-2)

# recursion without memoization     
def __recFibNoMemo (prev2, prev1, n):
    return __recFibNoMemo(prev1, prev1+prev2, n-1) if n>2 else prev1+prev2;
    
def recFibNoMemo (n):
    return __base(n) if n<2 else __recFibNoMemo(0,1,n);

# recursion with memoization    
memo = {}
def recFibMemo(n):
    ret = -1
    if n in memo:
        ret = memo[n]        
    else:
        ret = __base(n) if n<2 else recFibMemo(n-2)+recFibMemo(n-1);
        memo[n] = ret;
    return ret;
