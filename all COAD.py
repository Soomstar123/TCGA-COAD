import pandas as pd
import numpy as np
import os

maf_folder = "C:/mafout2/allout/"
maf_files = [file for file in os.listdir(maf_folder) if file.endswith('.maf')]

dataframes = []
for maf_file in maf_files:
    filepath = os.path.join(maf_folder, maf_file)
    df = pd.read_csv(filepath, sep='\t', comment='#')
    dataframes.append(df)

merged_df = pd.concat(dataframes, ignore_index=True)

coad_df = merged_df[merged_df['Variant_Type'] == 'SNP']

# Filter mutations with high impact
high_impact_mutations = ['Frame_Shift_Del', 'Frame_Shift_Ins', 'Missense_Mutation']
high_impact_df = coad_df[coad_df['Variant_Classification'].isin(high_impact_mutations)]

gene_frequencies = high_impact_df['Hugo_Symbol'].value_counts()

# Identify frequently mutated genes
top_mutated_genes = gene_frequencies.head(10)

# Print the top 10 frequently mutated genes in COAD
print("Top 10 Frequently Mutated Genes in COAD:")
print(top_mutated_genes)


import matplotlib.pyplot as plt

# Calculate mutation frequencies of genes
gene_frequencies = high_impact_df['Hugo_Symbol'].value_counts()

# Identify frequently mutated genes
top_mutated_genes = gene_frequencies.head(10)

# Create a bar plot for visualization
plt.figure(figsize=(10, 6))
plt.bar(top_mutated_genes.index, top_mutated_genes.values)
plt.xlabel('Genes')
plt.ylabel('Frequency')
plt.title('Top 10 Frequently Mutated Genes in COAD')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()




