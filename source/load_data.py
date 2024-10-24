import pandas as pd
import os

def load_data(countries, folder_name):

    # List of countries and corresponding file names

    # Initialize an empty list to store dataframes
    dfs = []

    # Loop through each file and load it into a dataframe
    for country in countries:
        # Construct the path to the CSV file, assuming files are named like 'BR.csv', 'US.csv', etc.
        file_name = f"{country}.csv"
        file_path = os.path.join('.', folder_name, file_name)
        
        # Load the CSV into a dataframe
        df = pd.read_csv(file_path)
        
        # Rename columns for consistency
        df.columns = ['Date', 'GDP']
        
        # Add a column to store the country name
        df['Country'] = country
        
        # Append to the list of dataframes
        dfs.append(df)

    # Combine all dataframes into one
    combined_df = pd.concat(dfs)

    # Convert the 'Date' column to datetime if necessary
    combined_df['Date'] = pd.to_datetime(combined_df['Date'])

    # Return the dataframe
    return combined_df