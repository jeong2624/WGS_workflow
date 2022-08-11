#!/usr/bin/env python
# chmod +x /home/pjw/Workspace/NGS/DNA_seq/Germline.py
# Running code : /home/pjw/Workspace/NGS/DNA_seq/Germline.py /home/pjw/Workspace/NGS/DNA_seq/germline/

import sys; import os; import subprocess as sub
sys.path.append("/home/pjw/Workspace/NGS/DNA_seq/")

directory = sys.argv[1]
ref_name = "hg38.chr21.fa"
known_vcf_site = "hg38_v0_Homo_sapiens_assembly38.known_indels.chr21.vcf.gz"
"""
# Variant Calling
import pipeline.Germline_calling as Germ

Call = Germ.Germline_calling(directory, ref_name)

haplot = Call.HaplotypeCaller("sample.recal.bam"); sub.call(haplot, shell = True)

Genotype = Call.GenotypeGVCFs("sample.g.vcf"); sub.call(Genotype, shell = True)
"""
# Annotation
import pipeline.Annotation as Anno

Anno_step = Anno.Annotation(directory, "sample.vcf")

gene_annotation = Anno_step.gene_based("hg38", "knownGene"); sub.call(gene_annotation, shell = True)

#region_annotation = Anno_step.region_based("hg38", "knownGene"); sub.call(region_annotation, shell = True)

#filter_annotation = Anno_step.filter_based("hg38", "knownGene"); sub.call(filter_annotation, shell = True)

