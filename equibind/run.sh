#!/bin/bash
source /opt/conda/etc/profile.d/conda.sh
conda activate equibind
python3 run_equibind.py $@
