# Functions for manipulations

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
    


def convert_col_to_int(dataframe, col_name, string_pattern):
    """Function to convert string to integer column type"""
    
    dataframe = dataframe.copy()
    
    dataframe[col_name] = dataframe[col_name].str.replace(string_pattern, "")
    
    dataframe[col_name] = dataframe[col_name].astype(int)
    
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