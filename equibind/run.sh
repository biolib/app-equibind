#!/bin/bash
source /opt/conda/etc/profile.d/conda.sh
conda activate equibind
python3 inference.py $@
