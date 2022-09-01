import os
import configuration.folder_structure as folder_structure


def cluster():
    output_dir = folder_structure.OTU  # '../example/otu'
    uniques_file = output_dir + '/uniques.fasta'
    zotus_file = output_dir + '/otus.fasta'

    os.system('usearch'
              + ' '
              + '-unoise3' + ' ' + uniques_file
              + ' '
              + '-zotus' + ' ' + zotus_file
              )


if __name__ == "__main__":
    cluster()
