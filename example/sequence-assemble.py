import glob
import os


file_tag = '.fastq.gz'
# zip_directory = input("Please enter the directory path of your fastq.gz files: ")

zip_directory = 'data'

paired_directory = 'pairs'
os.makedirs(paired_directory, exist_ok=True)

forward_files = glob.iglob(zip_directory + '/*L001_R1_001.fastq.gz')

file_pairs = ((forward, forward.replace('L001_R1_001.fastq.gz', 'L001_R2_001.fastq.gz')) for forward in forward_files)
for forward, backward in file_pairs:
    os.system('pear -f '
              + forward
              + ' -r '
              + backward
              + ' -q 20 -v 50 -j 12 -o '
              + forward.replace('L001_R1_001.fastq.gz', 'paired').replace(zip_directory, paired_directory))
