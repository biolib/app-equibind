import subprocess
import argparse
import os

# read inputs provided by user
parser = argparse.ArgumentParser()
parser.add_argument('--input-zip', help="Zip folder containing input in the format described in Description")
args = parser.parse_args()

os.makedirs('input/', exist_ok=True)
os.makedirs('output/', exist_ok=True)


subprocess.run([
    'unzip',
    args.input_zip,
])


subprocess.run([
    'python3',
    'inference.py',
    '--output_directory',
    'output/',
    '--inference_path',
    'input/'
])
