"""
Write a program that asks the user for a number n and gives them the possibility to choose between computing
the sum and computing the product of 1,…,n.
"""
num = int(input("Enter the Number:-  "))
sum = 0
sum1 = 1

for i in range(1, num + 1):
        sum = sum + i
        sum1 = sum1 * i

print("\n")
print(sum)
print(sum1)