library(tidyr)
library(dplyr)
library(stringr)
library(readr)

## Code to be improved to complete exercise 3


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
                               into = c("country_code", "parent_code"), sep = "_")
  
  
  # Remove the  parent_code column, not used in later analysis
  dataframe <- dplyr::select(dataframe, everything(), -parent_code)
  
  return(dataframe)
}


#' Function to convert string to integer column type
convert_type_to_int <- function(dataframe, column_name, string_value) {
  
  # Convert country_code to integer by removing extra strings
  # Using dataframe$column_name to get a column won't work when the column name is a variable
  dataframe[[column_name]] <- stringr::str_remove_all(dataframe[[column_name]], pattern = string_value)
  
  # Convert type
  dataframe[[column_name]] <- as.integer(dataframe[[column_name]])
  
  return(dataframe)
}


#
# add arguments, code and a return value to the function below
#


join_frames <- function(________, ________, ________, _________) {
  # Add your code here
  #
  #
  #
  #
  return(_________)
}


# 
# The below code will show if the function works
# don't forge to add the appropriate arguments
#

## Run the functions created

pop_density <- load_formatted_frame("../../data/population_density_2019.csv")
locations <- load_formatted_frame("../../data/locations.csv")


pop_density_single_code <- access_country_code(pop_density)


pop_density_correct_types <- convert_type_to_int(dataframe=pop_density_single_code,
                                                column_name="country_code",
                                                string_value="CC")

locations_correct_types <- convert_type_to_int(dataframe=locations,
                                              column_name="location_id",
                                              string_value='"')

population_location <- join_frames(pop_density_correct_types,
                                   locations_correct_types,
                                   "country_code",
                                   "location_id")

print(colnames(population_location))
print(head(population_location, 10))
