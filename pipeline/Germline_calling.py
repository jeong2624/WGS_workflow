#!/usr/bin/env python
# chmod +x /home/pjw/Workspace/NGS/DNA_seq/pipeline/Germline_calling.py

import os
class Germline_calling:
    def __init__(self, directory, ref_name):
        self.directory = directory
        self.ref_name = ref_name

    def HaplotypeCaller(self, recal_bam_file):
        self.recal_bam_file = recal_bam_file
        ref_data = self.directory + self.ref_name
        gatk = "/home/pjw/tools/gatk-4.1.8.1/gatk "

        activation = gatk + "HaplotypeCaller -R " + ref_data + " -I " + self.directory + recal_bam_file + " -O " + self.directory + "sample.g.vcf -ERC GVCF"
        return activation

    def GenotypeGVCFs(self, vcf_file):
        self.vcf_file = vcf_file
        ref_data = self.directory + self.ref_name
        gatk = "/home/pjw/tools/gatk-4.1.8.1/gatk "

        activation = gatk + "GenotypeGVCFs -R " + ref_data + " -V " + self.directory + vcf_file + " -O " + self.directory + "sample.vcf"
        return activation
