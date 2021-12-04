#   2. Transform Quality Filtered Fastq Files to Fasta
import glob
import os

# input_dir = 'paired/fasta-quality'
input_dir = 'trimmed'
output_dir = 'unique'
os.makedirs(output_dir, exist_ok=True)

files = glob.iglob(input_dir + '/*.fasta')

for filename in files:
    # print(filename)
    output_filename = filename.replace('.fasta', '_unique.fasta').replace(input_dir, output_dir)
    # print(output_filename)
    os.system('usearch '
              + '-fastx_uniques '
              + filename
              + ' -fastaout '
              + output_filename
              + ' -relabel Uniq '
              + '-sizeout')
