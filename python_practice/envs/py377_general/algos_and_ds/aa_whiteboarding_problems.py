# Day 1
def digital_root(num):
    import math

    sum = 0
    while num > 10:
        digit = num % 10
        remainder = math.ceil(num / 10)