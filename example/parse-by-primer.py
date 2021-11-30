import re
from pathlib import Path

input_file = Path('/Users/moritzkunzl/Documents/GitHub/metabar-coding/example/paired/fasta-quality/1_734_S1_paired.assembled_q30.fasta')

forward_primer = 'ACACCGCCCGTCACCCT'
reverse_primer = 'GGGCGGTGT'
header = ''

file_reader = open(input_file, 'r')
print(input_file)

output_file = input_file.with_name(input_file.stem + '_matchPrimer' + input_file.suffix)
file_writer = open(output_file, 'w')
print(output_file)

for line in file_reader:
    if re.search(rf'^{forward_primer}.*{reverse_primer}$', line):
        file_writer.write(header)
        trimmed_line = line.removeprefix(forward_primer).removesuffix(reverse_primer)
        file_writer.write(trimmed_line)
        pass
    header = line

file_reader.close()
file_writer.close()
