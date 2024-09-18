import pandas as pd

# Import our required modules
import input_output
import analysis
import manipulation


def get_analyse_output(population_filepath,
                       locations_filepath,
                       output_filepath):
    """
    Access the data, run the analysis of population density means over locations,
    output the data into a csv.
    """

    pop_density = input_output.load_formatted_frame(population_filepath)
    locations = input_output.load_formatted_frame(locations_filepath)
    
    
    # Added module names below
    pop_density_single_code = manipulation.access_country_code(pop_density)
    
    
    pop_density_correct_types = manipulation.convert_col_to_int(dataframe=pop_density_single_code,
                                                                 col_name="country_code",
                                                                 string_pattern="CC")
                                                    
    locations_correct_types = manipulation.convert_col_to_int(dataframe=locations,
                                                               col_name="location_id",
                                                               string_pattern='"')
    
    population_location = manipulation.join_frames(left_dataframe=pop_density_correct_types,
                                                   right_dataframe=locations_correct_types,
                                                   left_column="country_code",
                                                   right_column="location_id")
    
    # Added module name here
    aggreagation = analysis.aggregate_mean(dataframe=population_location,
                                           groupby_column="sdg_region_name",
                                           statistic_column="population_density")
                                  
    formatted_statistic = analysis.format_frame(aggreagation, "mean_population_density")
    

    input_output.write_output(formatted_statistic, output_filepath = output_filepath)
    
    
    
get_analyse_output(population_filepath = "../data/population_density_2019.csv",
                   locations_filepath = "../data/locations.csv",
                   output_filepath = "../outputs/mean_population_density.csv")