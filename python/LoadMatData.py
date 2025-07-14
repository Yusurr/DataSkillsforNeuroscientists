import matplotlib.pyplot as plt
import sys

# Package for importing MATLAB mat v7.3 files
import mat73



def load_mat_file(mat_file):
    """
    Load a MATLAB .mat file using mat73.
    
    Parameters:
    mat_file (str): Path to the .mat file.
    
    Returns:
    dict: Dictionary containing the loaded data.
    """
    print(f"Loading data from: {mat_file}")
    return mat73.loadmat(mat_file)


if __name__ == "__main__":

    mat_file = "../data/FL90__180316_15_20_48.mat"
    # Load the .mat file
    mat = load_mat_file(mat_file)


    # Print the keys to see what is inside
    print("Variables in the .mat file:", mat.keys())

    data = mat["allData"]["neurons"]["f"].T
    print(f"Neuron data (shape: {data.shape}): {data}")


    # If the data is 2D, plot as image; if 1D, as a line
    if data.ndim == 1:
        plt.plot(data)
        plt.xlabel("Index")
        plt.ylabel("Value")
    elif data.ndim == 2:
        plt.imshow(data, aspect="auto", cmap="viridis")
        plt.colorbar()
        plt.xlabel("Column")
        plt.ylabel("Row")

    plt.title("Plot from .mat file")

    plt.figure()
    for ca in data:
        plt.plot(ca)

    if "-nogui" not in sys.argv:
        plt.show()
