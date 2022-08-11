#!/usr/bin/env python
# chmod +x /home/pjw/Workspace/NGS/DNA_seq/Somatic.py
# Running code : /home/pjw/Workspace/NGS/DNA_seq/Somatic.py /home/pjw/Workspace/NGS/DNA_seq/somatic/

import sys; import os; import subprocess as sub
sys.path.append("/home/pjw/Workspace/NGS/DNA_seq/")

directory = sys.argv[1]
ref_name = "Homo_sapiens_assembly38.fasta"
population_germline = "chr17_af-only-gnomad_grch38.vcf.gz"

# Variant Calling
import pipeline.Somatic_calling as Soma

Call = Soma.Somatic_calling(directory, ref_name)

Mutect2 = Call.Mutect2_match(population_germline); sub.call(Mutect2, shell = True)

Filter = Call.FilterMutectCalls("somatic.vcf.gz"); sub.call(Filter, shell = True)

# Annotation
import pipeline.Annotation as Anno

Anno_step = Anno.Annotation(directory, "somatic_filtered.vcf.gz")

gene_annotation = Anno_step.gene_based("hg38", "knownGene"); sub.call(gene_annotation, shell = True)

#region_annotation = Anno_step.region_based("hg38", "knownGene"); sub.call(region_annotation, shell = True)

#filter_annotation = Anno_step.filter_based("hg38", "knownGene"); sub.call(filter_annotation, shell = True)
