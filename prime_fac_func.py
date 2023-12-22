#!/usr/bin/python3

def prime_func(num):
    factors = []
    for i in range(2, int((num**0.5) + 1)):
        if num % i == 0:
            factors.extend([i, (num // i)])
    for j in range(len(factors) - 1):
        if factors[j] * factors[j + 1] == num:
            print(f"{num}={factors[j + 1]}*{factors[j]}")


