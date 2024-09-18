

#' Join the required frames on specified columns, 
#' dropping unecessary columns
join_frames <- function(left_dataframe, right_dataframe, left_column, right_column) {
  
  # Change location_id to be called country_code for join
  colnames(right_dataframe)[colnames(right_dataframe) == right_column] <- left_column
  
  combined_frames <- dplyr::left_join(x = left_dataframe,
                                      y = right_dataframe,
                                      by = left_column)
  
  combined_frames_reduced <- dplyr::select(combined_frames, sdg_region_name, population_density)
  
  return(combined_frames_reduced)
}

#' Join a list of frames with an inner join on a specified column name
join_years <- function(dataframes, join_column) {

  merged_frame <- dataframes %>% purrr::reduce(.x = dataframes, 
                                                .f = dplyr::inner_join, 
                                                by = join_column)

  return(merged_frame)
}