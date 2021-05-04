# Modify the previous program such that only multiples of 3 or 5 are considered in the sum.
num = int(input("Enter the Number "))
sum = 0

for i in range(1, num + 1):
    if( i % 3 == 0 or i % 5 == 0 ):
        sum = sum + i
        print(i, "+", end=" ")
print("\n")
print(sum)