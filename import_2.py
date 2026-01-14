import csv

# Load immune GO pairs
immune_go = []
with open("fbgn_immune_go_pairs.txt") as f:
    reader = csv.reader(f, delimiter="\t")
    for row in reader:
        fbgn, go_term = row
        immune_go.append((fbgn, go_term))

# Load isoform annotations into a dict keyed by FBgn
isoforms = {}
with open("Longest_isoforms_whole_genome_annotated_10_14.tsv") as f:
    reader = csv.DictReader(f, delimiter="\t")
    for row in reader:
        fbgn = row["FBgn_ID"]
        isoforms[fbgn] = row

# Write merged output
with open("Immune_longest_isoforms_per_GO.tsv", "w", newline='') as f_out:
    fieldnames = ["FBgn_ID", "FBtr_ID", "FBpp_ID", "Gene_Symbol", "Immune_GO_terms"]
    writer = csv.DictWriter(f_out, delimiter="\t", fieldnames=fieldnames)
    writer.writeheader()

    for fbgn, go_term in immune_go:
        if fbgn in isoforms:
            row = isoforms[fbgn].copy()
            row["Immune_GO_terms"] = go_term
            writer.writerow(row)