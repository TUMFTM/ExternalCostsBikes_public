import os
import sys
import pandas as pd

# Construct the path to the 'input' directory and add it to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

class InputCollisions:
    def __init__(self):
        """
        Initialize the InputCollisions instance and load accident data with fallback.
        """
        base_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'csv')

        # Initialize scenario_variables to store processed scenario data
        self.scenario_variables = {}

        # Define possible data files with priority (first one found will be used)
        possible_files = [
            os.path.join(base_path, 'accident_data_2022_detailed_processed.csv'),  # Primary file
            os.path.join(base_path, 'accidents_dummy_processed.csv'),              # Dummy file as fallback
        ]

        # Load data with fallback mechanism
        accident_data_detailed_2022 = self.load_data_with_fallback(possible_files)
        if accident_data_detailed_2022 is None:
            raise FileNotFoundError("No valid accident data file found. Please provide a valid CSV file.")

        # Annual mileages in vkm
        self.annual_mileage_private_bicycle = 1103210000 # Source: D. Schröder, L. Kirn, J. Kinigadner, A. Loder, P. Blum, et al., „Ending the myth of mobility at zero costs: An external cost analysis,“ Research in Transportation Economics, vol. 97, p. 101246, 2022, DOI: 10.1016/j.retrec.2022.101246 + R. Follmer and J. Belz, „Mobilität in Deutschland – MiD Kurzreport Stadt München, Münchner Umland und MVV-Verbundraum,“ 2018.
        self.annual_mileage_shared_bicycle = 1487992.064 # Source: database 
        self.annual_mileage_Munich_shared_bicycle = 2066574.21 # Source: database mileage extrapolated for all shared bicycles in Munich

        self.annual_mileage_private_pedelec = 28290000 # Source: D. Schröder, L. Kirn, J. Kinigadner, A. Loder, P. Blum, et al., „Ending the myth of mobility at zero costs: An external cost analysis,“ Research in Transportation Economics, vol. 97, p. 101246, 2022, DOI: 10.1016/j.retrec.2022.101246 + R. Follmer and J. Belz, „Mobilität in Deutschland – MiD Kurzreport Stadt München, Münchner Umland und MVV-Verbundraum,“ 2018.
        self.annual_mileage_shared_pedelec = 200096.408 # Source: database 
        self.annual_mileage_Munich_shared_pedelec = 299626.408 # Source: database extrapolated for all shared pedelecs in Munich

        # Occupancy rates # Source: D. Schröder, L. Kirn, J. Kinigadner, A. Loder, P. Blum, et al., „Ending the myth of mobility at zero costs: An external cost analysis,“ Research in Transportation Economics, vol. 97, p. 101246, 2022, DOI: 10.1016/j.retrec.2022.101246
        self.occupancy_rate_private_bicycle = 1.0
        self.occupancy_rate_shared_bicycle = 1.0
        self.occupancy_rate_private_pedelec = 1.0
        self.occupancy_rate_shared_pedelec = 1.0

        # Collision data for bicycle (shared and private)
        self.rows_participant_1_bicycle = accident_data_detailed_2022[accident_data_detailed_2022['BArt01'] == 71.0]
        self.rows_participant_2_bicycle = accident_data_detailed_2022[accident_data_detailed_2022['BArt02'] == 71.0]
        self.rows_participant_3_bicycle = accident_data_detailed_2022[accident_data_detailed_2022['BArt03'] == 71.0]

        # Collision data for pedelec (shared and private)
        self.rows_participant_1_pedelec = accident_data_detailed_2022[(accident_data_detailed_2022['BArt01'] == 3.0) | (accident_data_detailed_2022['BArt01'] == 72.0)]
        self.rows_participant_2_pedelec = accident_data_detailed_2022[(accident_data_detailed_2022['BArt02'] == 3.0) | (accident_data_detailed_2022['BArt02'] == 72.0)]
        self.rows_participant_3_pedelec = accident_data_detailed_2022[(accident_data_detailed_2022['BArt03'] == 3.0) | (accident_data_detailed_2022['BArt03'] == 72.0)]

        # Load scenario data
        self.load_infrastructure_scenario_data()

    def load_infrastructure_scenario_data(self):
        """
        Load and process the accident data for the infrastructure scenario
        specifically for bicycles and pedelecs.
        """
        scenario_dir = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'python', 'data_handling', 'accident_data', 'accidents_infrastructure_scenario', 'processed_cycle_lane') #TODO: adapt for cycle path scenario

        # Check if directory exists
        if not os.path.exists(scenario_dir):
            print(f"Directory does not exist: {scenario_dir}")
            return

        # Get all CSV files
        csv_files = [name for name in os.listdir(scenario_dir) if name.endswith('.csv')]

        if not csv_files:
            print("No CSV files found in the directory.")
            return

        total_files = len(csv_files)
        # Commenting out the progress display here
        # print(f"Found {total_files} CSV files to process.")

        for idx, filename in enumerate(csv_files, start=1):
            scenario_path = os.path.join(scenario_dir, filename)
            # Commenting out per-file progress
            # print(f"Processing file: {filename}")

            try:
                scenario_data = pd.read_csv(scenario_path)

                # Create a combined structure per CSV that holds accident data for bicycles and pedelecs
                scenario = {
                    'bicycle': {
                        'participant_1': scenario_data[scenario_data['BArt01'] == 71.0],
                        'participant_2': scenario_data[scenario_data['BArt02'] == 71.0],
                        'participant_3': scenario_data[scenario_data['BArt03'] == 71.0]
                    },
                    'pedelec': {
                        'participant_1': scenario_data[(scenario_data['BArt01'] == 3.0) | (scenario_data['BArt01'] == 72.0)],
                        'participant_2': scenario_data[(scenario_data['BArt02'] == 3.0) | (scenario_data['BArt02'] == 72.0)],
                        'participant_3': scenario_data[(scenario_data['BArt03'] == 3.0) | (scenario_data['BArt03'] == 72.0)]
                    }
                }

                self.scenario_variables[f'CSV_{idx}'] = scenario

            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    collisions = InputCollisions()
    # Example usage: print out the first scenario
    for scenario_name, scenario_data in collisions.scenario_variables.items():
        print(f"Scenario: {scenario_name}")
        print("Bicycle Participant 1:")
        print(scenario_data['bicycle']['participant_1'].head()) 
        print("Pedelec Participant 1:")
        print(scenario_data['pedelec']['participant_1'].head())  