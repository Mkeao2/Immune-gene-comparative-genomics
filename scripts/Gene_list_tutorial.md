**Steps to get gene list:**

1. Download the full transcript (gmel-all-r6.65.gff), current annotation (fbgn_annotation_ID_fb_2025_04.tsv), mapping (fbgn_fbtr_fbpp_fb_2025_04.tsv), and GO terms for all genes (gene_association.fb.gz) files from FlyBase FTP. Files only include the longest isoforms for protein-coding genes - so no non-coding genes (e.g., miRNAs, lncRNAs, snoRNAs).  
3. Match the longest isoform gene names with gene symbol, transcript ID and protein ID (file 1).
5. Run the following to get a list of genes with all immune associated GO terms (file 2). 

```
grep -E 'GO:0002376|GO:0006955|GO:0045087|GO:0002757|GO:0006952|GO:0050830|GO:0050829|GO:0002252|GO:0002224|GO:0009617|GO:0002253|GO:0002221|GO:0002225|GO:0019730 
```

6. Extract only FBgns and GO columns from this list (file 3).
7. Merge files 1 and 3 to get a list with columns FBgn_ID, FBtr_ID, FBpp_ID and Gene_Symbol. 
