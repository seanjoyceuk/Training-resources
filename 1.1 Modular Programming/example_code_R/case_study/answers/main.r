library(tidyr)
library(dplyr)
library(stringr)
library(readr)

source("input_output.r")
source("analysis.r")
source("manipulation.r")
source("joins.r")




#' Access the data, run the analysis of population density means over locations,
#' output the data into a csv.
get_analyse_output <- function(pop_density_filepath, location_filepath, output_filepath) {
  
  pop_density <- load_formatted_frame(pop_density_filepath)
  locations <- load_formatted_frame(location_filepath)
  
  
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
  

  # output_filepath == True if not False
  if (output_filepath == TRUE) {
    write_output(formatted_statistic, output_filepath=output_filepath)
  }
  
  return(formatted_statistic)
}



#' Perform population density mean analysis across multiple files
combined_analysis <- function(population_filepaths, location_filepath, output_filepath) {
  

  loaded_dataframes = list()
  for (population_file in population_filepaths) {
    # The year is given at the end of the file path, but before '.csv'
    path_broken_up = stringr::str_split(population_file, pattern = "_")
    path_end = dplyr::last(dplyr::last(path_broken_up))
    
    year = substr(path_end, start = 1, stop = 4)

  
    year_analysis = get_analyse_output(population_file, location_filepath, output_filepath=FALSE)
  
    # Change the column name to the year of the population density
    formatted_year_analysis = column_name_year(year_analysis, "mean_population_density", year)
  
    
    loaded_dataframes[[length(loaded_dataframes) + 1]] <- formatted_year_analysis
    
  }

  combined_dataframes = join_years(loaded_dataframes, join_column="sdg_region_name")
  
  if (output_filepath != FALSE) {
    write_output(combined_dataframes, output_filepath=output_filepath)
  }
  
  return(combined_dataframes)
}


pop_path_2017 <- "../../../data/population_density_2017.csv"
pop_path_2018 <- "../../../data/population_density_2018.csv"
pop_path_2019 <- "../../../data/population_density_2019.csv"
pop_path_2020 <- "../../../data/population_density_2020.csv"

location_path <- "../../../data/locations.csv"

# Demonstration of final output for case study
final_output <- combined_analysis(list(pop_path_2017, pop_path_2018, pop_path_2019, pop_path_2020), 
                                  location_path, 
                                  output_filepath = FALSE)
print(final_output)