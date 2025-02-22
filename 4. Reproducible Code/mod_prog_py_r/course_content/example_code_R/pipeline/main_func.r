library(tidyr)
library(dplyr)
library(stringr)
library(readr)



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
  dataframe[column_name] <- stringr::str_remove_all(dataframe[[column_name]], pattern = string_value)
  
  # Convert type
  dataframe[column_name] <- as.integer(dataframe[[column_name]])
  
  return(dataframe)
}

#' Join the required frames on specified columns, 
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


#' Function to groupby and calculate the mean of two columns
aggregate_mean <- function(dataframe, groupby_column, statistic_column) {
  
  # Perform aggregation and summary
  
  # Use group_by_ because of variable column name
  region_mean_density_grouped <- group_by_(.data = dataframe, groupby_column)
  
  # use get() to access column name
  region_mean_density <- dplyr::summarise(.data = region_mean_density_grouped,
                                          "mean_population_density" = mean(get(statistic_column)))
  
  return(region_mean_density)
}


#' Format the dataframe for output
format_frame <- function(dataframe, statistic_column) {
  
  # Sort the data for clearer reading, descending order
  dataframe_sorted <- dplyr::arrange(.data = dataframe)
  
  # Round mean density for clearer reading
  dataframe_sorted[statistic_column] <- round(dataframe_sorted[statistic_column],
                                              digits = 2)
  
  return(dataframe_sorted)
}

#' write output statistic in formatted manner
write_output <- function(dataframe, output_filepath) {
  
  readr::write_csv(x = dataframe, path = output_filepath)
  
}


#' Access the data, run the analysis of population density means over locations,
#' output the data into a csv.
get_analyse_output <- function() {
  
  pop_density <- load_formatted_frame("../../data/population_density_2019.csv")
  locations <- load_formatted_frame("../../data/locations.csv")
  
  
  pop_density_single_code <- access_country_code(pop_density)
  
  
  pop_density_correct_types <- convert_type_to_int(dataframe = pop_density_single_code,
                                                   column_name = "country_code",
                                                   string_value = "CC")
  
  locations_correct_types <- convert_type_to_int(dataframe = locations,
                                                 column_name = "location_id",
                                                 string_value = '"')
  
  population_location <- join_frames(pop_density_correct_types,
                                     locations_correct_types,
                                     left_column = "country_code",
                                     right_column = "location_id")
  
  aggreagation <- aggregate_mean(dataframe = population_location,
                                 groupby_column = "sdg_region_name",
                                 statistic_column = "population_density")
  
  formatted_statistic <- format_frame(aggreagation, "mean_population_density")
  
  write_output(formatted_statistic, "./mean_pop_density.csv")
  
}


## Run the main function created

get_analyse_output()
