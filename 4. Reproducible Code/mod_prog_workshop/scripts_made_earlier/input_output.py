# Functions to import and write out data

import pandas as pd

def load_formatted_frame(filepath):
    dataframe = pd.read_csv(filepath)
    
    # Clean the column names, following naming conventions similar to PEP8
    dataframe.columns = dataframe.columns.str.lower() 
    dataframe.columns = dataframe.columns.str.replace(" ", "_")
    
    return dataframe

def write_output(dataframe, output_filepath):
    """Function to write output statistic in formatted manner"""

    dataframe.to_csv(output_filepath, index=False, sep=",")
    
    # We are not returning anything so our function
    # does not need a return value. By default this
    # will return `None`