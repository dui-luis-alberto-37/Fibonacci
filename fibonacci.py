#!/usr/bin/env python3
# Fibonacci series
# By: lgarciaorozco6@gmail.com
# 11/10/23
# LICENSE: GNU/GPL

n = int(input())
fibo = [0,1]
if n > 1:
    for _ in range(n-1):
        fibo.append(fibo[-2]+fibo[-1])
    # print(fibo[-1])
# else:
    # print(fibo[n])

for i in range(len(fibo)-1):
    print(fibo[i+1])

