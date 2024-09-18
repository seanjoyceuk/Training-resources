library(readr)

#' Read population data and reformat column names
load_formatted_frame <- function(path_to_data) {
    # Load the population density data 2019
    formatted_path <- file.path(path_to_data)
    dataframe <- readr::read_csv(formatted_path)
    
    # Clean the column names, following snake_case convention
    colnames(dataframe) <- tolower(colnames(dataframe))
    colnames(dataframe) <- stringr::str_replace_all(colnames(dataframe), pattern = " ", replacement = "_")
    
    return(dataframe)
}
    

#' write output statistic in formatted manner
write_output <- function(dataframe, output_filepath) {
    
    readr::write_csv(x = dataframe, path = output_filepath)
    
}
