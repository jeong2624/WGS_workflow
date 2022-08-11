#!/usr/bin/env python
# chmod +x /home/pjw/Workspace/NGS/DNA_seq/Basic_step.py
# Running code : /home/pjw/Workspace/NGS/DNA_seq/Basic.py /home/pjw/Workspace/NGS/DNA_seq/(germline or somatic)

import sys; import os; import subprocess as sub
sys.path.append("/home/pjw/Workspace/NGS/DNA_seq/")

directory = sys.argv[1]
ref_name = "hg38.chr21.fa"
known_vcf_site = "hg38_v0_Homo_sapiens_assembly38.known_indels.chr21.vcf.gz"

# Quality Control.
import pipeline.Quality_Control as QC

QC_step = QC.Quality(directory)

fastqc = QC_step.fastqc("sample_fastq"); sub.call(fastqc, shell = True)

# Alignment.
import pipeline.Alignment as Align

Align_step = Align.Alignment(directory, ref_name)

Alignment = Align_step.bwa_mem("paired"); sub.call(Alignment, shell = True)

# Mark Duplication
import pipeline.samtools as sam

samtool = sam.samtools(directory)

sam_to_bam = samtool.conversion("sample.mapped.sam"); sub.call(sam_to_bam, shell = True)

fixmate = samtool.fixmate("sample.mapped.bam"); sub.call(fixmate, shell = True)

sort_bam = samtool.sorting("sample.fixmate.bam"); sub.call(sort_bam, shell = True)

markdup = samtool.markdup("sample.fixmate.sorted.bam"); sub.call(markdup, shell = True)

bam_index = samtool.bam_index("sample.markdup.bam"); sub.call(bam_index, shell = True)

# Base Recalibration
import pipeline.Recalibrate_base as recal

gatk = recal.Recalibrate_base(directory, ref_name)

vcf_index = gatk.Index_feature(known_vcf_site); sub.call(vcf_index, shell = True)

Recalibration = gatk.Recalibrator("sample.markdup.bam", known_vcf_site); sub.call(Recalibration, shell = True)

ApplyBQSR = gatk.ApplyBQSR("sample.markdup.bam", "sample.recal_data.table"); sub.call(ApplyBQSR, shell = True)
