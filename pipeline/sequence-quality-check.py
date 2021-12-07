import gzip
import os
import shutil

# From: https://www.bioinformatics.babraham.ac.uk/projects/fastqc/INSTALL.txt
# Running FastQC Interactively
# ----------------------------
# Windows: Simply double click on the run_fastqc bat file.  If you want to make a pretty
# shortcut then we've included an icon file in the top level directory so you don't have
# to use the generic bat file icon.
#
# MacOSX: There is an application bundle for MacOSX which you can use to install and run
# FastQC.  Just drag the application from the disk image to your Applications folder (or
# wherever you want to install the program).
#
# Linux:  We have included a wrapper script, called 'fastqc' which is the easiest way to
# start the program.  The wrapper is in the top level of the FastQC installation.  You
# may need to make this file executable:
#
# chmod 755 fastqc
#
# ..but once you have done that you can run it directly
#
# ./fastqc
#
# ..or place a link in /usr/local/bin to be able to run the program from any location:
#
# sudo ln -s /path/to/FastQC/fastqc /usr/local/bin/fastqc

file_tag = '.fastq.gz'
zip_directory = input("Please enter the directory path of your fastq.gz files: ")

unzip_directory = zip_directory + '/fastq'
os.makedirs(unzip_directory, exist_ok=True)

#   1. unzip file
for filename in os.listdir(zip_directory):
    if filename.endswith(file_tag):
        with gzip.open(zip_directory + '/' + filename, 'rb') as f_in:
            with open(unzip_directory + '/' + filename.replace('.gz', ''), 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)


#   2. fastqc file
fastqc_directory = zip_directory + '/fastqc'
os.makedirs(fastqc_directory, exist_ok=True)

for filename in os.listdir(unzip_directory):
    os.system('fastqc ' + unzip_directory + '/' + filename + ' --outdir=' + fastqc_directory)
