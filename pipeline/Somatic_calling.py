#!/usr/bin/env python
# chmod +x /home/pjw/Workspace/NGS/DNA_seq/pipeline/Somatic_calling.py

import os
class Somatic_calling:
    def __init__(self, directory, ref_name):
        self.directory = directory
        self.ref_name = ref_name

    def Mutect2_match(self, population_germline):
        self.population_germline = population_germline

        bam_file = filter(lambda x: ".bam" in x, os.listdir(self.directory))
        normal_data = filter(lambda x: "normal" in x, bam_file)
        tumor_data = filter(lambda x: "tumor" in x, bam_file)
        ref_data = self.directory + self.ref_name
        gatk = "/home/pjw/tools/gatk-4.1.8.1/gatk "
        
        normal = ""; tumor = ""
        for i in normal_data:
            normal += "-I " + self.directory + i + " "
        
        for j in tumor_data:
            tumor += "-I " + self.directory + j + " "
        
        if population_germline:
            activation = gatk + "Mutect2 -R " + ref_data + " " + normal + tumor + "--germline-resource " + self.directory + population_germline + "--ignore-itr-artifacts -O " + self.directory + "somatic.vcf.gz"
        else:
            activation = gatk + "Mutect2 -R " + ref_data + " " + normal + tumor + "--ignore-itr-artifacts -O " + self.directory + "somatic.vcf.gz"
        return activation

    def Mutect2_single(self, bam_file):
        self.bam_file = bam_file
        ref_data = self.directory + self.ref_name
        gatk = "/home/pjw/tools/gatk-4.1.8.1/gatk "
        
        activation = gatk + "Mutect2 -R " + ref_data + " -I " + self.directory + bam_file + " -O " + self.directory + "somatic.vcf.gz"
        return activation

    def FilterMutectCalls(self, somatic_vcf):
        self.somatic_vcf = somatic_vcf
        ref_data = self.directory + self.ref_name
        gatk = "/home/pjw/tools/gatk-4.1.8.1/gatk "

        activation = gatk + "FilterMutectCalls -R " + ref_data + " -V " + self.directory + somatic_vcf + " -O " + self.directory + "somatic_filtered.vcf.gz"
        return activation

