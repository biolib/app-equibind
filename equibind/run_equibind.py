import subprocess
import argparse
import os, sys, shutil

# read inputs provided by user
parser = argparse.ArgumentParser()
parser.add_argument('--prot', help="A single file or a zip folder containing input protein in PDB format")
parser.add_argument('--binder', help="A single file or a zip folder containing input binder in .mol2 or .sdf format")
parser.add_argument('--docking', nargs='*',help="Which docking to perform: flexible self-docking (flex) or rigid re-docking (rigid). Default: Flexible self-docking (flex)")
args = parser.parse_args()

# TODO PDB can be a single file as well check if it ends with PDB or .zip:
os.makedirs('pdb/', exist_ok=True)
os.makedirs('binder/', exist_ok=True)
os.makedirs('output/', exist_ok=True)

subprocess.run([
    'unzip',
    args.pdb,
])
subprocess.run([
    'unzip',
    args.binder,
])

os.rename("input", "PDBBind")
shutil.move('PDBBind', "data/")
# Write input names:
i_names = os.listdir("data/PDBBind/")
with open("data/input_names", "w") as input_names:
    for i in i_names:
        input_names.write(i)

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

    inf.write("num_confs: 1\n")


subprocess.run([
    'python3',
    'inference_biolib.py',
    '--config',
    'inference.yml',
    '--output_directory',
    'output/'])#,
#    '--inference_path',
#    'input/',
#])

import pandas as pd

df_opt = pd.read_csv("equibind-opt_scoring.csv")

with open("output.md", "w") as mdout:
    mdout.write("# Equibind\n\n")
    mdout.write("Equibind optmizied scoring:\n")
    mdout.write(df_opt.to_markdown())

    # Maybe link to donwloading the top 10 or top 1 sdf files + pdb file


