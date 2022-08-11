#!/usr/bin/env python
# chmod +x /home/pjw/Workspace/NGS/DNA_seq/pipeline/Alignment.py

import os
class Alignment:
    def __init__(self, directory, ref_name):
        self.directory = directory
        self.ref_name = ref_name

    def bwa_index(self):
        bwa = "/home/pjw/tools/bwa-mem2/bwa-mem2 "
        ref_data = self.directory + self.ref_name
        activation = bwa + "index " + ref_data
        return activation
    
    def bwa_mem(self, mode):
        self.mode = mode
        bwa = "/home/pjw/tools/bwa-mem2/bwa-mem2 "
        ref_data = self.directory + self.ref_name
        raw_data = filter(lambda x: ".fastq.gz" in x, os.listdir(self.directory))

        if mode == "single":
            raw_set = self.directory + raw_data[0]
            activation = bwa + 'mem -t 1 -R "@RG\tID:sample\tSM:sample\tPL:platform" ' + ref_data + ' ' + raw_set + ' > ' + self.directory + 'sample.mapped.sam'
        elif mode == "paired":
            raw_set1 = self.directory + raw_data[0]
            raw_set2 = self.directory + raw_data[1]
            activation = bwa + 'mem -t 1 -R "@RG\tID:sample\tSM:sample\tPL:platform" ' + ref_data + ' ' + raw_set1 + ' ' + raw_set2 + ' > ' + self.directory + 'sample.mapped.sam'

        return activation

