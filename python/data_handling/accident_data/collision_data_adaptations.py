import sys
import os
import pandas as pd
import numpy as np
import zipfile
import time
from tqdm import tqdm
import matplotlib.pyplot as plt
import seaborn as sns

# Construct the path to the 'input' directory and add it to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'accident_data')) # TODO: data not publicly available due to privacy reasons --> please insert your own data following the structure of 'accidents_dummy.csv'

# Define the path to the CSV file
csv_path = os.path.join(os.path.dirname(__file__), 'police_accident_data_2022.csv')

# Print the absolute path for debugging
print("Absolute path of the input CSV file:", os.path.abspath(csv_path))

# Check if the file exists
if not os.path.exists(csv_path):
    raise FileNotFoundError(f"File not found: {csv_path}")

# Read the CSV file into a DataFrame called 'data'
# The CSV file is located at the specified path and is semicolon-separated
# The first 9 rows (headers) are skipped during the reading process
data = pd.read_csv(csv_path, sep=';', skiprows=9)


# ======================================================================================
#                   DEFINITION OF IMPORTANT COLUMNS
# ======================================================================================


# Extract the data from a specific column and store it in a variable 
vehicle_causer = data['BArt01']
vehicle_participant_2 = data['BArt02']
vehicle_participant_3 = data['BArt03']
injury_type_causer = data['Verl01']
people_killed = data['tot']
people_severly_injured = data['svl']
people_lightly_injured = data['lvl']


# ======================================================================================
#                   ADDITION OF REQUIRED COLUMNS 
# ======================================================================================


# Dictionary of energy values for each vehicle type based on categorisation used in 2019 police data 
energy_values = {
    '1.0': 8695, # moped
    '2.0': 8695, # moped
    '3.0': 754, # pedelec
    '4.0': 8695, # moped
    '5.0': 818, # e-scooter
    '6.0': 591680, # other --> assumption due to missing information
    '8.0': 591680, # other --> assumption due to missing information
    '11.0': 13393, # motorcycle
    '12.0': 13393, # motorcycle
    '13.0': 13393, # motorcycle
    '15.0': 13393, # motorcycle
    '21.0': 74690, # pkw
    '22.0': 129430, # transporter
    '31.0': 385719, # bus
    '32.0': 385719, # bus
    '33.0': 385719, # bus
    '34.0': 385719, # bus
    '40.0': 129430, # transporter
    '42.0': 129430, # transporter
    '44.0': 591680, # lkw
    '44.0': 591680, # lkw
    '46.0': 591680, # lkw
    '48.0': 591680, # lkw
    '51.0': 591680, # lkw
    '53.0': 591680, # lkw
    '54.0': 591680, # lkw
    '58.0': 591680, # lkw
    '59.0': 591680, # lkw
    '61.0': 850091, # tram
    '71.0': 704, # bike
    '72.0': 754, # pedelec
    '81.0': 84, # pedestrian
    '83.0': 84, # pedestrian
    '84.0': 84, # pedestrian
    '92.0': 591680, # other
    '93.0': 84, # pedestrian
}

# # Function to calculate Ekin accident for a row
# def calculate_ekin_accident(row):
#     ekin_bart01 = energy_values.get(str(row['BArt01']), 0)
#     ekin_bart02 = energy_values.get(str(row['BArt02']), 0)
#     ekin_bart03 = energy_values.get(str(row['BArt03']), 0)
#     return ekin_bart01 + ekin_bart02 + ekin_bart03

def calculate_ekin_accident(row):
    ekin_bart01 = energy_values.get(str(float(row['BArt01'])), 0)
    ekin_bart02 = energy_values.get(str(float(row['BArt02'])), 0)
    ekin_bart03 = energy_values.get(str(float(row['BArt03'])), 0)
    # print(row['BArt01'], row['BArt02'], row['BArt03'])
    # print(ekin_bart01, ekin_bart02, ekin_bart03)
    return ekin_bart01 + ekin_bart02 + ekin_bart03

# Calculate Ekin accident column
data['Ekin Accident'] = data.apply(calculate_ekin_accident, axis=1)


# ======================================================================================
#                   CALCULATION OF EPSILON DEPENDING ON CAUSER
# ======================================================================================


# Calculate Epsilon Participant 1 column
data['Epsilon Participant 1'] = data.apply(
    lambda row: energy_values.get(str(row['BArt01']), 0) / row['Ekin Accident']
    if row['Ekin Accident'] != 0 and not pd.isna(row['BArt01']) else 0, axis=1
)

# Calculate Epsilon Participant 2 column
data['Epsilon Participant 2'] = data.apply(
    lambda row: energy_values.get(str(row['BArt02']), 0) / row['Ekin Accident']
    if row['Ekin Accident'] != 0 and not pd.isna(row['BArt02']) else 0, axis=1
)

