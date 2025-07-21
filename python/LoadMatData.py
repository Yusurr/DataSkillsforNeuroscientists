import matplotlib.pyplot as plt
import sys

# Package for importing MATLAB mat v7.3 files
import mat73


def load_mat_file(mat_file):
    """
    Load a MATLAB .mat file of Gurnani & Silver data using mat73.

    Parameters:
    mat_file (str): Path to the .mat file.

    Returns:
    dict: Dictionary containing the loaded data.
    """
    print(f"Loading data from: {mat_file}")

    mat = mat73.loadmat(mat_file)
    # Print the keys to see what's inside
    print("Variables in the .mat file:", mat.keys())

    neuron_df_f = mat["allData"]["neurons"]["f"].T
    print(f"Neuron data (shape: {neuron_df_f.shape})")

    neuron_times = mat["allData"]["neurons"]["time"].T
    print(f"Neuron times data (shape: {neuron_times.shape})")

    speed = mat["allData"]["behaviour"]["speed"].T
    print(f"Speed data (shape: {speed.shape})")

    whisker_motion_index = mat["allData"]["behaviour"]["whiskerMI"].T
    print(f"Whisker motion index data (shape: {whisker_motion_index.shape})")

    state = mat["allData"]["behaviour"]["state"].T
    print(f"State data (shape: {state.shape})")

    pca_dff = mat["allAnalysed"]["PCA"]["dff"]["all"]["proj"]
    print(f"PCA of dF/F data (shape: {pca_dff.shape})")

    if (
        "puff_whisker" in mat["allEvents"]
        and mat["allEvents"]["puff_whisker"] is not None
    ):
        puff_events = mat["allEvents"]["puff_whisker"].T
        print(f"Puff event data (shape: {puff_events.shape})")
    else:
        puff_events = []

    return (
        neuron_df_f,
        neuron_times,
        speed,
        whisker_motion_index,
        state,
        pca_dff,
        puff_events,
    )


if __name__ == "__main__":
    mat_file = "../data/HG24__190726_15_44_45.mat"  # Example file, change as needed
    mat_file = "../data/FL90__180316_15_20_48.mat"
    # Load the .mat file

    (
        neuron_df_f_data,
        neuron_times,
        speed,
        whisker_motion_index,
        state,
        pca_dff,
        puff_events,
    ) = load_mat_file(mat_file)

    plt.imshow(neuron_df_f_data, aspect="auto", cmap="viridis")
    plt.colorbar()
    plt.xlabel("Time point")
    plt.ylabel("Neuron #")

    plt.title("Plot from .mat file")

    plt.figure()

    plt.xlabel("Time (s)")
    plt.ylabel("dF/F")

    for index in range(len(neuron_df_f_data)):
        plt.plot(
            [t / 1000 for t in neuron_times[index]],
            neuron_df_f_data[index] - index,
            color="k",
            linewidth=0.5,
        )

    if len(puff_events) > 0:
        for e in puff_events[0]:
            print("Adding puff event at time %s" % (e / 1000))
            plt.plot(e / 1000, 2, color="r", linestyle=None, marker=".", markersize=2)

    plt.figure()

    plt.xlabel("Time (s)")
    plt.ylabel("PCA dF/F")

    for index in range(len(pca_dff)):
        plt.plot(pca_dff[index] + index * -10, label=f"PC {index+1}")

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
