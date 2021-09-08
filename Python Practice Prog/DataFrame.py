# Creating Data Frame with List and Dictionary
import pandas as pd
# Creating Data Frame with list.
L1 = [1, 2, 3, 4, 5, 6, 7]
data1 = pd.DataFrame(L1)
print(data1)
print("\n")

# Creating Data Frame with Dictionary.
Dt1 = {'fruit_name': ['Apple', 'Orange', 'Banana', 'Grapes', 'Mango'], 'Count': [10, 70, 45, 65, 99]}
data2 = pd.DataFrame(Dt1)
print(data2)
print("\n")

