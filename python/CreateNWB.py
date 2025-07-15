from datetime import datetime

from dateutil.tz import tzlocal
import pynwb
import platform
import hdmf
from LoadMatData import load_mat_file

from WriteMetadata import metadata

session_start_time = datetime.now(tz=tzlocal())
create_date = datetime.now(tz=tzlocal())


hdmf_ver = "v%s" % hdmf.__version__

original_experiment_id = "FL90__180316_15_20_48"
mat_file = f"../data/{original_experiment_id}.mat"

nwb_file_info = (
    "NWB file based on data from %s, created with pynwb v%s (hdmf %s), Python v%s"
    % (
        metadata["paper_title"],
        pynwb.__version__,
        hdmf_ver,
        platform.python_version(),
    )
)

nwbfile = pynwb.NWBFile(
    session_description=metadata["reference"],
    identifier=original_experiment_id,
    session_start_time=session_start_time,
    file_create_date=create_date,
    notes=nwb_file_info,
    experimenter=metadata["experimenter"],
    experiment_description=metadata["experiment_description"],
    institution=metadata["institution"],
    lab=metadata["lab"],
)

# Load the .mat file
neuron_df_f_data, neuron_times, speed, whisker_motion_index, state = load_mat_file(
    mat_file
)

recorded_data = {"Wheel speed": speed}

for key, value in recorded_data.items():
    print(f"Adding recorded data: {key} with shape {value.shape}")
    ts = pynwb.TimeSeries(
        name=key, data=value[1], unit="??", timestamps=value[0] / 1000
    )
    # nwbfile.add_acquisition(ts)


for i in range(len(neuron_df_f_data)):
    neuron_id = i + 1
    print("Adding neuron data %i" % neuron_id)
    data = neuron_df_f_data[i]

    # TODO: Not correct units!!!
    timestamps = [t for t in neuron_times[i] / 1000]  # Convert to seconds

    ts = pynwb.TimeSeries(
        "Neuron %i fluorescence" % neuron_id, data, "seconds", timestamps=timestamps
    )

    # nwbfile.add_acquisition(ts)

nwb_file_name = "Gurnani2021.nwb"

print("Saving NWB file: \n%s" % nwbfile)
io = pynwb.NWBHDF5IO(nwb_file_name, mode="w")

print("Written: %s" % nwb_file_name)

io.write(nwbfile)
io.close()
