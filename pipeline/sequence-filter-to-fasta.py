import glob
import os


def main():
    file_tag = '.fastq.gz'
    # assembled_directory = input("Please enter the directory path of your assembled files: ")
    assembled_directory = 'pairs'

    fasta_directory = assembled_directory + '/fasta-quality'
    fastq_quality_directory = fasta_directory + '/fastq'

    os.makedirs(fastq_quality_directory, exist_ok=True)

    assembled_files = glob.iglob(assembled_directory + '/*.assembled.fastq')

    #   1. Create Quality Filtered Fastq Files
    for filename in assembled_files:
        # print(filename)
        output_filename = filename.replace('assembled', 'assembled_q30').replace(assembled_directory,
                                                                                 fastq_quality_directory)
        # print(output_filename)
        os.system('fastq_quality_filter '
                  + '-Q33 -p 90 -q 30 -i '
                  + filename
                  + ' -o '
                  + output_filename)

    #   2. Transform Quality Filtered Fastq Files to Fasta
    quality_files = glob.iglob(fastq_quality_directory + '/*.fastq')

    for filename in quality_files:
        # print(filename)
        output_filename = filename.replace('.fastq', '.fasta').replace(fastq_quality_directory, fasta_directory)
        # print(output_filename)
        os.system('fastq_to_fasta '
                  + '-Q33 -i '
                  + filename
                  + ' -o '
                  + output_filename)


if __name__ == "__main__":
    main()
