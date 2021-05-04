# Write a program that prints all prime numbers up to a given number N.
num = int(input("Enter range: "))
print("Prime numbers are :-")
for n in range(1, num):
    for i in range(2, n):
        if(n % i == 0):
            break
    else:
        print(n, end=' ')