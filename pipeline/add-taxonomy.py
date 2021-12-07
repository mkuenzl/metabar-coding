#   2. Transform Quality Filtered Fastq Files to Fasta
import fileinput
import glob
import os
import re

filename = 'otu/otutable.txt'

with fileinput.input(filename, inplace=1) as file_reader_writer:
    line_counter = 1
    for line in file_reader_writer:
        # retrieve Otu references
        split_by_tab = line.split('\t')
        otu = split_by_tab[0]

        # search for Otu reference in query
        if re.search(rf'^Otu', line):
            print(line.replace(line, '>' + str(line_counter)))
            line_counter += 1
            pass
        else:
            print(line.replace('\n', ''))

        # print taxonomy between Otu & Reads

    file_reader_writer.close()

# awk -F '\t' -v OFS='\t' '{print $1, $2, $4}' query.txt | taxonkit reformat -I 1 -f "{k}|{p}|{c}|{o}|{f}|{g}|{s}" -F  | tee lineage.txt

# awk 'FNR==NR{a[$2]=$0; next} ($1 in a) {print a[$1], $0}' lineage.txt otutable.txt > out.txt