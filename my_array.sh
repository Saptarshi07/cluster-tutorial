#!/bin/bash
#SBATCH --job-name=arrays
#SBATCH -N 1
#SBATCH -n 1
#SBATCH --mem=1GB
#SBATCH --output=my_output_%A_%a.txt

module load python/3.7.4

python simple_python.py run_files/run_file-$SLURM_ARRAY_TASK_ID.txt