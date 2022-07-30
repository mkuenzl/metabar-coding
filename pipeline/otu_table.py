import os
import configuration.folder_structure as folder_structure

def create_table(strand: str, id: int):
    
    output_dir = folder_structure.OTU #'../example/otu'

    merged_file = output_dir + '/merged.fasta'
    otu_file = output_dir + '/otus.fasta'
    otu_table_file = output_dir + '/otutable.txt'

    os.system('usearch'
            + ' '
            + '-usearch_global' + ' ' + merged_file
            + ' '
            + '-db' + ' ' + otu_file
            + ' '
            + '-strand'+ ' ' + strand
            + ' '
            + '-id' + ' ' + id
            + ' '
            + '-otutabout' + ' ' + otu_table_file)
