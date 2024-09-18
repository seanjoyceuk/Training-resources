import pandas as pd

# Import our required modules
import input_output
import analysis
import manipulation
import joins




def get_analyse_output(pop_density_filepath, location_filepath, output_filepath):
    """
    Access the data, run the analysis of population density means over locations,
    output the data into a csv.
    """

    pop_density = input_output.load_formatted_frame(pop_density_filepath)
    locations = input_output.load_formatted_frame(location_filepath)
    
    
    # Added module names below
    pop_density_single_code = manipulation.access_country_code(pop_density)
    
    
    pop_density_correct_types = manipulation.convert_type_to_int(dataframe=pop_density_single_code,
                                                                 column_name="country_code",
                                                                 string_value="CC")
                                                    
    locations_correct_types = manipulation.convert_type_to_int(dataframe=locations,
                                                               column_name="location_id",
                                                               string_value='"')
    
    population_location = joins.join_frames(left_dataframe=pop_density_correct_types,
                                                   right_dataframe=locations_correct_types,
                                                   left_column="country_code",
                                                   right_column="location_id")
    
    # Added module name here
    aggreagation = analysis.aggregate_mean(dataframe=population_location,
                                           groupby_column="sdg_region_name",
                                           aggregate_column="population_density")
                                  
    formatted_statistic = analysis.format_frame(aggreagation, "mean_population_density")
    
    # output_filepath == True if not False
    if output_filepath:
        input_output.write_output(formatted_statistic, output_filepath=output_filepath)
    
    return formatted_statistic
    
    
    
def combined_analysis(population_filepaths, location_filepath, output_filepath):
    """Function to perform population density mean analysis across multiple files"""
    
    loaded_dataframes = []
    for population_file in population_filepaths:
        # The year is given at the end of the file path, but before '.csv'
        path_end = population_file.split("_")[-1]
        year = path_end[:4]
        
        year_analysis = get_analyse_output(population_file, location_filepath, output_filepath=False)
        
        # Change the column name to the year of the population density
        formatted_year_analysis = manipulation.column_name_year(year_analysis, "mean_population_density", year)

        loaded_dataframes.append(formatted_year_analysis)
        
    combined_dataframes = joins.join_years(loaded_dataframes, join_column="sdg_region_name")
    
    if output_filepath:
        input_output.write_output(combined_dataframes, output_filepath=output_filepath)
    
    return combined_dataframes
    
    
    
    
if __name__ == "__main__":
    pop_path_2017 = "../../../../data/population_density_2017.csv"
    pop_path_2018 = "../../../../data/population_density_2018.csv"
    pop_path_2019 = "../../../../data/population_density_2019.csv"
    pop_path_2020 = "../../../../data/population_density_2020.csv"

    location_path = "../../../../data/locations.csv"

    # Demonstration of final output for case study
    print(combined_analysis([pop_path_2017, pop_path_2018, pop_path_2019, pop_path_2020], 
                            location_path, 
                            output_filepath=False))
