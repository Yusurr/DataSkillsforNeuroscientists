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

    neuron_df_f = mat["allData"]["neurons"]["f"].T
    print(f"Neuron data (shape: {neuron_df_f.shape}): {neuron_df_f}")

    neuron_times = mat["allData"]["neurons"]["time"].T
    print(f"Neuron times data (shape: {neuron_times.shape}): {neuron_times}")

    speed = mat["allData"]["behaviour"]["speed"].T
    print(f"Speed data (shape: {speed.shape}): {speed}")

    whisker_motion_index = mat["allData"]["behaviour"]["whiskerMI"].T
    print(
        f"Whisker motion index data (shape: {whisker_motion_index.shape}): {whisker_motion_index}"
    )

    state = mat["allData"]["behaviour"]["state"].T
    print(f"State data (shape: {state.shape}): {state}")

    return neuron_df_f, neuron_times, speed, whisker_motion_index, state


if __name__ == "__main__":
    mat_file = "../data/FL90__180316_15_20_48.mat"
    # Load the .mat file

    neuron_df_f_data, neuron_times, speed, whisker_motion_index, state = load_mat_file(
        mat_file
    )

    plt.imshow(neuron_df_f_data, aspect="auto", cmap="viridis")
    plt.colorbar()
    plt.xlabel("Time point")
    plt.ylabel("Neuron #")

    plt.title("Plot from .mat file")

    plt.figure()

    plt.xlabel("Time (s)")
    plt.ylabel("dF/F")

    for index in range(len(neuron_df_f_data)):
        plt.plot([t / 1000 for t in neuron_times[index]], neuron_df_f_data[index])

    plt.figure()
    plt.xlabel("Time (s)")
    plt.ylabel("Speed")
    plt.plot([t / 1000 for t in speed[0]], speed[1])

    plt.figure()
    plt.xlabel("Time (s)")
    plt.ylabel("Whisker motion index")
    plt.plot([t / 1000 for t in whisker_motion_index[0]], whisker_motion_index[1])

    plt.figure()
    plt.xlabel("Time (s)")
    plt.ylabel("State (active period with locomotion/whisking or quiet wakeful state")
    plt.plot(
        [t / 1000 for t in state[0]], state[1], linewidth=0.5, marker=".", markersize=2
    )

    if "-nogui" not in sys.argv:
        plt.show()
