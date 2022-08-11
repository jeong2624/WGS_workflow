#!/usr/bin/env python
# chmod +x /home/pjw/Workspace/NGS/DNA_seq/pipeline/samtools.py

import os
class samtools:
    def __init__(self, directory):
        self.directory = directory

    def conversion(self, file_name):
        self.file_name = file_name
        activation = "samtools view -Sb " + self.directory + self.file_name + " -o " + self.directory + "sample.mapped.bam"
        return activation

    def ref_index(self, file_name):
        self.file_name = file_name
        activation = "samtools faidx " + self.directory + self.file_name
        return activation

    def raw_index(self, file_name):
        self.file_name = file_name
        activation = "samtools fqidx " + self.directory + self.file_name
        return activation

    def sorting(self, file_name):
        self.file_name = file_name
        activation = "samtools sort -o " + self.directory + file_name.replace(file_name[-3:], "") + "sorted.bam " + self.directory + file_name
        return activation

    def fixmate(self, file_name):
        self.file_name = file_name
        activation = "samtools fixmate -m " + self.directory + file_name + " " + self.directory + "sample.fixmate.bam"
        return activation

    def markdup(self, file_name):
        self.file_name = file_name
        activation = "samtools markdup " + self.directory + file_name + " " + self.directory + "sample.markdup.bam"
        return activation

    def bam_index(self, file_name):
        self.file_name = file_name
        activation = "samtools index " + self.directory + file_name
        return activation

    def fasta_dict(self, file_name):
        self.file_name = file_name
        activation = "samtools dict " + self.directory + file_name + " -o " + self.directory + file_name.replace(file_name[-2:], "") + "dict"
        return activation
