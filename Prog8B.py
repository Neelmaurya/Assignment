"""
Write a program that prints the next 20 leap years, write 3 different programs each using While loop.
"""
starting = int(input('Enter starting year: '))
ending = starting + 80
print ('Leap years between', starting, 'and', ending)
while starting <= ending:
    if starting % 4 == 0 and starting % 100 != 0:
       print (starting, " is a leap year")
    if starting % 100 == 0 and starting % 400 == 0:
       print (starting, " is a leap year")
    starting = starting + 1