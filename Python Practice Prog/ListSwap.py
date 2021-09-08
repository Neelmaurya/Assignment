# Swap 1 and last Digit
def swapList(newList):
    size = len(newList)

    # Swapping
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp
    return newList
newList = [10, 11, 12, 15, 18, 22, 25, 45]
print(swapList(newList))
