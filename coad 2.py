import pandas as pd
maf_data = pd.read_csv('C:/mafout2/out2/2615ab19-6065-42fa-9a9b-e4dc20f85376.wxs.aliquot_ensemble_masked.maf', sep='\t', comment='#', low_memory=False)
print(maf_data.head())
relevant_columns = ['Hugo_Symbol', 'Variant_Classification', 'Variant_Type']
maf_filtered = maf_data[relevant_columns]
mutation_counts = maf_filtered['Variant_Type'].value_counts()
print(mutation_counts)

filtered_data = maf_data[maf_data['Variant_Type'] == 'SNP']
print(filtered_data)




# Create a cross-tabulation of mutation types and variant classifications
cross_tab = pd.crosstab(filtered_data['Variant_Type'], filtered_data['Variant_Classification'])
print(cross_tab)


mutation_types = ['SNP', 'Deletion', 'Insertion']
picked_data = maf_data[maf_data['Variant_Type'].isin(mutation_types)]
print(picked_data)

mutation_count = picked_data['Hugo_Symbol'].value_counts()
print(mutation_count)


top_5_genes = mutation_count.nlargest(5)
print(top_5_genes)


import matplotlib.pyplot as plt

# Assuming you have already calculated the mutation count per gene and stored it as a Pandas Series called `mutation_count`

# Create a bar plot of mutation count by gene
plt.figure(figsize=(10, 6))
top_5_genes.plot(kind='bar')
plt.xlabel('Hugo_Symbol')
plt.ylabel('Mutation Count')
plt.title('Mutation Count by Gene')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
