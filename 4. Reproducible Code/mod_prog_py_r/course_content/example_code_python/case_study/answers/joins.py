import pandas as pd


def join_frames(left_dataframe, right_dataframe, left_column, right_column):
    """
    Function to join the required frames on specified columns, dropping
    unrecessary column
    """
    combined_frames = left_dataframe.merge(right=right_dataframe,
                                           how="left",
                                           left_on=left_column,
                                           right_on=right_column)
                                           
    combined_frames_reduced = combined_frames.drop(labels=[right_column], axis=1)
    
    return combined_frames_reduced
    
    
    
def join_years(dataframes, join_column):
    """Function to join a list of frames with an inner join on a specified column name"""
    
    # Starting with first frame iterate over each other frame and join to initial
    temp_frame = dataframes[0]
    
    for frame in dataframes[1:]:
        temp_frame = temp_frame.merge(frame, how="inner", on=join_column)
    
  
    return temp_frame
