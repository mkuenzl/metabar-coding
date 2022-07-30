import os
import configuration.folder_structure as folder_structure

def blastn(database: str, formatting: str, max_seqs: int):

    os.system('blastn'
            + ' '
            + '-db' + ' ' + database
            + ' '
            + '-query' + ' ' + folder_structure.OTU + '/otus.fasta'
            + ' '
            + ' -outfmt' + ' ' + '"' + formatting + '"'
            + ' '
            + '-max_target_seqs' + ' ' + max_seqs
            + ' '
            + '-out' + ' ' + folder_structure.OTU + '/query.txt'
            + ' '
            + '-remote')
