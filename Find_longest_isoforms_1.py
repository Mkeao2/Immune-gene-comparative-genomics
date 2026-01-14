#!/usr/bin/env python3

import csv
import re
from collections import defaultdict

# ------------------------
# INPUT FILES
# ------------------------
gff_file = "dmel-all-r6.57.gff"                        # FlyBase GFF3
longest_file = "Longest_isoforms_whole_genome_10_14.txt"
mapping_file = "Mapping_file_10_14.tsv"               # FBgn -> FBtr -> FBpp
annotation_file = "fbgn_annotation_ID_fb_2025_04.tsv" # FBgn -> Gene Symbol
output_file = "Longest_isoforms_whole_genome_annotated_10_14.tsv"

# ------------------------
# STEP 1: Parse longest isoforms file
# ------------------------
# This file already contains FBgn and FBtr pairs
longest_transcripts = {}
with open(longest_file) as f:
    for line in f:
        parts = line.strip().split("\t")
        if len(parts) < 2:
            continue
        fbgn, fbtr = parts[:2]
        longest_transcripts[fbtr] = fbgn  # map transcript to gene

# ------------------------
# STEP 2: Load FBgn-FBtr-FBpp mapping
# ------------------------
mapping = {}
with open(mapping_file) as f:
    reader = csv.reader(f, delimiter="\t")
    for row in reader:
        if len(row) < 3:
            continue
        fbgn_map, fbtr_map, fbpp = row[:3]  # take first 3 columns
        mapping[fbtr_map] = (fbgn_map, fbpp)

# ------------------------
# STEP 3: Load gene symbols
# ------------------------
gene_symbols = {}
with open(annotation_file) as f:
    reader = csv.reader(f, delimiter="\t")
    for row in reader:
        if not row or row[0].startswith("##") or len(row) < 3:
            continue
        symbol = row[0].strip()
        fbgn = row[2].strip()
        gene_symbols[fbgn] = symbol

# ------------------------
# STEP 4: Merge information and write annotated output
# ------------------------
with open(output_file, "w") as out:
    writer = csv.writer(out, delimiter="\t")
    writer.writerow(["FBgn_ID", "Gene_Symbol", "FBtr_ID", "FBpp_ID"])
    
    for fbtr, fbgn in longest_transcripts.items():
        # get FBgn and FBpp from mapping (if available)
        fbgn_map, fbpp = mapping.get(fbtr, (fbgn, ""))
        symbol = gene_symbols.get(fbgn_map, "")
        writer.writerow([fbgn_map, symbol, fbtr, fbpp])

print(f"✅ Annotated longest isoforms written to {output_file}")
