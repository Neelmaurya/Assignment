# Factorial  of any number using python.
num = int(input("Enter a Number :  \n"))
result = 1
for i in range(num, 0, -1):
    print("Calling the Values :  ", i)
    result = result*i
print("Factorial of ", num, " is  ", result)