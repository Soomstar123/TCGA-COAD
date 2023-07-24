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

#절취선
# Filter mutations with high impact
# Co-occurring mutations
co_occurring_mutations = merged_df.groupby(['Tumor_Seq_Allele1', 'Tumor_Seq_Allele2']).size().reset_index(name='Count')
co_occurring_mutations.sort_values('Count', ascending=False, inplace=True)

# Co-occurring genes
co_occurring_genes = merged_df.groupby(['TTN', 'TP53']).size().reset_index(name='Count')
co_occurring_genes.sort_values('Count', ascending=False, inplace=True)


###































