#!/bin/bash

#SBATCH --job-name=firstbatch
#SBATCH -N 1
#SBATCH -n 1 
#SBATCH --time=5:00
#SBATCH --output=output.out
#SBATCH --error=error.err

module load python/3.7.4

python simple_python.py simple_text.txt