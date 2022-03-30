import subprocess
import argparse
import os, sys

# read inputs provided by user
parser = argparse.ArgumentParser()
parser.add_argument('--input-zip', help="Zip folder containing input in the format described in Description")
parser.add_argument('--docking', nargs='*',help="Which docking to perform: flexible self-docking (flex) or rigid re-docking (rigid). Default: Flexible self-docking (flex)")
args = parser.parse_args()

os.makedirs('input/', exist_ok=True)
os.makedirs('output/', exist_ok=True)


subprocess.run([
    'unzip',
    args.input_zip,
])

# Write inference yml and call using --configs 
with open("inference.yml", "w") as inf:
    inf.write(f"run_dirs:\n")
    if args.docking[0] == "flex":
        inf.write(f"  - flexible_self_docking\n")
    else:
        inf.write(f"  - rigid_redocking\n")
    if len(args.docking) == 2: 
        inf.write(f"  - flexible_self_docking\n")
        inf.write(f"  - rigid_redocking\n")
    
    inf.write("output_directory: 'output'\n")
    inf.write("run_corrections: True\n")
    inf.write("use_rdkit_coords: False\n")
    inf.write("save_trajectories: true\n\n")

    inf.write("num_confs: 1'\n")

    
    


sys.exit(1)
subprocess.run([
    'python3',
    'inference.py',
    '--configs',
    'inference.yml',
    '--output_directory',
    'output/'])#,
#    '--inference_path',
#    'input/',
#])
