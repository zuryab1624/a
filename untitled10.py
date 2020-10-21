# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 22:54:35 2020

@author: Ahtazaz
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 22:40:25 2020

@author: Ahtazaz
"""

import math
ara=[]
seq = []
v=[]
N = int(input("please enter value of N "))   
n = int((-1+math.sqrt((1+8*N)))/2.0)
d=int(N-n*(n+1)/2)
for i in range(1,n):
    ara.append(i)
ara.append(n+d) 
print(ara)
def aa(ara):
    
    for i in ara:
        if type(math.sqrt(i))==int:
            v.append(i)
        return v
lss = aa(ara)
seq=list(map(lambda x: x*x, lss))
print(seq) 
print(lss)
