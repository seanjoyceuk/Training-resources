# File to analyse the mean population density data from the UN

# Import relevant libraries for analysis
library(tidyr)
library(dplyr)
library(stringr)
library(readr)

# Load the population density data 2019
population_path <- file.path("../../data/population_density_2019.csv")
pop_density <- readr::read_csv(population_path)

# Clean the column names, following snake_case convention
colnames(pop_density) <- tolower(colnames(pop_density))
colnames(pop_density) <- stringr::str_replace_all(colnames(pop_density), pattern = " ", replacement = "_")


# The country_and_parent_code column needs to 
# be split into two columns without the strings
pop_density <- tidyr::separate(data = pop_density, col = country_and_parent_code,
                               into = c("country_code", "parent_code"), 
                               sep = "_")


# Remove the  parent_code column, not used in later analysis
pop_density <- dplyr::select(pop_density, everything(), -parent_code)

# Convert country_code to integer by removing strings
pop_density$country_code <- stringr::str_remove_all(pop_density$country_code, pattern = "CC")
pop_density$country_code <- as.integer(pop_density$country_code)


# Load the locations data to get the Sustainable Development Goals sub regions
locations_path <- file.path("../../data/locations.csv")
locations <- readr::read_csv(locations_path)

# Clean the column names, following naming conventions similar to PEP8
colnames(locations) <- tolower(colnames(locations))
colnames(locations) <- stringr::str_replace_all(colnames(locations), pattern = " ", replacement = "_")

# The location_id data has quotation marks making it a string,
# it needs to be converted to a numeric
locations$location_id <- stringr::str_remove_all(locations$location_id, pattern = '"')
locations$location_id <- as.integer(locations$location_id)


# Change location_id to be called country_code for join
colnames(locations)[colnames(locations) == "location_id"] <- "country_code"

# Join the data sets
# Left merge so we keep all pop_density data
pop_density_location <- dplyr::left_join(pop_density,
                                         locations,
                                         by = "country_code")


# Get just the relevant columns in preparation
# for the following groupby
region_density <- dplyr::select(pop_density_location, sdg_region_name, population_density)

# Calculate the mean population density for each region
# A non-weighted mean

region_density_grouped <- dplyr::group_by(region_density, sdg_region_name)

region_mean_density <- dplyr::summarise(region_density_grouped,
                                        "mean_population_density" = mean(population_density)
                                        )

# Sort the data for clearer reading, descending order
region_mean_density <- dplyr::arrange(region_mean_density,  -mean_population_density)

# Round mean density for clearer reading
region_mean_density$mean_population_density <- round(region_mean_density$mean_population_density,
                                                     digits = 2)

# Write out the final output
readr::write_csv(x = region_mean_density, file = "mean_population_density_output.csv")