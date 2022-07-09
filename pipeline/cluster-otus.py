import os

output_dir = '../example/otu'

uniques_file = output_dir + '/uniques.fasta'
otus_file = output_dir + '/otus.fasta'

os.system('usearch '
          + '-cluster_otus '
          + uniques_file
          + ' -otus '
          + otus_file
          + ' -relabel Otu '
          + '-minsize 10')
