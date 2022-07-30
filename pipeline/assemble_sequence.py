import glob
import os
import configuration.folder_structure as folder_structure

def assemble(zip_directory: str, forward_tag: str, reverse_tag: str, q: int, v: int, j: int):

    output_dir = folder_structure.ASSEMBLED
    os.makedirs(output_dir, exist_ok=True)

    forward_files = glob.iglob(zip_directory + '/*{}'.format(forward_tag))

    file_pairs = ((forward, forward.replace(forward_tag, reverse_tag)) for forward in forward_files)
    for forward, backward in file_pairs:
        os.system('pear'
                + ' ' 
                + '-f' + ' ' + forward
                + ' '
                + '-r' + ' ' + backward
                + ' '
                + '-q' + ' ' + q
                + ' '
                + '-v' + ' ' + v
                + ' '
                + '-j' + ' ' + j
                + ' ' 
                + '-o' + ' ' + forward.replace('L001_R1_001.fastq.gz', 'paired').replace(zip_directory, output_dir))
