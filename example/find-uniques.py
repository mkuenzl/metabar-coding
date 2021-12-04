#   2. Transform Quality Filtered Fastq Files to Fasta
import fileinput
import glob
import os

input_dir = 'trimmed'
output_dir = 'otu'
os.makedirs(output_dir, exist_ok=True)
uniques_file = output_dir + '/uniques.fasta'
merged_file = output_dir + '/merged.fasta'


files = glob.iglob(input_dir + '/*.fasta')
with open(merged_file, 'w') as output_file:
    for line in fileinput.input(files):
        output_file.write(line)

os.system('usearch '
          + '-fastx_uniques '
          + merged_file
          + ' -fastaout '
          + uniques_file
          + ' -relabel Uniq '
          + '-sizeout')
