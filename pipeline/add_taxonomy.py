import fileinput
import re
import configuration.folder_structure as folder_structure

def add_taxonomy():
    filename = folder_structure.OTU + '/otutable.txt'

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

def create_lineage():
    # awk -F '\t' -v OFS='\t' '{print $1, $2, $4}' query.txt | taxonkit reformat -I 1 -f "{k}|{p}|{c}|{o}|{f}|{g}|{s}" -F  | tee lineage.txt
    return 0

def create_otu():
    # awk 'FNR==NR{a[$2]=$0; next} ($1 in a) {print a[$1], $0}' lineage.txt otutable.txt > out.txt
    return 0
    