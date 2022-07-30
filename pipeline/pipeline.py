import configuration.helper_config as helper_config

config = helper_config.read_config()

fastq_quality_filter = config['fastq_quality_filter']['q']

print(fastq_quality_filter)

# sequence-quality-check

# sequence-assemble

# sequence-filter-to-fasta

# parse-by-primer

# label-fasta

# find-uniques

# cluster-otus

# otu-table
