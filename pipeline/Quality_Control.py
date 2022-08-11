#!/usr/bin/env python
# chmod +x /home/pjw/Workspace/NGS/DNA_seq/pipeline/Quality_Control.py

import os

class Quality:
    def __init__(self, directory):
        self.directory = directory

    def fastqc(self, output_name):
        self.output_name = output_name
        raw_data = self.directory + "*.fastq.gz"
        output = self.directory + output_name

        if output_name in os.listdir(self.directory): 
            pass
        else: 
            os.chdir(self.directory)
            os.mkdir(output_name)
        
        activation = "fastqc -o " + output + " " + raw_data
        return activation
    
 
    def sickle(self, mode, platform):
        self.mode = mode
        self.platform = platform

        if mode == "single":
            raw_data = self.directory + filter(lambda x: ".fastq.gz" in x, os.listdir(self.directory))[0]
            activation = "sickle se -f " + raw_data + " -t " + platform + " -o " + self.directory + "trimmed_output_file.fastq"
        elif mode == "paired":
            raw_data1 = self.directory + filter(lambda x: self.file_format in x, os.listdir(self.directory))[0]
            raw_data2 = self.directory + filter(lambda x: self.file_format in x, os.listdir(self.directory))[1]
            activation = "sickle pe -f " + raw_data1 + " -r " + raw_data2 + " -t " + platform + " -o " + self.directory + "trimmed_output_file1.fastq -p " + self.directory + "trimmed_output_file2.fastq -s " + self.directory + "trimmed_singles_file.fastq"
        return activation

