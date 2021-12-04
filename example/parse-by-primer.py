import glob
import os
import re

input_dir = 'paired/fasta-quality'

output_dir = 'trimmed'

os.makedirs(output_dir, exist_ok=True)

forward_primer = 'ACACCGCCCGTCACCCT'
reverse_primer = 'GGGCGGTGT'
header = ''

for filename in glob.iglob(input_dir + '/*_paired.assembled_q30.fasta'):
    with open(filename, 'r') as file_reader:
        print(filename)
        output_file = filename.replace('_paired.assembled_q30.fasta', '_paired.assembled_q30_matchPrimer.fasta')\
            .replace(input_dir, output_dir)
        with open(output_file, 'w') as file_writer:
            print(output_file)
            for line in file_reader:
                if re.search(rf'^{forward_primer}.*{reverse_primer}$', line):
                    file_writer.write(header)
                    trimmed_line = line.removeprefix(forward_primer).removesuffix(reverse_primer)
                    file_writer.write(trimmed_line)
                    pass
                header = line
            file_writer.close()
        file_reader.close()
