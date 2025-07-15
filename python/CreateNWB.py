from datetime import datetime

from dateutil.tz import tzlocal
import pynwb
import platform
import hdmf

from LoadMatData import load_mat_file

start_time = datetime.now(tz=tzlocal())
create_date = datetime.now(tz=tzlocal())


hdmf_ver = "v%s" % hdmf.__version__

paper_title = "Multidimensional population activity in an electrically coupled inhibitory circuit in the cerebellar cortex"
authors = ["Harsha Gurnani", "R. Angus Silver"]
main_experimenter = "Harsha Gurnani"

ref = "GurnaniSilver2021"

info = (
    "NWB file based on data from %s, created with pynwb v%s (hdmf %s), Python v%s"
    % (
        paper_title,
        pynwb.__version__,
        hdmf_ver,
        platform.python_version(),
    )
)
nwbfile = pynwb.NWBFile(
    ref,
    "NWB123",
    start_time,
    file_create_date=create_date,
    notes=info,
    experimenter=main_experimenter,
    experiment_description=(
        "This dataset was used in the study “Multidimensional population activity in an electrically coupled inhibitory circuit in the cerebellar cortex” by Gurnani and Silver in Neuron, 2021. It includes pre-processed two-photon imaging data and behavioural data from head-fixed awake mice exhibiting spontaneous whisking and locomotion on a cylindrical wheel."
    ),
    institution="University College London",
    lab="Silver Lab",
)

mat_file = "../data/FL90__180316_15_20_48.mat"
# Load the .mat file
neuron_df_f_data = load_mat_file(mat_file)


for i in range(len(neuron_df_f_data)):
    cell_id = i
    print("Adding cell data %i" % cell_id)
    data = neuron_df_f_data[cell_id]

    # TODO: Not correct units!!!
    timestamps = [t for t in range(len(data))]

    ts = pynwb.TimeSeries("Sweep_%i" % cell_id, data, "SIunit", timestamps=timestamps)

    nwbfile.add_acquisition(ts)

nwb_file_name = "Gurnani2021.nwb"

print("Saving NWB file: %s" % nwbfile)
io = pynwb.NWBHDF5IO(nwb_file_name, mode="w")

print("Written: %s" % info)

io.write(nwbfile)
io.close()
