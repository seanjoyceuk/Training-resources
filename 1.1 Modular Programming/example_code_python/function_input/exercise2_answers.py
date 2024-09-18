import pandas as pd
import os

## Code to be improved to complete exercise 2

def load_formatted_frame(path_to_data):
    """Read csv and reformat column names"""
    formatted_path = os.path.join(path_to_data)
    # Load the csv from given path
    dataframe = pd.read_csv(formatted_path)
    
    # Clean the column names, following naming conventions similar to PEP8
    dataframe.columns = dataframe.columns.str.lower()
    dataframe.columns = dataframe.columns.str.replace(" ", "_")
    
    return dataframe


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


## Run the functions created

pop_density = load_formatted_frame("../../data/population_density_2019.csv")
locations = load_formatted_frame("../../data/locations.csv")


pop_density_single_code = access_country_code(pop_density)


pop_density_correct_types = convert_type_to_int(dataframe=pop_density_single_code,
                                                column_name="country_code",
                                                string_value="CC")
                                                
locations_correct_types = convert_type_to_int(dataframe=locations,
                                                column_name="location_id",
                                                string_value='"')

print(pop_density_correct_types.dtypes)
print(locations_correct_types.dtypes)







