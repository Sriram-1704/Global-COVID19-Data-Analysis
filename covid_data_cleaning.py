# Importing Pandas Library for Cleaning and Manipulating the Datasets
import pandas as pd

# Loading the datasets
# Reading the country_wise_latest.csv file
country_data = pd.read_csv("Health Related Datasets/country_wise_latest.csv")

# Reading the day_wise.csv file
day_data = pd.read_csv("Health Related Datasets/day_wise.csv")

# Reading the worldometer_data.csv file
worldometer_data = pd.read_csv("Health Related Datasets/worldometer_data.csv")

# Checking whether the data is loaded properly or not
print("Country wise dataset loaded successfully. Shape:", country_data.shape)
print("Day wise dataset loaded successfully. Shape:", day_data.shape)
print("Worldometer dataset loaded successfully. Shape:", worldometer_data.shape)

# Shows the first 5 rows of the country_data
print(country_data.head())

# Removing Missing or Null values from the datasets
country_data = country_data.dropna()
day_data = day_data.dropna()
worldometer_data = worldometer_data.dropna()

# Changing column names by removing extra spaces and converting to lowercase
country_data.columns = country_data.columns.str.strip().str.lower()
day_data.columns = day_data.columns.str.strip().str.lower()
worldometer_data.columns = worldometer_data.columns.str.strip().str.lower()

# Creating two new columns in country_data one is recovery_rate and the other is death_rate 
country_data['recovery_rate'] = (country_data['recovered'] / country_data['confirmed']) * 100
country_data['death_rate'] = (country_data['deaths'] / country_data['confirmed']) * 100

# To keep the output of recovery_rate and death_rate neat, we use .round() function 
country_data['recovery_rate'] = country_data['recovery_rate'].round(2)
country_data['death_rate'] = country_data['death_rate'].round(2)

# Viewing Summary Statistics info like Mean, Min, Max, Standard Deviation, Quartiles 
print("\n Basic Summary Statistics (Country Data)")
print(country_data[['confirmed', 'deaths', 'recovered', 'recovery_rate', 'death_rate']].describe())

# Finding which country has the highest confirmed, deaths, and recovery
highest_confirmed = country_data.loc[country_data['confirmed'].idxmax(), ['country/region', 'confirmed']]
highest_deaths = country_data.loc[country_data['deaths'].idxmax(), ['country/region', 'deaths']]
highest_recovery_rate = country_data.loc[country_data['recovery_rate'].idxmax(), ['country/region', 'recovery_rate']]

# Displays country names and values of Highest Confirmed Cases, Highest Deaths, Highest Recovery Rate
print("\nCountry with Highest Confirmed Cases:", highest_confirmed['country/region'], "-", highest_confirmed['confirmed'])
print("Country with Highest Deaths:", highest_deaths['country/region'], "-", highest_deaths['deaths'])
print("Country with Highest Recovery Rate:", highest_recovery_rate['country/region'], "-", highest_recovery_rate['recovery_rate'], "%")

# Sums up the values across all countries to get global totals
total_confirmed = country_data['confirmed'].sum()
total_deaths = country_data['deaths'].sum()
total_recovered = country_data['recovered'].sum()

# Calculating global recovery rate and death rate using total
global_recovery_rate = (total_recovered / total_confirmed) * 100
global_death_rate = (total_deaths / total_confirmed) * 100

print("\n Global Summary ")
print("Total Confirmed Cases:", total_confirmed)
print("Total Deaths:", total_deaths)
print("Total Recovered:", total_recovered)
print("Average Recovery Rate:", round(global_recovery_rate, 2), "%")
print("Average Death Rate:", round(global_death_rate, 2), "%")

# Saving the cleaned datasets into new CSV files 
country_data.to_csv("Health Related Datasets/country_cleaned.csv", index=False)
day_data.to_csv("Health Related Datasets/day_cleaned.csv", index=False)
worldometer_data.to_csv("Health Related Datasets/worldometer_cleaned.csv", index=False)

print("\n Cleaned CSV files have been saved inside the 'Health Related Datasets' folder.")


