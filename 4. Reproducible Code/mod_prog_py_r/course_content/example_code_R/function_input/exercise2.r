library(tidyr)
library(dplyr)
library(stringr)
library(readr)

## Code to be improved to complete exercise 2


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


#
# Adapt the function below to achieve the task set in exercise 1
# Remove the ____'s and fill them with appropriate variables
#


#' Function to split combined code columns 
#' and remove uncessary columns
access_country_code <- function(dataframe) {
  # The country_and_parent_code column needs to 
  # be split into two columns without the strings
  dataframe <- tidyr::separate(data = dataframe, col = country_and_parent_code,
                               into = c("country_code", "parent_code"), sep = "_")
  
  
  # Remove the  parent_code column, not used in later analysis
  dataframe <- dplyr::select(dataframe, everything(), -parent_code)
  
  return(dataframe)
}




#
# add arguments, code and a return value to the function below
#

convert_type_to_int <- function(_____, ______, ______) {
  # Add your code here
  #
  #
  #
  return(______)
}

# 
# The below code will show if the function works
# don't forget to add the appropriate arguments
#

pop_density <- load_formatted_frame("../../data/population_density_2019.csv")
locations <- load_formatted_frame("../../data/locations.csv")

pop_density_single_code <- access_country_code(pop_density)

# Using the conversion function created
population_density_correct_types <- convert_type_to_int(pop_density_single_code, ______, _______)
locations_correct_types <- convert_type_to_int(locations, _______, ________)

print(str(population_density_correct_types))
print(str(locations_correct_types))