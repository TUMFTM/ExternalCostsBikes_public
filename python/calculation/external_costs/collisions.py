import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scienceplots
import pickle 


# Add the path to the external cost input directory for importing necessary modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))


# Set up directories for saving plots and results
current_file = os.path.realpath('__file__')
current_directory = os.path.dirname(current_file)
figures_directory = os.path.join(current_directory, 'figures')
results_directory = os.path.join(current_directory, 'results')  
os.makedirs(figures_directory, exist_ok=True)
os.makedirs(results_directory, exist_ok=True)


from input.external_costs.input_collisions import InputCollisions


class CollisionsCalculator:
    def __init__(self, mode='all_bicycle', method='damage_potential'):
        """
        Initialize the CollisionsCalculator with a specific mode and method.
        
        Args:
            mode (str): The transportation mode (e.g., 'private_bicycle', 'shared_pedelec').
            method (str): The calculation method ('damage_potential' or 'causer').
        """
        self.mode = mode
        self.method = method
        self.tag = 'Collisions'
        self.input_collisions = InputCollisions() 
        self.result = {}
        self.scenario_results_df = pd.DataFrame()  
        self.init_vehicle_modes()


    def init_vehicle_modes(self):
        """
        Initialize vehicle modes and related parameters such as mileage, 
        occupancy rates, and cost factors for shared and private vehicles.
        """
        self.factor_shared_bicycle = self.input_collisions.annual_mileage_Munich_shared_bicycle / (self.input_collisions.annual_mileage_private_bicycle + self.input_collisions.annual_mileage_Munich_shared_bicycle)
        self.factor_private_bicycle = self.input_collisions.annual_mileage_private_bicycle / (self.input_collisions.annual_mileage_private_bicycle + self.input_collisions.annual_mileage_Munich_shared_bicycle)
        self.factor_shared_pedelec = self.input_collisions.annual_mileage_Munich_shared_pedelec / (self.input_collisions.annual_mileage_private_pedelec + self.input_collisions.annual_mileage_Munich_shared_pedelec)
        self.factor_private_pedelec = self.input_collisions.annual_mileage_private_pedelec / (self.input_collisions.annual_mileage_private_pedelec + self.input_collisions.annual_mileage_Munich_shared_pedelec)
        self.factor_all = 1  # Factor for the aggregated mode

        self.modes = {
            'private_bicycle': {
                'epsilon_participant_1': self.input_collisions.rows_participant_1_bicycle['Epsilon Participant 1'],
                'epsilon_participant_2': self.input_collisions.rows_participant_2_bicycle['Epsilon Participant 2'],
                'epsilon_participant_3': self.input_collisions.rows_participant_3_bicycle['Epsilon Participant 3'],
                'collision_costs_participant_1': self.input_collisions.rows_participant_1_bicycle['Accident Costs'],
                'collision_costs_participant_2': self.input_collisions.rows_participant_2_bicycle['Accident Costs'],
                'collision_costs_participant_3': self.input_collisions.rows_participant_3_bicycle['Accident Costs'],
                'annual_mileage_private': self.input_collisions.annual_mileage_private_bicycle,
                'annual_mileage_shared': self.input_collisions.annual_mileage_shared_bicycle,
                'occupancy_rate': self.input_collisions.occupancy_rate_private_bicycle,
                'factor': self.factor_private_bicycle,
            },
            'shared_bicycle': {
                'epsilon_participant_1': self.input_collisions.rows_participant_1_bicycle['Epsilon Participant 1'],
                'epsilon_participant_2': self.input_collisions.rows_participant_2_bicycle['Epsilon Participant 2'],
                'epsilon_participant_3': self.input_collisions.rows_participant_3_bicycle['Epsilon Participant 3'],
                'collision_costs_participant_1': self.input_collisions.rows_participant_1_bicycle['Accident Costs'],
                'collision_costs_participant_2': self.input_collisions.rows_participant_2_bicycle['Accident Costs'],
                'collision_costs_participant_3': self.input_collisions.rows_participant_3_bicycle['Accident Costs'],
                'annual_mileage_private': self.input_collisions.annual_mileage_shared_bicycle,
                'annual_mileage_shared': self.input_collisions.annual_mileage_shared_bicycle,
                'occupancy_rate': self.input_collisions.occupancy_rate_shared_bicycle,
                'factor': self.factor_shared_bicycle,
            },
            'private_pedelec': {
                'epsilon_participant_1': self.input_collisions.rows_participant_1_pedelec['Epsilon Participant 1'],
                'epsilon_participant_2': self.input_collisions.rows_participant_2_pedelec['Epsilon Participant 2'],
                'epsilon_participant_3': self.input_collisions.rows_participant_3_pedelec['Epsilon Participant 3'],
                'collision_costs_participant_1': self.input_collisions.rows_participant_1_pedelec['Accident Costs'],
                'collision_costs_participant_2': self.input_collisions.rows_participant_2_pedelec['Accident Costs'],
                'collision_costs_participant_3': self.input_collisions.rows_participant_3_pedelec['Accident Costs'],
                'annual_mileage_private': self.input_collisions.annual_mileage_private_pedelec,
                'annual_mileage_shared': self.input_collisions.annual_mileage_shared_pedelec,
                'occupancy_rate': self.input_collisions.occupancy_rate_private_pedelec,
                'factor': self.factor_private_pedelec,
            },
            'shared_pedelec': {
                'epsilon_participant_1': self.input_collisions.rows_participant_1_pedelec['Epsilon Participant 1'],
                'epsilon_participant_2': self.input_collisions.rows_participant_2_pedelec['Epsilon Participant 2'],
                'epsilon_participant_3': self.input_collisions.rows_participant_3_pedelec['Epsilon Participant 3'],
                'collision_costs_participant_1': self.input_collisions.rows_participant_1_pedelec['Accident Costs'],
                'collision_costs_participant_2': self.input_collisions.rows_participant_2_pedelec['Accident Costs'],
                'collision_costs_participant_3': self.input_collisions.rows_participant_3_pedelec['Accident Costs'],
                'annual_mileage_private': self.input_collisions.annual_mileage_Munich_shared_pedelec,
                'annual_mileage_shared': self.input_collisions.annual_mileage_Munich_shared_pedelec,
                'occupancy_rate': self.input_collisions.occupancy_rate_shared_pedelec,
                'factor': self.factor_shared_pedelec,
            },
            'all_bicycle': {
                'epsilon_participant_1': self.input_collisions.rows_participant_1_bicycle['Epsilon Participant 1'],
                'epsilon_participant_2': self.input_collisions.rows_participant_2_bicycle['Epsilon Participant 2'],
                'epsilon_participant_3': self.input_collisions.rows_participant_3_bicycle['Epsilon Participant 3'],
                'collision_costs_participant_1': self.input_collisions.rows_participant_1_bicycle['Accident Costs'],
                'collision_costs_participant_2': self.input_collisions.rows_participant_2_bicycle['Accident Costs'],
                'collision_costs_participant_3': self.input_collisions.rows_participant_3_bicycle['Accident Costs'],
                'annual_mileage_private': self.input_collisions.annual_mileage_private_bicycle,
                'annual_mileage_shared': self.input_collisions.annual_mileage_Munich_shared_bicycle,
                'occupancy_rate': self.input_collisions.occupancy_rate_private_bicycle,
                'factor': self.factor_all,
            },
            'all_pedelec': {
                'epsilon_participant_1': self.input_collisions.rows_participant_1_pedelec['Epsilon Participant 1'],
                'epsilon_participant_2': self.input_collisions.rows_participant_2_pedelec['Epsilon Participant 2'],
                'epsilon_participant_3': self.input_collisions.rows_participant_3_pedelec['Epsilon Participant 3'],
                'collision_costs_participant_1': self.input_collisions.rows_participant_1_pedelec['Accident Costs'],
                'collision_costs_participant_2': self.input_collisions.rows_participant_2_pedelec['Accident Costs'],
                'collision_costs_participant_3': self.input_collisions.rows_participant_3_pedelec['Accident Costs'],
                'annual_mileage_private': self.input_collisions.annual_mileage_private_pedelec,
                'annual_mileage_shared': self.input_collisions.annual_mileage_Munich_shared_pedelec,
                'occupancy_rate': self.input_collisions.occupancy_rate_private_pedelec,
                'factor': self.factor_all,
            }
        }


    def calc_costs(self):
        """
        Calculate external costs based on the mode and method.
        """
        if 'infrastructure' in self.method:
            return self.process_infrastructure_scenario()
        elif self.mode in self.modes:
            mode_data = self.modes[self.mode]
            epsilon_participant_1 = mode_data['epsilon_participant_1']
            epsilon_participant_2 = mode_data['epsilon_participant_2']
            epsilon_participant_3 = mode_data['epsilon_participant_3']
            collision_costs_participant_1 = mode_data['collision_costs_participant_1']
            collision_costs_participant_2 = mode_data['collision_costs_participant_2']
            collision_costs_participant_3 = mode_data['collision_costs_participant_3']
            annual_mileage_private = mode_data['annual_mileage_private']
            annual_mileage_shared = mode_data['annual_mileage_shared']
            occupancy_rate = mode_data['occupancy_rate']
            factor = mode_data['factor']

            if self.method == 'damage_potential':
                sum_costs_participant_1 = sum(epsilon_participant_1 * collision_costs_participant_1)
                sum_costs_participant_2 = sum(epsilon_participant_2 * collision_costs_participant_2)
                sum_costs_participant_3 = sum(epsilon_participant_3 * collision_costs_participant_3)

                total_accident_costs_damage_potential_year = (sum_costs_participant_1 +
                                                              sum_costs_participant_2 +
                                                              sum_costs_participant_3) * factor

                total_accident_costs_damage_potential_pkm = total_accident_costs_damage_potential_year * 100 / (
                        (annual_mileage_private + annual_mileage_shared) * occupancy_rate)
                total_accident_costs_damage_potential_vkm = total_accident_costs_damage_potential_year * 100 / (
                        annual_mileage_private + annual_mileage_shared)

                self.result['cost per vkm'] = total_accident_costs_damage_potential_vkm
                self.result['cost per pkm'] = total_accident_costs_damage_potential_pkm
                self.result['cost per year'] = total_accident_costs_damage_potential_year

                return self.result

            elif self.method == 'causer':
                total_accident_costs_causer_year = sum(collision_costs_participant_1) * factor

                total_accident_costs_causer_pkm = total_accident_costs_causer_year * 100 / (
                        (annual_mileage_private + annual_mileage_shared) * occupancy_rate)
                total_accident_costs_causer_vkm = total_accident_costs_causer_year * 100 / (
                        annual_mileage_private + annual_mileage_shared)

                self.result['cost per vkm'] = total_accident_costs_causer_vkm
                self.result['cost per pkm'] = total_accident_costs_causer_pkm
                self.result['cost per year'] = total_accident_costs_causer_year

                return self.result

        return None
    

    def process_infrastructure_scenario(self):
        """
        Process infrastructure scenarios and calculate external costs for the given mode.
        Loads saved results if the script is imported, otherwise calculates and saves them.
        """
        import __main__
        is_main = (__main__.__name__ == '__main__')

        if not is_main:
            # When imported as a module: load results
            results_file = os.path.join(results_directory, f"infrastructure_results_{self.mode}_{self.method}.pkl")
            if os.path.exists(results_file):
                with open(results_file, 'rb') as f:
                    loaded_data = pickle.load(f)
                    self.result = loaded_data['result']
                    self.scenario_results_df = loaded_data['scenario_results_df']
                print(f"Results for mode '{self.mode}' and method '{self.method}' loaded from '{results_file}'.")
                return self.result
            else:
                print(f"Saved results for mode '{self.mode}' and method '{self.method}' not found. Performing calculations.")
                # Fallback: Perform calculations since no saved results are available

        # Perform calculations if running as main or no saved results are found
        scenario_results = []

        if self.mode not in ['all_bicycle', 'all_pedelec']:
            print(f"Unsupported mode '{self.mode}' for infrastructure scenario.")
            return None

        for scenario_name, scenario_data in self.input_collisions.scenario_variables.items():
            if self.mode == 'all_bicycle':
                vehicle_data = scenario_data['bicycle']
                annual_mileage_private = self.input_collisions.annual_mileage_private_bicycle
                annual_mileage_shared = self.input_collisions.annual_mileage_shared_bicycle
                occupancy_rate = self.input_collisions.occupancy_rate_private_bicycle
            elif self.mode == 'all_pedelec':
                vehicle_data = scenario_data['pedelec']
                annual_mileage_private = self.input_collisions.annual_mileage_private_pedelec
                annual_mileage_shared = self.input_collisions.annual_mileage_shared_pedelec
                occupancy_rate = self.input_collisions.occupancy_rate_private_pedelec

            epsilon_participant_1 = vehicle_data['participant_1']['Epsilon Participant 1']
            epsilon_participant_2 = vehicle_data['participant_2']['Epsilon Participant 2']
            epsilon_participant_3 = vehicle_data['participant_3']['Epsilon Participant 3']
            collision_costs_participant_1 = vehicle_data['participant_1']['Accident Costs']
            collision_costs_participant_2 = vehicle_data['participant_2']['Accident Costs']
            collision_costs_participant_3 = vehicle_data['participant_3']['Accident Costs']

            sum_costs_participant_1 = sum(epsilon_participant_1 * collision_costs_participant_1)
            sum_costs_participant_2 = sum(epsilon_participant_2 * collision_costs_participant_2)
            sum_costs_participant_3 = sum(epsilon_participant_3 * collision_costs_participant_3)

            if 'damage_potential' in self.method:
                total_accident_costs_year = sum_costs_participant_1 + sum_costs_participant_2 + sum_costs_participant_3
            elif 'causer' in self.method:
                total_accident_costs_year = sum(collision_costs_participant_1)

            total_accident_costs_pkm = total_accident_costs_year * 100 / ((annual_mileage_private + annual_mileage_shared) * occupancy_rate)
            total_accident_costs_vkm = total_accident_costs_year * 100 / (annual_mileage_private + annual_mileage_shared)

            scenario_result = {
                'scenario': f'{scenario_name}_{self.mode}',
                'cost per vkm': total_accident_costs_vkm,
                'cost per pkm': total_accident_costs_pkm,
                'cost per year': total_accident_costs_year,
            }

            scenario_results.append(scenario_result)

        self.scenario_results_df = pd.DataFrame(scenario_results)
        avg_results = self.scenario_results_df[['cost per vkm', 'cost per pkm', 'cost per year']].mean()

        self.result = {
            'cost per vkm': avg_results['cost per vkm'],
            'cost per pkm': avg_results['cost per pkm'],
            'cost per year': avg_results['cost per year'],
        }

        if is_main:
            # Save results
            results_file = os.path.join(results_directory, f"infrastructure_results_{self.mode}_{self.method}.pkl")
            with open(results_file, 'wb') as f:
                pickle.dump({
                    'result': self.result,
                    'scenario_results_df': self.scenario_results_df
                }, f)
            print(f"Results for mode '{self.mode}' and method '{self.method}' saved to '{results_file}'.")

        return self.result

    @staticmethod

    @staticmethod
    def plot_combined_distributions(scenarios, save_path="combined_distributions_external_costs_cycle_lane_scenarios.pdf"): #TODO: adapt for cycle path scenario
        """
        Plot combined histograms and density plots for infrastructure scenarios.
        """
        if not scenarios:
            print("No infrastructure scenarios provided for plotting.")
            return

        plt.rcParams.update(plt.rcParamsDefault)
        plt.style.use(['science', 'nature'])

        # Create the plot window
        fig, ax = plt.subplots(figsize=(16, 12))

        # Defined colors for consistency with other plots
        colors = [
            '#76C893',  # Darker green - Damage Potential Method
            '#1A759F',  # Medium blue - Damage Potential Method (Infrastructure)
            '#52B69A',  # Teal - Cost-by-Cause Method
            '#184E77'   # Darker blue - Cost-by-Cause Method (Infrastructure)
        ]

        # Iterate through the scenarios
        for i, (mode, method, calculator) in enumerate(scenarios):
            if 'infrastructure' not in method:
                continue

            results_df = calculator.scenario_results_df
            if results_df.empty:
                print(f"No results available for mode '{mode}' ({method}). Skipping...")
                continue

            # Extract data
            data = results_df['cost per pkm']
            mode_label = mode.replace('all_bicycle', 'c-bike').replace('all_pedelec', 'e-bike')
            label = f"{mode.replace('_', ' ').title()} ({method.replace('_', ' ').title()})"
            scenario_color = colors[i % len(colors)]

            # Plot histogram with KDE
            sns.histplot(data, kde=True, color=scenario_color, label=label, stat="density", line_kws={"linewidth": 2})

            # Calculate mean values
            mean_value = data.mean()
            count_value = len(data)

            # Vertical line for mean value in scenario color
            ax.axvline(mean_value, color=scenario_color, linestyle='-', linewidth=2, alpha=0.7)

            # Position calculation for offset labels
            label_y_pos = plt.ylim()[1] * (0.85 if i % 2 == 0 else 0.75)

            # Box for mean and count in scenario color
            ax.text(mean_value, label_y_pos, f'{mean_value:.2f}%\n(n={count_value})',  
                    color='white', fontsize=14, ha='center', va='center', fontweight='bold',
                    bbox=dict(facecolor=scenario_color, edgecolor='black', boxstyle='round,pad=0.3'))

        # Set title and axis labels
        ax.set_xlabel("Cost per PKM (€-ct)", fontsize=18)
        ax.set_ylabel("Density", fontsize=18)

        # Increase axis ticks size
        ax.tick_params(axis='both', labelsize=16)

        # Add legend
        ax.legend(title="Cycle Lane Scenarios", fontsize=14, title_fontsize=16) #TODO: adapt for cycle path scenario

        # Grid lines for better readability
        ax.grid(True, linestyle="--", alpha=0.7)

        # Save the plot
        plt.savefig(os.path.join(figures_directory, 'KDE_external_costs_cycle_lane_scenarios.pdf'), dpi=300, bbox_inches="tight") #TODO: adapt for cycle path scenario
        plt.savefig(os.path.join(figures_directory, 'KDE_external_costs_cycle_lane_scenarios.svg'), dpi=300, bbox_inches="tight") #TODO: adapt for cycle path scenario
        plt.show()


    def print_results(self): 
        """
        Print the calculated external costs in a formatted manner for both regular 
        and infrastructure scenarios.
        """
        if self.result:
            is_infrastructure = 'infrastructure' in self.method
            scenario_type = 'INFRASTRUCTURE SCENARIO' if is_infrastructure else 'STANDARD SCENARIO'

            print('\n=========================================================================================================')
            print(f'#     EXTERNAL COSTS {self.mode.upper()} ({self.method.replace("_", " ").title()}) - {scenario_type}     #')
            print('=========================================================================================================\n')
            print(f'    {self.method.replace("_", " ").title()}')

            # Print costs per vkm, pkm, and year for both standard and infrastructure methods
            print(f'         {self.method.replace("_", " ").title()} costs per vkm                 : {self.result["cost per vkm"]:6.2f} €-ct/vkm')
            print(f'         {self.method.replace("_", " ").title()} costs per pkm                 : {self.result["cost per pkm"]:6.2f} €-ct/pkm')
            print(f'         {self.method.replace("_", " ").title()} costs per year                : {self.result["cost per year"]:6.2f} €/year')

            print('-' * 50)
        else:
            print(f'Mode: {self.mode}, Method: {self.method} - No results available')
            

# Main execution
if __name__ == "__main__":
    print("Starting main execution...")

    scenarios = []
    modes_and_methods = [
        ('all_bicycle', 'damage_potential'),
        ('all_bicycle', 'causer'),
        ('all_pedelec', 'damage_potential'),
        ('all_pedelec', 'causer')
    ]

    for mode, method in modes_and_methods:
        calculator = CollisionsCalculator(mode=mode, method=method)
        results = calculator.calc_costs()
        scenarios.append((mode, method, calculator))
        calculator.print_results()

    for mode in ['all_bicycle', 'all_pedelec']:
        for method in ['damage_potential_infrastructure', 'causer_infrastructure']: 
            calculator = CollisionsCalculator(mode=mode, method=method)
            results = calculator.calc_costs()
            scenarios.append((mode, method, calculator))
            calculator.print_results()

    plot_path = os.path.join(figures_directory, "combined_distributions_external_costs_infrastructure_scenarios_cycle_lane.pdf")  #TODO: adapt for cycle path scenario
    CollisionsCalculator.plot_combined_distributions(scenarios=scenarios, save_path=plot_path)

    print("Main execution completed.")
    











