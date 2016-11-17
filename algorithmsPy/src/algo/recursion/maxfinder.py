'''
Created on Nov 18, 2016

@author: vvy
'''
def find_max(int_list):
    ret = int_list.pop() #raises exception
    if len(int_list)>0:
        ret = max(ret, find_max(int_list))
    return ret

print find_max([1,2,5,3,3,5,0])
    