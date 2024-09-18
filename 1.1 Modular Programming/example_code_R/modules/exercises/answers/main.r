library(tidyr)
library(dplyr)
library(stringr)
library(readr)

source("input_output.r")
source("analysis.r")
source("manipulation.r")




#' Access the data, run the analysis of population density means over locations,
#' output the data into a csv.
get_analyse_output <- function() {
  
  pop_density <- load_formatted_frame("../../../../data/population_density_2019.csv")
  locations <- load_formatted_frame("../../../../data/locations.csv")
  
  
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