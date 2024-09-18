import pandas as pd

def access_country_code(dataframe):
    """Function to split combined code columns and remove uncessary columns"""
    
    dataframe[["country_code", "parent_code"]] = (dataframe["country_and_parent_code"]
                                                .str.split("_", expand=True))
                                                
    dataframe_dropped = dataframe.drop(labels=[
                                                "country_and_parent_code",
                                                "parent_code"
                                              ], axis=1)
    return dataframe_dropped  
    


def convert_type_to_int(dataframe, column_name, string_value):
    """Function to convert string to integer column type"""
    
    dataframe[column_name] = dataframe[column_name].str.replace(string_value, "")
    
    dataframe[column_name] = dataframe[column_name].astype(int)
    
    return dataframe



def column_name_year(dataframe, original_column, new_column):
    """Function to change name of specified columns in dataframe"""
    
    dataframe_new_name = dataframe.rename(columns={original_column: new_column})
    
    return dataframe_new_name

    
