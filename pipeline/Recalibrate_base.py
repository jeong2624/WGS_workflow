#!/usr/bin/env python
# chmod +x /home/pjw/Workspace/NGS/DNA_seq/pipeline/Recalibrate_base.py

import os
class Recalibrate_base:
    def __init__(self, directory, ref_name):
        self.directory = directory
        self.ref_name = ref_name

    def Index_feature(self, known_site_vcf_file):
        self.known_site_vcf_file = known_site_vcf_file
        gatk = "/home/pjw/tools/gatk-4.1.8.1/gatk "
        activation = gatk + "IndexFeatureFile -I " + self.directory + known_site_vcf_file
        return activation

    def Recalibrator(self, bam_file, known_site_vcf_file):
        self.bam_file_name = bam_file
        self.knwon_site_vcf_file = known_site_vcf_file
        ref_data = self.directory + self.ref_name
        gatk = "/home/pjw/tools/gatk-4.1.8.1/gatk "

        activation = gatk + "BaseRecalibrator -I " + self.directory + bam_file + " -R " + ref_data + " --known-sites " + self.directory + known_site_vcf_file + " -O " + self.directory + "sample.recal_data.table"
        return activation

    def ApplyBQSR(self, bam_file, recal_table_file):
        self.bam_file = bam_file
        self.recal_table_file = recal_table_file
        ref_data = self.directory + self.ref_name
        gatk = "/home/pjw/tools/gatk-4.1.8.1/gatk "
        
        activation = gatk + "ApplyBQSR -R " + ref_data + " -I " + self.directory + bam_file + " --bqsr-recal-file " + self.directory + recal_table_file + " -O " + self.directory + "sample.recal.bam"
        return activation

