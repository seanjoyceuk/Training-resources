

#' Function to groupby and calculate the mean of two columns
aggregate_mean <- function(dataframe, groupby_column, statistic_column) {
  
  # Perform aggregation and summary
  
  # Use group_by_ because of variable column name
  region_mean_density_grouped <- group_by_(.data = dataframe, groupby_column)
  
  # use get() to access column name
  region_mean_density <- dplyr::summarise(.data = region_mean_density_grouped,
                                          "mean_population_density" = mean(get(statistic_column)))
  
  return(region_mean_density)
}


#' Format the dataframe for output
format_frame <- function(dataframe, statistic_column) {
  
  # Sort the data for clearer reading, descending order
  dataframe_sorted <- dplyr::arrange(.data = dataframe)
  
  # Round mean density for clearer reading
  dataframe_sorted[statistic_column] <- round(dataframe_sorted[statistic_column],
                                              digits = 2)
  
  return(dataframe_sorted)
}