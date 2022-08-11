#!/usr/bin/env python
# chmod +x /home/pjw/Workspace/NGS/DNA_seq/pipeline/Annotation.py

import os
class Annotation:
    def __init__(self, directory, vcf_name):
        self.directory = directory
        self.vcf_name = vcf_name

    def convert_avinput(self):
        convert =  "/home/pjw/tools/annovar/convert2annovar.pl "
        activation = convert + "-format vcf4 " + self.directory + self.vcf_name + " > " + self.directory + self.vcf_name.replace("vcf.gz", "avinput")
        return activation

    def Download_database(self, database, version):
        self.database = database
        self.version = version
        humandb = "/home/pjw/Workspace/NGS/DNA_seq/pipeline/humandb/"
        annotate = "/home/pjw/tools/annovar/annotate_variation.pl "

        activation = annotate + " -buildver " + version + " -downdb -webfrom annovar " + databse + " " + humandb
        return activation

    def gene_based(self, version, database):
        self.version = version
        self.database = database
        humandb = "/home/pjw/Workspace/NGS/DNA_seq/pipeline/humandb/"
        table = "/home/pjw/tools/annovar/table_annovar.pl "

        if "Annotation_result" in os.listdir(self.directory):pass
        else: os.chdir(self.directory); os.mkdir("Annotation_result")

        activation = table + self.directory + self.vcf_name + " " + humandb + " -buildver " + version + " -out " + self.directory + "Annotation_result/result -remove -protocol " + database + " -operation g -nastring . -vcfinput -polish"
        return activation

    def region_based(self, version):
        self.version = version
        humandb = "/home/pjw/Workspace/NGS/DNA_seq/pipeline/humandb/"
        table = "/home/pjw/tools/annovar/table_annovar.pl "

        if "Annotation_result" in os.listdir(self.directory):pass
        else: os.chdir(self.directory); os.mkdir("Annotation_result")

        activation = table + self.directory + self.vcf_name + " " + humandb + " -buildver " + version + " -out " + self.directory + "Annotation_result/result -remove -protocol " + database + " -operation r -nastring . -vcfinput -polish"
        return activation

    def filter_based(self, version):
        self.version = version
        humandb = "/home/pjw/Workspace/NGS/DNA_seq/pipeline/humandb/"
        table = "/home/pjw/tools/annovar/table_annovar.pl "

        if "Annotation_result" in os.listdir(self.directory):pass
        else: os.chdir(self.directory); os.mkdir("Annotation_result")

        activation = table + self.directory + self.vcf_name + " " + humandb + " -buildver " + version + " -out " + self.directory + "Annotation_result/result -remove -protocol " + database + " -operation f -nastring . -vcfinput -polish"
        return activation
