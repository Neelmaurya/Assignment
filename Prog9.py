# Write a function that returns the largest element in a list of Integers.
def lis( list ):
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max
print(lis([1, 2, -8, 0, 5, 4, 3]))