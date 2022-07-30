import os
import configuration.folder_structure as folder_structure

def cluster():
    
    output_dir = folder_structure.OTU #'../example/otu'
    uniques_file = output_dir + '/uniques.fasta'
    otus_file = output_dir + '/otus.fasta'

    os.system('usearch'
                + ' '
                + '-cluster_otus' + ' ' + uniques_file
                + ' '
                + '-otus' + ' ' + otus_file
                + ' '
                + '-relabel' + ' ' + 'Otu'
                + ' '
                + '-minsize' + ' ' + '10')