# Calculate Epsilon Participant 3 column
data['Epsilon Participant 3'] = data.apply(
    lambda row: energy_values.get(str(row['BArt03']), 0) / row['Ekin Accident']
    if row['Ekin Accident'] != 0 and not pd.isna(row['BArt03']) else 0, axis=1
)


# ======================================================================================
#                   CALCULATION OF TOTAL ACCIDENT COSTS 
# ======================================================================================


# Function to calculate Accident Costs for a row
def calculate_accident_costs(row):
    tot_cost = row['tot'] * 4904583.106 if not pd.isna(row['tot']) else 0
    svl_cost = row['svl'] * 688699.75 if not pd.isna(row['svl']) else 0
    lvl_cost = row['lvl'] * 44573.84 if not pd.isna(row['lvl']) else 0
    
    verl01 = row['Verl01']
    if pd.isna(verl01):
        verl01_cost = 0
    elif verl01 == 4.0:
        verl01_cost = 4147816.27
    elif verl01 == 3.0:
        verl01_cost = 551527.60
    elif verl01 == 2.0:
        verl01_cost = 41471.69
    elif verl01 == 1.0:
        verl01_cost = 0
    else:
        verl01_cost = 0
    
    return tot_cost + svl_cost + lvl_cost - verl01_cost

# Calculate Accident Costs column
data['Accident Costs'] = data.apply(calculate_accident_costs, axis=1)

# Remove rows with NaN or empty values in the first column (assuming the first column is 'Datum')
data.dropna(subset=['Datum'], inplace=True)

# Save the DataFrame as a CSV file
processed_csv_path = os.path.join(os.path.dirname(__file__), 'accident_data_2022_detailed_processed.csv')
data.to_csv(processed_csv_path, index=False)


# ======================================================================================
#               CALCULATION OF BICYCLE INFRASTRUCTURE SCENARIO ACCIDENT COSTS 
# ======================================================================================


scenario_dir = os.path.join(os.path.dirname(__file__), 'accidents_infrastructure_scenario')
zip_file = os.path.join(scenario_dir, 'cycle_lane.zip')  #TODO: adapt for cycle path scenario

if not os.path.exists(scenario_dir):
    os.makedirs(scenario_dir)
    print(f"Created directory: {scenario_dir}")

required_columns = {'BArt01', 'BArt02', 'BArt03', 'Verl01', 'tot', 'svl', 'lvl'}

def process_pkl_in_zip(zip_file):
    with zipfile.ZipFile(zip_file, 'r') as z:
        file_list = [file_name for file_name in z.namelist() if file_name.endswith('.pkl')]
        
        if not file_list:
            print("No .pkl files found in the ZIP archive.")
            return
        
        # Ableitung des Zielordners aus dem ZIP-Dateinamen
        zip_base_name = os.path.splitext(os.path.basename(zip_file))[0]
        processed_dir = os.path.join(scenario_dir, f'processed_{zip_base_name}')
        
        # Zielordner erstellen, falls er noch nicht existiert
        if not os.path.exists(processed_dir):
            os.makedirs(processed_dir)
            print(f"Created processed directory: {processed_dir}")
        
        for file_name in tqdm(file_list, desc="Processing files", unit="file"):
            print(f"Processing file: {file_name}")
            with z.open(file_name) as f:
                data = pd.read_pickle(f)
            
            missing_columns = required_columns - set(data.columns)
            if missing_columns:
                raise ValueError(f"Missing columns in {file_name}: {missing_columns}")
            
            data['Ekin Accident'] = data.apply(calculate_ekin_accident, axis=1)
            
            data['Epsilon Participant 1'] = data.apply(
                lambda row: energy_values.get(str(row['BArt01']), 0) / row['Ekin Accident']
                if row['Ekin Accident'] != 0 and not pd.isna(row['BArt01']) else 0, axis=1
            )

            data['Epsilon Participant 2'] = data.apply(
                lambda row: energy_values.get(str(row['BArt02']), 0) / row['Ekin Accident']
                if row['Ekin Accident'] != 0 and not pd.isna(row['BArt02']) else 0, axis=1
            )

            data['Epsilon Participant 3'] = data.apply(
                lambda row: energy_values.get(str(row['BArt03']), 0) / row['Ekin Accident']
                if row['Ekin Accident'] != 0 and not pd.isna(row['BArt03']) else 0, axis=1
            )
            
            data['Accident Costs'] = data.apply(calculate_accident_costs, axis=1)

            processed_csv_path = os.path.join(processed_dir, file_name.replace('.pkl', '.csv'))
            data.to_csv(processed_csv_path, index=False)
            
            print(f"\nSaved processed file to {processed_csv_path}")
            print(data.head())

process_pkl_in_zip(zip_file)
