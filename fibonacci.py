#!/usr/bin/env python3
# Fibonacci series
# By: lgarciaorozco6@gmail.com
# 11/10/23
# LICENSE: GNU/GPL
from math import sqrt

n = int(input())
fibo = [1,1]

if n > 1:
    for _ in range(n-2):
        fibo.append(fibo[-2]+fibo[-1])
    print(fibo)
elif n == 1:
    print(fibo[:1])
else: print(fibo)

# for i in range(len(fibo)-1):
    # print(fibo[i+1])

razones = [fibo[i+1]/fibo[i] for i in range(len(fibo)-1)]
print(sum(razones)/len(razones),(1+sqrt(5))/2)
    
