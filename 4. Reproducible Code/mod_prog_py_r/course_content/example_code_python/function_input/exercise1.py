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



#
# Adapt the function below to achieve the task set in exercise 1
# Remove the ____'s and fill them with appropriate variables
#

def access_country_code(______):
    # Write your code below
    #
    #
    #
    return ______


# Loading both data frames

pop_density = load_formatted_frame("../../data/population_density_2019.csv")
locations = load_formatted_frame("../../data/locations.csv")


# 
# Check your function works as expected with the code below
#

pop_density_single_code = access_country_code(______)
print(pop_density_single_code["country_code"])
                               
                               




