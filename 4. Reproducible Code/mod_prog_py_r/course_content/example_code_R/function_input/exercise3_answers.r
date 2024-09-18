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

#' join the required frames on specified columns, 
#' dropping unecessary columns
join_frames <- function(left_dataframe, right_dataframe, left_column, right_column) {
  
  # Change location_id to be called country_code for join
  colnames(right_dataframe)[colnames(right_dataframe) == right_column] <- left_column
  
  combined_frames <- dplyr::left_join(x = left_dataframe,
                                      y = right_dataframe,
                                      by = left_column)

  combined_frames_reduced <- dplyr::select(combined_frames, sdg_region_name, population_density)

  return(combined_frames_reduced)
}


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
                                   left_column = "country_code",
                                   right_column = "location_id")

print(colnames(population_location))
print(head(population_location, 10))
