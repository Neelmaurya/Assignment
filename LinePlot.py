"""
Create Simple line plot, Where x and y axis range from 0-10. This is "Y vs X",
x-axis label is "x-axis" and "y-axis" level is "y-axis".
"""

import numpy as np
from matplotlib import pyplot as plt
x = np.arange(0, 10, 1)
print(x)
y = np.arange(0, 10, 1)
print(y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("X vs Y")
plt.plot(x, y)

# Run this code in Jupyter or Colab