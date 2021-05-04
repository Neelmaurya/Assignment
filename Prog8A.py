"""
Write a program that prints the next 20 leap years, write 3 different programs each using For loop.
"""
year = int(input('enter Start year\n'))
Endyear = year + 80

print("\n==========================================\n")
for i in range(year, Endyear+1):
    if (i % 4) == 0:
        if (i % 100) == 0:
            if (i % 400) == 0:
                print(i, " is a leap year")

        else:
            print(i, " is a leap year")
