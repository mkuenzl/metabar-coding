import glob
import os
import re
import configuration.folder_structure as folder_structure
import fileinput


def parse(forward_primer: str, reverse_primer: str):
    os.makedirs(folder_structure.FASTA_QUALITY_TRIMMED, exist_ok=True)

    header = ''

    for filename in glob.iglob(folder_structure.FASTA_QUALITY + '/*_paired.assembled_q30.fasta'):
        with open(filename, 'r') as file_reader:
            print(filename)
            output_file = filename.replace('_paired.assembled_q30.fasta', '_paired.assembled_q30_matchPrimer.fasta') \
                .replace(folder_structure.FASTA_QUALITY, folder_structure.FASTA_QUALITY_TRIMMED)
            with open(output_file, 'w') as file_writer:
                print(output_file)

                # TODO 
                # ! PROBLEM !
                # ! probe tags are not created 
                # ! sequences without primer are not removed

                for line in file_reader:
                    if re.search(rf'^{forward_primer}.*{reverse_primer}$', line):
                        file_writer.write(header)
                        lineWithoutPrefix = line[len(forward_primer):]
                        # lineWithoutPrefix = line.removeprefix(forward_primer)
                        if lineWithoutPrefix.endswith("\n"):
                            lineWithoutPreSuffix = lineWithoutPrefix[:-len(reverse_primer + "\n")]
                            # lineWithoutPreSuffix = lineWithoutPrefix.removesuffix(reverse_primer + "\n")
                            file_writer.write(lineWithoutPreSuffix + "\n")
                        else:
                            lineWithoutPreSuffix = lineWithoutPrefix[:-len(reverse_primer)]
                            # lineWithoutPreSuffix = lineWithoutPrefix.removesuffix(reverse_primer)
                            file_writer.write(lineWithoutPreSuffix)
                        pass
                    header = line
                file_writer.close()
            file_reader.close()


def label():
    for filename in glob.iglob(folder_structure.FASTA_QUALITY_TRIMMED + '/*.fasta'):
        with fileinput.input(filename, inplace=1) as file_reader_writer:
            line_counter = 1
            for line in file_reader_writer:
                if re.search(rf'^>', line):
                    file_id = filename.replace(folder_structure.FASTA_QUALITY_TRIMMED + '/', '') \
                        .replace('_paired.assembled_q30_matchPrimer.fasta', '.')
                    # identifier = file_id[file_id.find('_'):]
                    print(line.replace(line, '>' + file_id + str(line_counter)))
                    line_counter += 1
                    pass
                else:
                    print(line.replace('\n', ''))
            file_reader_writer.close()
