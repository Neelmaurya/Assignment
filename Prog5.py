# Write a program that prints a multiplication table for numbers up to 12.
num = int(input("Enter the number: "))

for j in range(1, num+1):
    print("Table of is ", j,)
    print("******************************************")
    for i in range(1, 11):
        print('{1}  *  {0}  =  {2}'.format(i, j, j*i))
    print("==========================================\n")