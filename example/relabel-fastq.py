import fileinput
import glob
import re

# input_dir = input('Directory: ')
input_dir = '/home/mkuen/git/metabar-coding/example/pairs'

for filename in glob.iglob(input_dir + '/*assembled.fastq'):
    with fileinput.input(filename, inplace=1) as file_reader_writer:
        line_counter = 1
        for line in file_reader_writer:
            if re.search(rf'^>', line):
                file_id = filename.replace(input_dir + '/', '')\
                    .replace('_S1_paired.assembled_q30_matchPrimer.fasta', '.')
                print(line.replace(line, '>' + file_id + str(line_counter)))
                line_counter += 1
                pass
            else:
                print(line.replace('\n', ''))
        file_reader_writer.close()
