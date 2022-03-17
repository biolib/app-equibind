import subprocess
import argparse

# read inputs provided by user
parser = argparse.ArgumentParser()
parser.add_argument('--input-zip', help="Zip folder containing input in the format described in Description")
args = parser.parse_args()

os.makedirs('input/', exists_ok=True)
os.makedirs('output/', exists_ok=True)


subprocess.run([
    'unzip',
    args.input_zip,
    '-d',
    'input/'
])


subprocess.run([
    'python3 inference.py',
    '--output-directory',
    'output/',
    '--inference-paths',
    'input/'
])