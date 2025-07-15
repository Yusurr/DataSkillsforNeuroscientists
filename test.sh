 
#!/bin/bash
set -ex

# Format and check Python files using ruff
ruff format python/*.py
ruff check python/*.py

# Install Python dependencies
pip install -r requirements.txt

# Run the data loading scripts
cd python
python LoadCSVData.py -nogui
python LoadMatData.py -nogui

# Regenerate the NWB file
python WriteMetadata.py
python CreateNWB.py

echo "Finished running tests"