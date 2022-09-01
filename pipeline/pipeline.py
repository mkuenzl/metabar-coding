import configuration.helper_config as helper_config
import assemble_sequence as assemble_sequence
import sequence_filter_to_fasta as filter_sequence
import parse_primer as primer
import find_uniques as unique
import cluster_otus
import cluster_zotus
import otu_table
import blast_otus
import add_taxonomy

config = helper_config.read_config()

# Pre-Analysis sequence-quality-check

# 1. sequence-assemble
# pear_config = config['pear']
# # assemble_sequence.assemble('/home/mkuen/Documents/metabar-lara/',
#
# assemble_sequence.assemble('/media/mkuen/Hama_USB/Metabarcode_NW',
#                            pear_config['f'],
#                            pear_config['r'],
#                            pear_config['q'],
#                            pear_config['v'],
#                            pear_config['j'])
#
# # 2. sequence-filter-to-fasta
# quality_config = config['fastq_quality_filter']
#
# filter_sequence.quality_filter_fastq(quality_config['p'], quality_config['q'])
# filter_sequence.transform_fastq_to_fasta()

# 3. parse-by-primer
primer_config = config['primer']

primer.parse(primer_config['forward'], primer_config['reverse'])
primer.label()

# find-uniques
unique.retrieve()

# TODO Problem otus not the same as in the example check with whole dataset

# cluster-otus
# cluster_otus.cluster()
cluster_zotus.cluster()

# otu-table
table_config = config['usearch_global']

otu_table.create_table(table_config['strand'], table_config['id'])

# blast-otus
print('start blastn...')
blast_config = config['blastn']

blast_otus.blastn(database=blast_config['db'],
                  formatting=blast_config['outfmt'],
                  max_seqs=blast_config['max_target_seqs'])

# add-taxonomy
add_taxonomy.add_taxonomy()  # Not working
add_taxonomy.create_lineage()  # TODO
add_taxonomy.create_otu()  # TODO
