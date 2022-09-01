import glob
import os
import configuration.folder_structure as folder_structure


#   1. Create Quality Filtered Fastq Files
def quality_filter_fastq(p: int, q: int):
    os.makedirs(folder_structure.FASTQ_QUALITY, exist_ok=True)

    assembled_files = glob.iglob(folder_structure.ASSEMBLED + '/*.assembled.fastq')

    for filename in assembled_files:
        output_filename = filename.replace('assembled', 'assembled_q30').replace(folder_structure.ASSEMBLED,
                                                                                 folder_structure.FASTQ_QUALITY)
        os.system('fastq_quality_filter'
                  + ' '
                  + '-Q33'
                  + ' '
                  + '-p' + ' ' + p
                  + ' '
                  + '-q' + ' ' + q
                  + ' '
                  + '-i' + ' ' + filename
                  + ' '
                  + '-o' + ' ' + output_filename)


#   2. Transform Quality Filtered Fastq Files to Fasta
def transform_fastq_to_fasta():
    os.makedirs(folder_structure.FASTA_QUALITY, exist_ok=True)

    quality_files = glob.iglob(folder_structure.FASTQ_QUALITY + '/*.fastq')

    for filename in quality_files:
        output_filename = filename.replace('.fastq', '.fasta').replace(folder_structure.FASTQ_QUALITY,
                                                                       folder_structure.FASTA_QUALITY)

        os.system('fastq_to_fasta'
                  + ' '
                  + '-Q33'
                  + ' '
                  + '-i' + ' ' + filename
                  + ' '
                  + '-o' + ' ' + output_filename)


if __name__ == "__main__":
    quality_filter_fastq(90, 30)
    transform_fastq_to_fasta()
