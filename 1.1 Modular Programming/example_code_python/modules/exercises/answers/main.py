import pandas as pd

# Import our required modules
import input_output
import analysis
import manipulation





def get_analyse_output():
    """
    Access the data, run the analysis of population density means over locations,
    output the data into a csv.
    """

    pop_density = input_output.load_formatted_frame("../../../../data/population_density_2019.csv")
    locations = input_output.load_formatted_frame("../../../../data/locations.csv")
    
    
    # Added module names below
    pop_density_single_code = manipulation.access_country_code(pop_density)
    
    
    pop_density_correct_types = manipulation.convert_type_to_int(dataframe=pop_density_single_code,
                                                                 column_name="country_code",
                                                                 string_value="CC")
                                                    
    locations_correct_types = manipulation.convert_type_to_int(dataframe=locations,
                                                               column_name="location_id",
                                                               string_value='"')
    
    population_location = manipulation.join_frames(left_dataframe=pop_density_correct_types,
                                                   right_dataframe=locations_correct_types,
                                                   left_column="country_code",
                                                   right_column="location_id")
    
    # Added module name here
    aggreagation = analysis.aggregate_mean(dataframe=population_location,
                                           groupby_column="sdg_region_name",
                                           aggregate_column="population_density")
                                  
    formatted_statistic = analysis.format_frame(aggreagation, "mean_population_density")
    

    input_output.write_output(formatted_statistic, output_filepath="./mean_pop_density.csv")
    
    
    
if __name__ == "__main__":
    get_analyse_output()
