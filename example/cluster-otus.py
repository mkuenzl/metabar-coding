#   2. Transform Quality Filtered Fastq Files to Fasta
import fileinput
import glob
import os

output_dir = 'otu'

uniques_file = output_dir + '/uniques.fasta'
merged_file = output_dir + '/otus.fasta'

os.system('usearch '
          + '-cluster_otus '
          + uniques_file
          + ' -otus '
          + merged_file
          + ' -relabel Otu '
          + '-minsize 10')
