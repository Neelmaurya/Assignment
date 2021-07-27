# Write a python program which will keep adding a stream of number inputted by the user.
# The adding stop as soon as user presses q key on the keyboard.

sum = 0
while(True):
    UserInput = input("Enter Number to add:-  \n")
    if (UserInput != 'q'):
        sum = sum + int(UserInput)
        print(f"Total is :-   {sum}")
    else:
        print(f"Total of all numbers entered by You:-   {sum}")
        break