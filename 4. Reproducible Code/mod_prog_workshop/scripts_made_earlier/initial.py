# File to analyse the mean population density data from the UN

# Import relevant libraries for analysis
import pandas as pd

# Load the population density data 2019

pop_density = pd.read_csv("../data/population_density_2019.csv")

# Clean the column names, following naming conventions similar to PEP8
pop_density.columns = pop_density.columns.str.lower()
pop_density.columns = pop_density.columns.str.replace(" ", "_")

# Split country code and parent code into two columns without the strings
pop_density[["country_code", "parent_code"]] = (pop_density["country_and_parent_code"]
                                                .str.split("_", expand=True))

# Remove columns we won't use later
pop_density = pop_density.drop(labels=["country_and_parent_code", 
                                       "parent_code"], 
                               axis=1) # axis = 1 to act on columns

# Convert country_code to integer
pop_density["country_code"] = pop_density["country_code"].str.replace("CC", "")
pop_density["country_code"] = pop_density["country_code"].astype(int)


# Load the locations data to get the Sustainable Development Goals sub regions
locations = pd.read_csv("../data/locations.csv")

# Clean the column names, following naming conventions similar to PEP8
locations.columns = locations.columns.str.lower()
locations.columns =  locations.columns.str.replace(" ", "_")

# Convert location_id to integer 
locations["location_id"] = locations["location_id"].str.replace('"', '')
locations["location_id"] = locations["location_id"].astype(int)


# Left merge to join datasets together
pop_density_location = pop_density.merge(locations, 
                                         how="left",
                                         left_on="country_code",
                                         right_on="location_id") # Column names differ 

# Remove the location_id column as it is equal to country_code or missing
pop_density_location = pop_density_location.drop(labels=["location_id"], axis=1)

# Keep relevant columns only
region_density = pop_density_location[["sdg_region_name", "population_density"]]

# Calculate the mean population density by region
region_mean_density = (region_density.groupby('sdg_region_name', as_index=False)
                       .agg({"population_density": "mean"}))
                       
region_mean_density = region_mean_density.rename(columns={"population_density": "mean_population_density"})

# Sort the output 
region_mean_density = region_mean_density.sort_values(by="mean_population_density",
                                                      ascending=False)

# Round the output
region_mean_density["mean_population_density"] = region_mean_density["mean_population_density"].round(2)

# Write out the final output
region_mean_density.to_csv("../outputs/mean_population_density_output.csv", index=False)
