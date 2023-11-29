# This example is optimised for the PyCharm Environment

import numpy as np
import matplotlib.pyplot as plt

# Parallel Coordinates

# Initialise values
# Alternatively, read from CSV
City1 = np.array([15, 16, 18, 20, 22, 23, 28, 24, 21, 19, 17, 16], dtype='int')
City2 = np.array([5, 7, 9, 12, 15, 19, 24, 20, 19, 15, 11, 8], dtype='int')
City3 = np.array([4, 6, 8, 10, 11, 13, 14, 12, 10, 9, 7, 5], dtype='int')

# Print the values
print('\nCity 1: ', end=' ')
for i in range(0, 12):
    print(City1[i], end=' ')

print('\nCity 2: ', end=' ')
for i in range(0, 12):
    print(City2[i], end=' ')

print('\nCity 3: ', end=' ')
for i in range(0, 12):
    print(City3[i], end=' ')

# Spine names
Months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Spines
for i in range(0, 12):
    plt.vlines(i, 0, 50, '#808080')

# Display the multi-line on the plot
# name acts as X coordinates, array as Y coordinates
plt.plot(Months, City1, '#FF0000')
plt.plot(Months, City2, '#00FF00')
plt.plot(Months, City3, '#0000FF')

# Display city names with the corresponding colours
# Position each name next to the last temperature
plt.text(12, City1[11], 'City 1', color='#FF0000')
plt.text(12, City2[11], 'City 2', color='#00FF00')
plt.text(12, City3[11], 'City 3', color='#0000FF')

# Show the plot
plt.show()