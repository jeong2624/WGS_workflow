#!/usr/bin/env python
# chmod +x /home/pjw/Workspace/NGS/DNA_seq/Supplementary_step.py
# Running code : /home/pjw/Workspace/NGS/DNA_seq/Supplementary_step.py /home/pjw/Workspace/NGS/DNA_seq/(germline or somatic)

import sys; import os; import subprocess as sub
sys.path.append("/home/pjw/Workspace/NGS/DNA_seq/")

Answer = raw_input("What do you want? Trimming / Samtools")
directory = sys.argv[1]
ref_name = "hg38.chr21.fa"

# Trimming step
if Answer == "Trimming":
    import pipeline.Quality_Control as QC

    Trimming_step = QC.Quality(directory)

    sickle = Trimming_step.sickle("paired", "sanger"); sub.call(sickle, shell = True)

# Samtools
else:
    import pipeline.samtools as sam

    samtool = sam.samtools(directory)

    sort_bam = samtool.sorting("sample.mapped.bam"); sub.call(sort_bam, shell = True)

    bam_index = samtool.bam_index("sample.mapped.bam"); sub.call(bam_index, shell = True)

    fasta_dict = samtool.fasta_dict(self, ref_name); sub.call(fasta_dict, shell = True)


