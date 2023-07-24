library(readr)
library(dplyr)
# Replace "path_to_maf_files" with the directory path where your MAF files are located.
# For example, "C:/TCGA_MAF_Files/" or "~/Documents/TCGA_MAF_Files/"
maf_files <- list.files(path = "c:/mafout2/allout/", pattern = "*.maf", full.names = TRUE)
maf_data_list <- lapply(maf_files, read_delim, delim = "\t", col_names = TRUE, comment = "#")

str(maf_data_list)
install.packages("purrr")
library(purrr)
map(maf_data_list, colnames)
library(dplyr)
merged_maf_data <- do.call(rbind, maf_data_list)
# Save the merged and filtered data frame as a new MAF file
write_delim(merged_maf_data, path = "c:/mafout2/outt/merged_filtered_maf.maf", delim = "\t")
library(maftools)
# Replace "path_to_merged_maf.maf" with the actual path to your merged MAF file
maf_data <- read.maf("c:/mafout2/outt/merged_filtered_maf.maf")
summary(maf_data)
####################

clinical_data <- read_tsv("C:/mafout2/outt/coadread_tcga_pan_can_atlas_2018_clinical_data.tsv")
summary(clinical_data)


#library(readr)
#library(dplyr)
#somatic_maf_data <- read.maf("c:/mafout2/outt/merged_filtered_maf.maf")
#clinical_data <- read_tsv("C:/mafout2/outt/coadread_tcga_pan_can_atlas_2018_clinical_data.tsv")
library(maftools)
maf_data <- read.delim("c:/mafout2/outt/merged_filtered_maf.maf", sep = "\t")
maf_data[1:2, ]


