# File to analyse the mean population density data from the UN

# Import relevant libraries for analysis
import pandas as pd
import os

# Load the population density data 2019
population_path = os.path.join("../../data/population_density_2019.csv")
pop_density = pd.read_csv(population_path)

# Clean the column names, following naming conventions similar to PEP8
pop_density.columns = pop_density.columns.str.lower()
pop_density.columns = pop_density.columns.str.replace(" ", "_")

# The country_and_parent_code column needs to 
# be split into two columns without the strings
pop_density[["country_code", "parent_code"]] = (pop_density["country_and_parent_code"]
                                                .str.split("_", expand=True))

# Remove the country_and_parent_code and parent_code columns, not used in later analysis
# axis=1 to remove the columns
pop_density = pop_density.drop(labels=[
                                       "country_and_parent_code", 
                                       "parent_code"
                                       ], 
                               axis=1)

# Convert country_code to integer by removing strings
pop_density["country_code"] = pop_density["country_code"].str.replace("CC", "")
pop_density["country_code"] = pop_density["country_code"].astype(int)


# Load the locations data to get the Sustainable Development Goals sub regions
locations_path = os.path.join("../../data/locations.csv")
locations = pd.read_csv(locations_path)

# Clean the column names, following naming conventions similar to PEP8
locations.columns = locations.columns.str.lower()
locations.columns =  locations.columns.str.replace(" ", "_")

# The location_id data has quotation marks making it a string,
# it needs to be converted to a numeric
locations["location_id"] = locations["location_id"].str.replace('"', '')
locations["location_id"] = locations["location_id"].astype(int)

# Join the data sets
# Left merge so we keep all pop_density data
pop_density_location = pop_density.merge(locations, 
                                         how="left",
                                         left_on="country_code",
                                         right_on="location_id")

# Remove the location_id column as it is equal to country_code or missing
pop_density_location = pop_density_location.drop(labels=["location_id"], axis=1)

# Get just the relevant columns in preparation
# for the following groupby
region_density = pop_density_location[["sdg_region_name", "population_density"]]

# Calculate the mean population density for each region
# A non-weighted mean
region_mean_density = (region_density.groupby('sdg_region_name', as_index=False)
                       .agg({"population_density": "mean"}))
                       
region_mean_density = region_mean_density.rename(columns={"population_density": "mean_population_density"})

# Sort the data for clearer reading
region_mean_density = region_mean_density.sort_values(by="mean_population_density",
                                                      ascending=False)

# Round mean density for clearer reading
region_mean_density["mean_population_density"] = region_mean_density["mean_population_density"].round(2)

# Write out the final output
region_mean_density.to_csv("mean_population_density_output.csv", index=False)
