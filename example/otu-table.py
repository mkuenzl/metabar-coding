#   2. Transform Quality Filtered Fastq Files to Fasta
import fileinput
import glob
import os

output_dir = 'otu'

merged_file = output_dir + '/merged.fasta'
otu_file = output_dir + '/otus.fasta'
otu_table_file = output_dir + '/otutable.txt'

os.system('usearch '
          + '-usearch_global '
          + merged_file
          + ' -db '
          + otu_file
          + ' -strand plus '
          + '-id 0.97 '
          + '-otutabout '
          + otu_table_file)
