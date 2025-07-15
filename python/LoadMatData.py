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

    mat = mat73.loadmat(mat_file)
    # Print the keys to see what is inside
    print("Variables in the .mat file:", mat.keys())

    neuron_df_f_data = mat["allData"]["neurons"]["f"].T
    print(f"Neuron data (shape: {neuron_df_f_data.shape}): {neuron_df_f_data}")

    return neuron_df_f_data


if __name__ == "__main__":

    mat_file = "../data/FL90__180316_15_20_48.mat"
    # Load the .mat file

    neuron_df_f_data = load_mat_file(mat_file)

    plt.imshow(neuron_df_f_data, aspect="auto", cmap="viridis")
    plt.colorbar()
    plt.xlabel("Time")
    plt.ylabel("Neuron #")

    plt.title("Plot from .mat file")

    plt.figure()

    plt.xlabel("Time")
    plt.ylabel("dF/F")

    for ca in neuron_df_f_data:
        plt.plot(ca)

    if "-nogui" not in sys.argv:
        plt.show()
