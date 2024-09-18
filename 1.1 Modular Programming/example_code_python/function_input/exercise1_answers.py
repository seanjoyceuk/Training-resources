import pandas as pd
import os

## Code to be improved to complete exercise 1

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
    
    # Copy the incoming data to prevent editing the original
    dataframe = dataframe.copy()
    
    dataframe[["country_code", "parent_code"]] = (dataframe["country_and_parent_code"]
                                                .str.split("_", expand=True))
                                                
    dataframe_dropped = dataframe.drop(labels=[
                                                 "country_and_parent_code",
                                                 "parent_code"
                                              ], axis=1)
    return dataframe_dropped
    

# Loading both data frames

pop_density = load_formatted_frame("../../data/population_density_2019.csv")
locations = load_formatted_frame("../../data/locations.csv")

  
pop_density_single_code = access_country_code(pop_density)
print(pop_density_single_code["country_code"])









