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
    
    
#
# add arguments, code and a return value to the function below
#

def convert_type_to_int(_____, ______, ______):
    # Add your code here
    #
    #
    #
    return ______


# 
# The below code will show if the function works
# don't forge to add the appropriate arguments
#

pop_density = load_formatted_frame("../../data/population_density_2019.csv")
locations = load_formatted_frame("../../data/locations.csv")

pop_density_single_code = access_country_code(pop_density)

# Using the conversion function created
population_density_correct_types = convert_type_to_int(pop_density_single_code)
locations_correct_types = convert_type_to_int(locations)

print(population_density_correct_types.dtypes)
print(locations_correct_types.dtypes)








