#!/bin/bash

# Move and rename downloaded files  

path_to_downloads="/Users/scampione/Downloads/RP_paralogs_protein_batch"
destination_path="/Volumes/ZhouLab/Sam/RP_paralogs_batch/RP_paralogs_protein_batch"

# Rename files and change to .dnas 
orig_names_gDNA=$(ls $path_to_downloads | sed "s/_protein.fsa//g")
for orig_name in $orig_names_gDNA
do
    new_name=$(echo $orig_name | sed "s/^.*RP/RP/g")
    mv "${path_to_downloads}/${orig_name}_protein.fsa" "${path_to_downloads}/${new_name}_protein.dnas"
done

# Get names of type A paralogs, iterate through to place in the pairs' shared directory 
A_genes=$(ls $path_to_downloads | grep A | sed 's/_.*//')
for gene in $A_genes
do
  base_name=$(echo $gene | sed "s/A//g")  # Create the directory for gene
  mkdir -p "${path_to_downloads}/${base_name}_protein"
  
  mv "${path_to_downloads}/${gene}_protein.dnas" "${path_to_downloads}/${base_name}_protein/"
done

# Get names of type B paralogs, iterate through to place in the pairs' shared directory 
B_genes=$(ls $path_to_downloads | grep B | sed 's/_.*//')
for gene in $B_genes
do
  base_name=$(echo $gene | sed "s/B//g")
  
  mv "${path_to_downloads}/${gene}_protein.dnas" "${path_to_downloads}/${base_name}_protein/"
done

echo "Directories created and files moved."

