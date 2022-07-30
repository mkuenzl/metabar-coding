import configparser

# create object
config_file = configparser.ConfigParser()

config_file['fastq_quality_filter'] = {
    'p': '90',
    'q': '30'
}

config_file['usearch_cluster'] = {
    'cluster_otus': 'uniques_file',
    'otus': 'otu_file',
    'relabel': 'output',
    'minsize': '10'
}

config_file['usearch_global'] = {
    'usearch_global': 'merged_file',
    'db': 'otu_file',
    'strand': 'plus',
    'id': '0.97',
    'otuabout': 'output'
}

config_file['primer'] = {
    'forward': 'TAGAACAGGCTCCTCTAG',
    'reverse': 'GCATAGTGGGGTATCTAA',
}

config_file['pear'] = {
    #forward file tag
    'f': 'L001_R1_001.fastq.gz',
    #reverse file tag
    'r': 'L001_R2_001.fastq.gz',
    'q': '20',
    'v': '50',
    'j': '12',
    #output file name
    'o': ''
}

config_file['blastn'] = {
    'db': 'nt',
    'query': 'otu_file',
    'outfmt': '6 staxids qseqid sseqid pident evalue stitle sstrand',
    'max_target_seqs': '1',
    'out': 'output_file'
}

with open(r'configuration.ini', 'w') as config_file_object:
    config_file.write(config_file_object)
    config_file_object.flush()
    config_file_object.close()

print("Config file 'configurations.ini' created")

# PRINT FILE CONTENT
read_file = open("configuration.ini", "r")
content = read_file.read()
print("Content of the config file are:\n")
print(content)
read_file.flush()
read_file.close()