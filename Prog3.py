"""
Write a program that takes integer Array of N element and prints sum of even numbers and
sum of odd numbers within the Array.
"""

a = [2, 1, 4, 5, 3, 13, 11, 6]
b = len(a)
sum = 0
sum1 = 0

for i in range(0, b):
    if a[i] % 2 == 0:
        sum = sum + a[i]

    else:
        sum1 = sum1 + a[i]
print("Sum of even Number", sum)
print("Sum of odd Number", sum1)