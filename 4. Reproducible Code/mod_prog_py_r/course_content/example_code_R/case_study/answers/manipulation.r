

#' Function to split combined code columns 
#' and remove uncessary columns
access_country_code <- function(dataframe) {
  # The country_and_parent_code column needs to 
  # be split into two columns without the strings
  dataframe <- tidyr::separate(data = dataframe, col = country_and_parent_code,
                               into = c("country_code", "parent_code"), sep = "_")
  
  
  # Remove the  parent_code column, not used in later analysis
  dataframe <- dplyr::select(dataframe, everything(), -parent_code)
  
  return(dataframe)
}


#' Function to convert string to integer column type
convert_type_to_int <- function(dataframe, column_name, string_value) {
  
  # Convert country_code to integer by removing extra strings
  # Using dataframe$column_name to get a column won't work when the column name is a variable
  dataframe[column_name] <- stringr::str_remove_all(dataframe[[column_name]], pattern = string_value)
  
  # Convert type
  dataframe[column_name] <- as.integer(dataframe[[column_name]])
  
  return(dataframe)
}

#' Change name of specified columns in dataframe
column_name_year <- function(dataframe, original_column, new_column) {

  colnames(dataframe)[colnames(dataframe) == original_column] <- new_column

  return(dataframe)
}
