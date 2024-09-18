library(tidyr)
library(dplyr)
library(stringr)
library(readr)

## Code to be improved to complete exercise 1


#' Read population data and reformat column names
load_formatted_frame <- function(path_to_data) {
  # Load the population density data 2019
  formatted_path <- file.path(path_to_data)
  dataframe <- readr::read_csv(formatted_path)
  
  # Clean the column names, following snake_case convention
  colnames(dataframe) <- tolower(colnames(dataframe))
  colnames(dataframe) <- stringr::str_replace_all(colnames(dataframe), pattern = " ", replacement = "_")
  
  return(dataframe)
}


#' Function to split combined code columns 
#' and remove uncessary columns
access_country_code <- function(dataframe) {
  # The country_and_parent_code column needs to 
  # be split into two columns without the strings
  dataframe <- tidyr::separate(data = dataframe, col = country_and_parent_code,
                               into = c("country_code", "parent_code"), 
                               sep = "_")
  
  # Remove the  parent_code column, not used in later analysis
  dataframe <- dplyr::select(dataframe, everything(), -parent_code)
  
  return(dataframe)
}


# Loading both data frames
population_density <- load_formatted_frame("../../data/population_density_2019.csv")
locations <- load_formatted_frame("../../data/locations.csv")

# Run the code created checking output
pop_density_single_code <- access_country_code(population_density)
print(pop_density_single_code$country_code)
