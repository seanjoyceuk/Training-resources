import pandas as pd
import os


def load_formatted_frame(path_to_data):
    """Read csv and reformat column names"""
    formatted_path = os.path.join(path_to_data)
    # Load the csv from given path
    dataframe = pd.read_csv(formatted_path)
    
    # Clean the column names, following naming conventions similar to PEP8
    dataframe.columns = dataframe.columns.str.lower()
    dataframe.columns = dataframe.columns.str.replace(" ", "_")
    
    return dataframe
    

def write_output(dataframe, output_filepath):
    """Function to write output statistic in formatted manner"""

    dataframe.to_csv(output_filepath, index=False, sep=",")
    
