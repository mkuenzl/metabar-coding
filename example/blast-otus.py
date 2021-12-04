import os

input_dir = 'otu'
otus_file = input_dir + '/otus.fasta'
query_file = input_dir + '/query.txt'

os.system('blastn '
          + '-db '
          + 'nt '
          + '-query '
          + otus_file
          + ' -outfmt '
          + '"6 staxids qseqid sseqid pident evalue stitle sstrand" '
          + '-max_target_seqs '
          + '1'
          + ' -out '
          + query_file
          + ' -remote')
