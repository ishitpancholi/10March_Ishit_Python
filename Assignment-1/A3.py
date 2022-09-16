#Write a Python program to sum of three given integers.


def sum_three(x, y, z):
    if x == y or y == z or x==z:
        sum = 0
    else:
        sum = x + y + z
    return sum
print(sum_three(3, 1, 2))
print(sum_three(4, 2, 2))
print(sum_three(5, 2, 2))
print(sum_three(6, 2, 3))
