import os
import pandas as pd
from tierebike import TierEbike  # Import the TierEbike class

# Create an instance of the TierEbike class and assign it to Pedelec
Pedelec = TierEbike()

Pedelec.refresh_cache()

# Calculate all attributes using the Pedelec instance
space_value = Pedelec.space
hours_idling_value = Pedelec.hours_idling
annual_mileage_value = Pedelec.annual_mileage
power_consumption_driving_value = Pedelec.power_consumption_driving
power_consumption_idling_value = Pedelec.power_consumption_idling
avg_power_consumption_per_vkm_value = Pedelec.avg_power_consumption_per_vkm
annual_usage_time = Pedelec.annual_usage_time  
annual_parking_cost = Pedelec.annual_parking_cost

# Create a dictionary with the calculated values
data = {
    'space_pedelec': [space_value],
    'hours_idling_pedelec': [hours_idling_value],
    'annual_mileage_pedelec': [annual_mileage_value],
    'power_consumption_driving_pedelec': [power_consumption_driving_value],
    'power_consumption_idling_pedelec': [power_consumption_idling_value],
    'avg_power_consumption_per_vkm_pedelec': [avg_power_consumption_per_vkm_value],
    'annual_usage_time_pedelec': [annual_usage_time],
    'annual_parking_cost_pedelec': [annual_parking_cost]
}

# Create a Pandas DataFrame from the dictionary
result_df_pedelec = pd.DataFrame(data)

# Construct the relative path to the 'csv' directory
base_path = os.path.join(os.path.dirname(__file__), '..', '..', 'csv')

# Ensure the directory exists
if not os.path.exists(base_path):
    os.makedirs(base_path)

# Construct the path to the CSV file
path_to_csv = os.path.join(base_path, 'pedelec_attributes.csv')

# Save the DataFrame as a CSV file at the specified path
result_df_pedelec.to_csv(path_to_csv, index=False)

print(f"Attributes have been calculated and saved in '{path_to_csv}'.")

# Read the DataFrame from the CSV file at the specified path
result_df_pedelec = pd.read_csv(path_to_csv)

# Print the results
print("Calculated Attributes Pedelec:")
print("Space Pedelec:", result_df_pedelec['space_pedelec'][0])
print("Hours Idling Pedelec:", result_df_pedelec['hours_idling_pedelec'][0])
print("Annual Mileage Pedelec:", result_df_pedelec['annual_mileage_pedelec'][0])
print("Power Consumption Driving Pedelec:", result_df_pedelec['power_consumption_driving_pedelec'][0])
print("Power Consumption Idling Pedelec:", result_df_pedelec['power_consumption_idling_pedelec'][0])
print("Power Consumption per vkm Pedelec:", result_df_pedelec['avg_power_consumption_per_vkm_pedelec'][0])
print("Annual Usage Time Pedelec:", result_df_pedelec['annual_usage_time_pedelec'][0]) 
print("Annual Parking Cost Pedelec:", result_df_pedelec['annual_parking_cost_pedelec'][0])  
