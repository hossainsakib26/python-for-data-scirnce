# This program is optimised for the PyCharm environment

import numpy as np
import matplotlib.pyplot as plt

# This subroutine encapsulates the 'plot' method, as the most suitable for raster rendering
def DrawBox(x, y, size, r, g, b):
    if r < 0:
        r = int(0)
    if g < 0:
        g = int(0)
    if b < 0:
        b = int(0)
    if r > 255:
        r = int(255)
    if g > 255:
        g = int(255)
    if b > 255:
        b = int(255)
    for i in range(0, int(size)):
        plt.plot([x, x + size], [y + i, y + i], '#{:02x}{:02x}{:02x}'.format(r, g, b))


# Initialise the data
# Example works with positive temperatures
# Would require extra steps to include negative temperatures
City1 = np.array([15, 16, 18, 20, 22, 23, 28, 24, 21, 19, 17, 16], dtype='int')
City2 = np.array([5, 7, 9, 12, 15, 19, 24, 20, 19, 15, 11, 8], dtype='int')
City3 = np.array([4, 6, 8, 10, 11, 13, 14, 12, 10, 9, 7, 5], dtype='int')

# Set the plot
plt.axis([0, 600, 0, 400])
plt.xticks([])
plt.yticks([])

# Offsets for the labels
OffsetX = int(15)
OffsetY = int(12)

# Size of the squares
BoxSize = int(40)

# Find the minimum, maximum and the range
Min = int(min(np.min(City1), np.min(City2), np.min(City3)))
Max = int(max(np.max(City1), np.max(City2), np.max(City3)))
R = Max - Min

# Generate the heat map
# Starts from point 60, 140
# Calculate the colour code
# Draw the squares
# Add the text

for i in range(0, 12):
    ColourCode = int((City1[i]/R)*255)
    DrawBox(60+BoxSize*i, 140, BoxSize, ColourCode, 0, 0)
    plt.text(60+i*BoxSize+OffsetX, 140+OffsetY, str(City1[i]), color='white')

for i in range(0, 12):
    ColourCode = int((City2[i]/R)*255)
    DrawBox(60+BoxSize*i, 140-BoxSize, BoxSize, ColourCode, 0, 0)
    plt.text(60+i*BoxSize+OffsetX, 140-BoxSize+OffsetY, str(City2[i]), color='white')

for i in range(0, 12):
    ColourCode = int((City3[i]/R)*255)
    DrawBox(60+i*BoxSize, 140-2*BoxSize, BoxSize, ColourCode, 0, 0)
    plt.text(60+i*BoxSize+OffsetX, 140-2*BoxSize+OffsetY, str(City3[i]), color='white')

# Draw the colour code guide
for i in range(0, 256):
    plt.plot([560, 580], [i + 60, i + 60], '#{:02x}{:02x}{:02x}'.format(int(i), 0, 0))

# Display names of the months
plt.text(72, 20, 'Jan')
plt.text(112, 20, 'Feb')
plt.text(152, 20, 'Mar')
plt.text(192, 20, 'Apr')
plt.text(232, 20, 'May')
plt.text(272, 20, 'Jun')
plt.text(312, 20, 'Jul')
plt.text(352, 20, 'Aug')
plt.text(392, 20, 'Sep')
plt.text(432, 20, 'Oct')
plt.text(472, 20, 'Nov')
plt.text(512, 20, 'Dec')

# Names of the cities
plt.text(5, 155, 'City 1')
plt.text(5, 115, 'City 2')
plt.text(5, 75, 'City 3')

# Minimum and maximum temperatures
plt.text(585, 57, str(Min))
plt.text(585, 184, str(int(Min+R/2)))
plt.text(585, 312, str(Max))

plt.show()