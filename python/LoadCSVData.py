"""

A simple python script to load data from a CSV file and plot it using matplotlib.

Note: the CSV file contains a subset of the data exported from the MATLAB .mat file used in the other scripts.

"""

import numpy as np
import matplotlib.pyplot as plt
import sys


filename = "../data/example_data.csv"

# Load the CSV file into a numpy array
# Assumes numerical data and no header row
data = np.loadtxt(filename, delimiter=",")

print(f"Loaded data from: {filename}")

print(f"Data has shape: {data.shape} and type: {data.dtype}")

# Plot

plt.imshow(data.T, aspect="auto", cmap="viridis")
plt.colorbar()
plt.xlabel("Column")
plt.ylabel("Row")


plt.title("Plot from CSV file")

if "-nogui" not in sys.argv:
    plt.show()
