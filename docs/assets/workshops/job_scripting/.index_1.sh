#!/bin/bash -e

set -u

# Reference genome indexing, once for all samples.
ref_genome=ref_genome/ecoli_rel606.fasta

gunzip -kf ${ref_genome}.gz
bwa-mem2 index ${ref_genome}
