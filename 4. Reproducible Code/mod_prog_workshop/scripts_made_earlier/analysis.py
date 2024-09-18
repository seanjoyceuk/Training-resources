# Functions for analysis of the data

import pandas as pd


def aggregate_mean(dataframe, groupby_column, statistic_column):
    """Function to groupby and calculate the aggregate mean of two columns"""
    
    dataframe = dataframe.copy()
    
    # Remove unecessary columns
    subset = dataframe[[groupby_column, statistic_column]]
    
    # Perform mean calculation
    statistic = (subset.groupby(groupby_column, as_index=False)
                       .agg({statistic_column: "mean"}))
                       
    statistic_renamed = statistic.rename(columns={statistic_column: "mean_" + statistic_column})
  
    return statistic_renamed
    
    
    
def format_frame(dataframe, statistic_column):
    """Function to format the dataframe for output"""
    
    dataframe = dataframe.copy()
    
    dataframe_sorted = dataframe.sort_values(by=statistic_column,
                                             ascending=False)
                                      
    dataframe_sorted[statistic_column] = dataframe_sorted[statistic_column].round(2)
    
    return dataframe_sorted