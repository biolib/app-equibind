#!/bin/bash
echo "Hello World"
source /opt/conda/etc/profile.d/conda.sh
conda activate equibind
python3 run_equibind.py $@
