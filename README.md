# metabar-coding
Documentation of the automation.

There are a lot of programs and libaries which already do what we are trying to automate here. 
But they suck.
| program  | link |
| ------------- | ------------- |
| DECIPHER KEGG  | http://www2.decipher.codes/Downloads.html  |
| UNITE  | https://unite.ut.ee/repository.php  |
| DADA  | https://benjjneb.github.io/dada2/training.html  |
| Silva  | https://zenodo.org/record/1447330  |
 

### What do you need?

1. A linux system - we build on ubuntu

2. A lot of binaries which should be added to the $path

  - FastQC (Quality check of sequences) <br/>
    https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ </br>
    Use the INSTALL.txt to add the fastqc.perl script to your /usr/bin folder

  - Pear (Assembly of paired reads and quality trimming) <br/>
    https://www.h-its.org/de/downloads/pear-academic/

  - FastX Toolkit (Quality filter assembled fastq sequences and transform to fasta files)  <br/>
    http://hannonlab.cshl.edu/fastx_toolkit/download.html

  - Usearch (Sequence dereplication, OTU clustering and building of OTU table) <br/>
    https://www.drive5.com/usearch/download.html

  - Blastn (Assign taxonomy to OTUs) <br/>
    https://blast.ncbi.nlm.nih.gov/Blast.cgi?CMD=Web&PAGE_TYPE=BlastDocs&DOC_TYPE=Download

  - Blastn Taxonomy File (add folder of unpacked file to path with "export BLASTDB=path/to/folder")
    ftp://ftp.ncbi.nlm.nih.gov/blast/db/taxdb.tar.gz

  - TaxonKit </br>
    https://bioinf.shenwei.me/taxonkit/
   
3. Some understanding of shell scripts. 

4. Your Primertable

| species  | primer | direction | sequence | amplicon size |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| Newts	| 12S V5 Primer	| Forward	| TAGAACAGGCTCCTCTAG	| Min: 73BP Max:110BP |
|  |                | Reverse	| TTAGATACCCCACTATGC |
| Fire Salamander	| 12S Primer 	| Forward	| ACACCGCCCGTCACCCT	| Mean: 51BP Max 100BPG4 |
||                            | Reverse	| GTAYACTTACCATGTTACGACTT |

## Follow the example

1. Check the quality <br/>
```
fastqc FILE
```
2. Assemble forward and reverse sequences <br/>
```
pear -f FW.fastq.gz -r RV.fastq.gz -q 20 -v 50 -o FILENAME
```
3. Quality filter, remove with less than 90% bases with Q30 or higher <br/> 
```
fastq_quality_filter -Q33 -p 90 -q 30 -i  FILE.fastq -o FILE_Q30.fastq
```
4. Transform fastq file to fasta format <br/> 
```
fastq_to_fasta -Q33 -i FILE_Q30.fastq -o FILENAME.fasta
```
5. Filter all sequences from fasta file <br/> 
```
grep -E -B1 “^forwardPrimerSequence.*reverseComplementOfReversePrimerSequence$” FILE.fasta > NEWFILE.fasta
```
 (Degenerate primers GTAAC[A-Z]GTATA[A-Z]CCCTTG or GTAAC.GTATA.CCCTTG)
6. Trim off primer sequences <br/> 
```
grep -E -B1 “^forwardPrimerSequence.*reverseComplementOfReversePrimerSequence$” FILE.fasta 
        | sed -r ‘/^[A-Z]/s/^.{22}//’ 
                | sed -r ‘/^[A-Z]/s/.{26}$//’ > NEWFILE.fasta
```
7. Filter by 6bp inline barcode <br/> 
```
grep -E -B1 “^Barcode” FILENAME.fasta > NEWFILE.fasta
```
8. OTU Clustering 
    - Merge and count identical sequences <br/> 
        ```
        usearch -fastx_uniques FILE.fasta -fastaout FILE.uniq.fasta -sizeout
        ```
    - OTU clustering and generation of centroid sequence database based on divergence cuttoff <br/> 
        ```
        usearch -cluster_otus FILE.uniq.fasta -otus FILE.otus.fasta  -relabel OUT -minsize 10
        ```
9. BLAST against NCBI database <br/>
   QUERY.fasta are equal to finale fasta file with DNA code  <br/> 
   Output format: (https://www.metagenomics.wiki/tools/blast/blastn-output-format-6) <br/>
   FORMATTER "6 staxids qseqid sseqid pident evalue sscinames scomnames sblastnames sskingdoms stitle salltitles sstrand"
```
Run on your PC with a database
blastn -db database.fasta -query QUERY.fasta -outfmt 6 -max_target_seqs 1 -out FILE.out

Run on Blast Webserver with their databases 
blastn -db nt -query QUERY.fasta -outfmt FORMATTER -max_target_seqs 1 -out FILE.out -remote
```
10. Generate OTU table by comparing all sequences against  database <br/> 
```
usearch -usearch_global Database.fasta -db FILE.otus.fasta -strand plus -id 0.97 -otutabout otu_table.txt
```


