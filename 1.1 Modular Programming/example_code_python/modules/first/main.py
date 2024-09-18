import pandas as pd


def access_country_code(dataframe):
    """Function to split combined code columns and remove uncessary columns"""
    
    dataframe = dataframe.copy()
    
    dataframe[["country_code", "parent_code"]] = (dataframe["country_and_parent_code"]
                                                .str.split("_", expand=True))
                                                
    dataframe_dropped = dataframe.drop(labels=[
                                                "country_and_parent_code",
                                                "parent_code"
                                              ], axis=1)
    return dataframe_dropped  
    


def convert_type_to_int(dataframe, column_name, string_value):
    """Function to convert string to integer column type"""
    
    dataframe = dataframe.copy()
    
    dataframe[column_name] = dataframe[column_name].str.replace(string_value, "")
    
    dataframe[column_name] = dataframe[column_name].astype(int)
    
    return dataframe


def join_frames(left_dataframe, right_dataframe, left_column, right_column):
    """
    Function to join the required frames on specified columns, dropping
    unrecessary column
    """
    
    left_dataframe = left_dataframe.copy()
    right_dataframe = right_dataframe.copy()
    
    combined_frames = left_dataframe.merge(right=right_dataframe,
                                           how="left",
                                           left_on=left_column,
                                           right_on=right_column)
                                           
    combined_frames_reduced = combined_frames.drop(labels=[right_column], axis=1)
    
    return combined_frames_reduced


def aggregate_mean(dataframe, groupby_column, aggregate_column):
    """Function to groupby and calculate the aggregate mean of two columns"""
    
    dataframe = dataframe.copy()
    
    # Remove unecessary columns
    subset = dataframe[[groupby_column, aggregate_column]]
    
    # Perform mean calculation
    statistic = (subset.groupby(groupby_column, as_index=False)
                       .agg({aggregate_column: "mean"}))
                       
    statistic_renamed = statistic.rename(columns={aggregate_column: "mean_" + aggregate_column})
  
    return statistic_renamed
    
    
    
def format_frame(dataframe, statistic_column):
    """Function to format the dataframe for output"""
    
    dataframe = dataframe.copy()
    
    dataframe_sorted = dataframe.sort_values(by=statistic_column,
                                             ascending=False)
                                      
    dataframe_sorted[statistic_column] = dataframe_sorted[statistic_column].round(2)
    
    return dataframe_sorted
    
    



def get_analyse_output():
    """
    Access the data, run the analysis of population density means over locations,
    output the data into a csv.
    """
    
    pop_density = load_formatted_frame("../../data/population_density_2019.csv")
    locations = load_formatted_frame("../../data/locations.csv")
    
    
    pop_density_single_code = access_country_code(pop_density)
    
    
    pop_density_correct_types = convert_type_to_int(dataframe=pop_density_single_code,
                                                    column_name="country_code",
                                                    string_value="CC")
                                                    
    locations_correct_types = convert_type_to_int(dataframe=locations,
                                                  column_name="location_id",
                                                  string_value='"')
    
    population_location = join_frames(left_dataframe=pop_density_correct_types,
                                       right_dataframe=locations_correct_types,
                                       left_column="country_code",
                                       right_column="location_id")
    
    aggreagation = aggregate_mean(dataframe=population_location,
                                  groupby_column="sdg_region_name",
                                  aggregate_column="population_density")
                                  
    formatted_statistic = format_frame(aggreagation, "mean_population_density")
    
    write_output(formatted_statistic, output_filepath="./mean_pop_density.csv")
    
    
    
if __name__ == "__main__":
    get_analyse_output()
