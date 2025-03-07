import os
import pandas as pd
from mvgbike import MVGBike  

Bicycle = MVGBike()

Bicycle.refresh_cache()

# Calculate all attributes using the Bicycle instance
space_value = Bicycle.space 
number_vehicles = Bicycle.number_vehicles
hours_idling_value = Bicycle.hours_idling 
annual_mileage_value = Bicycle.annual_mileage  
annual_usage_time = Bicycle.annual_usage_time    
annual_parking_cost = Bicycle.annual_parking_cost
annual_parking_cost_stations = Bicycle.annual_parking_cost_stations

# Create a dictionary with the calculated values
data = {
    'space_bicycle': [space_value],  
    'number_vehicles_bicycle': [number_vehicles],
    'hours_idling_bicycle': [hours_idling_value], 
    'annual_mileage_bicycle': [annual_mileage_value],  
    'annual_usage_time_bicycle': [annual_usage_time],
    'annual_parking_cost_bicycle': [annual_parking_cost],
    'annual_parking_cost_bicycle_stations': [annual_parking_cost_stations] 
}

# Create a Pandas DataFrame from the dictionary
result_df_bicycle = pd.DataFrame(data) 

# Construct the relative path to the 'csv' directory
base_path = os.path.join(os.path.dirname(__file__), '..', '..', 'csv')

# Ensure the directory exists
if not os.path.exists(base_path):
    os.makedirs(base_path)

# Construct the path to the CSV file
path_to_csv = os.path.join(base_path, 'bicycle_attributes.csv')

# Save the DataFrame as a CSV file at the specified path
result_df_bicycle.to_csv(path_to_csv, index=False)  

print(f"Attributes have been calculated and saved in '{path_to_csv}'.")

# Read the DataFrame from the CSV file at the specified path
result_df_bicycle = pd.read_csv(path_to_csv)  

# Print the results
print("Calculated Attributes Bicycle:")  
print("Space Bicycle:", result_df_bicycle['space_bicycle'][0]) 
print("Number Vehicles Bicycle:", result_df_bicycle['number_vehicles_bicycle'][0])  
print("Hours Idling Bicycle:", result_df_bicycle['hours_idling_bicycle'][0])  
print("Annual Mileage Bicycle:", result_df_bicycle['annual_mileage_bicycle'][0]) 
print("Annual Usage Time Bicycle:", result_df_bicycle['annual_usage_time_bicycle'][0])  
print("Annual Parking Cost Bicycle:", result_df_bicycle['annual_parking_cost_bicycle'][0])  
print("Annual Parking Cost Bicycle Stations:", result_df_bicycle['annual_parking_cost_bicycle_stations'][0])  
