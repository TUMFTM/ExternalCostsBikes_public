import os
import sys

# Add a directory path to the Python system path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from input.external_costs.input_air_pollution import InputAirPollution

class AirPollutionCalculator:
    ENERGY_TYPES = ['Water power', 'Wind energy', 'Solar power', 'Bio mass', 'Brown coal', 'Black coal', 'Gas', 'Oil', 'Nuclear energy']

    def __init__(self, mode='private_bicycle', method='advanced'):
        """
        Initialize AirPollutionCalculator instance.

        Args:
            mode (str): Vehicle mode (default: 'private_bicycle').
            method (str): Calculation method (default: 'advanced').
        """
        self.mode = mode
        self.method = method
        self.input_air_pollution = InputAirPollution()
        self.tag = 'Air Pollution'
        self.result = {}

        self.init_vehicle_modes()

    def init_vehicle_modes(self):
        """
        Initialize vehicle modes and associated data.
        """
        # Initialize a dictionary of vehicle modes with associated data
        self.modes = {
            'private_bicycle': {
                'power_consumption_driving_vkm': self.input_air_pollution.power_consumption_driving_vkm_private_bicycle,
                'power_consumption_idling_vkm': self.input_air_pollution.power_consumption_idling_vkm_private_bicycle,
                'exhaust_cost': self.input_air_pollution.exhaust_cost_private_bicycle,
                'abrasion_cost': self.input_air_pollution.abrasion_cost_private_bicycle,
                'annual_mileage': self.input_air_pollution.annual_mileage_private_bicycle,
                'occupancy_rate': self.input_air_pollution.occupancy_rate_private_bicycle,
            },
            'shared_bicycle': {
                'power_consumption_driving_vkm': self.input_air_pollution.power_consumption_driving_vkm_shared_bicycle,
                'power_consumption_idling_vkm': self.input_air_pollution.power_consumption_idling_vkm_shared_bicycle,
                'exhaust_cost': self.input_air_pollution.exhaust_cost_shared_bicycle,
                'abrasion_cost': self.input_air_pollution.abrasion_cost_shared_bicycle,
                'annual_mileage': self.input_air_pollution.annual_mileage_shared_bicycle,
                'occupancy_rate': self.input_air_pollution.occupancy_rate_shared_bicycle,
            },
            'private_pedelec': {
                'power_consumption_driving_vkm': self.input_air_pollution.power_consumption_driving_vkm_private_pedelec,
                'power_consumption_idling_vkm': self.input_air_pollution.power_consumption_idling_vkm_private_pedelec,
                'exhaust_cost': self.input_air_pollution.exhaust_cost_private_pedelec,
                'abrasion_cost': self.input_air_pollution.abrasion_cost_private_pedelec,
                'annual_mileage': self.input_air_pollution.annual_mileage_private_pedelec,
                'occupancy_rate': self.input_air_pollution.occupancy_rate_private_pedelec,
            },
            'shared_pedelec': {
                'power_consumption_driving_vkm': self.input_air_pollution.power_consumption_driving_vkm_shared_pedelec,
                'power_consumption_idling_vkm': self.input_air_pollution.power_consumption_idling_vkm_shared_pedelec,
                'exhaust_cost': self.input_air_pollution.exhaust_cost_shared_pedelec,
                'abrasion_cost': self.input_air_pollution.abrasion_cost_shared_pedelec,
                'annual_mileage': self.input_air_pollution.annual_mileage_shared_pedelec,
                'occupancy_rate': self.input_air_pollution.occupancy_rate_shared_pedelec,
            },
        }

    def calc_costs(self):
        """
        Calculate air pollution costs based on the selected mode.

        Returns:
            dict: Calculated air pollution costs.
        """
        if self.mode not in self.modes:
            return {'mode': 0}

        mode_data = self.modes[self.mode]
        power_consumption_driving_vkm = mode_data['power_consumption_driving_vkm']
        power_consumption_idling_vkm = mode_data['power_consumption_idling_vkm']
        exhaust_cost = mode_data['exhaust_cost']
        abrasion_cost = mode_data['abrasion_cost']
        annual_mileage = mode_data['annual_mileage']
        occupancy_rate = mode_data['occupancy_rate']

        if self.method == 'advanced':

                total_energy_production_costs_vkm_per_energy_type = []
                total_energy_production_costs_pkm_per_energy_type = []
                total_energy_production_costs_year_per_energy_type = []

                # Calculate for the entire Power Mix
                power_mix_cost_total = sum(self.input_air_pollution.power_mix_share[energy_type] * self.input_air_pollution.pollution_costs[energy_type] for energy_type in self.ENERGY_TYPES)

                for energy_type in self.ENERGY_TYPES:
                    pollution_cost = self.input_air_pollution.pollution_costs[energy_type]
                    power_mix_share = self.input_air_pollution.power_mix_share[energy_type]

                    energy_production_costs_driving = power_consumption_driving_vkm * (power_mix_share * pollution_cost) * self.input_air_pollution.net_loss_factor * self.input_air_pollution.charging_loss_factor
                    energy_production_costs_idling = power_consumption_idling_vkm * (power_mix_share * pollution_cost) * self.input_air_pollution.net_loss_factor * self.input_air_pollution.charging_loss_factor

                    total_energy_production_costs_vkm = energy_production_costs_driving + energy_production_costs_idling
                    total_energy_production_costs_year = total_energy_production_costs_vkm * annual_mileage * 1 / 100 
                    total_energy_production_costs_pkm = total_energy_production_costs_year * 100 * 1 / (annual_mileage * occupancy_rate) 

                    total_energy_production_costs_vkm_per_energy_type.append(total_energy_production_costs_vkm)
                    total_energy_production_costs_year_per_energy_type.append(total_energy_production_costs_year)
                    total_energy_production_costs_pkm_per_energy_type.append(total_energy_production_costs_pkm)

                # Calculate total air pollution costs in €-ct/vkm
                total_air_pollution_costs_vkm_total = power_mix_cost_total * (power_consumption_driving_vkm + power_consumption_idling_vkm) * self.input_air_pollution.net_loss_factor * self.input_air_pollution.charging_loss_factor + exhaust_cost + abrasion_cost

                # Calculate air pollution costs by energy production driving in €-ct/vkm
                total_air_pollution_costs_vkm_driving = power_mix_cost_total * power_consumption_driving_vkm * self.input_air_pollution.net_loss_factor * self.input_air_pollution.charging_loss_factor 

                # Calculate air pollution costs by energy production idling in €-ct/vkm
                total_air_pollution_costs_vkm_idling = power_mix_cost_total * power_consumption_idling_vkm * self.input_air_pollution.net_loss_factor * self.input_air_pollution.charging_loss_factor 

                # Calculate air pollution costs by abrasion in €-ct/vkm
                total_air_pollution_costs_vkm_abrasion = abrasion_cost

                # Calculate total air pollution costs in €/year
                total_air_pollution_costs_year_total = total_air_pollution_costs_vkm_total * annual_mileage * 1 / 100

                # Calculate total air pollution costs driving in €/year
                total_air_pollution_costs_year_driving = total_air_pollution_costs_vkm_driving * annual_mileage * 1 / 100

                # Calculate total air pollution costs idling in €/year
                total_air_pollution_costs_year_idling = total_air_pollution_costs_vkm_idling * annual_mileage * 1 / 100

                # Calculate air pollution costs by abrasion in €/year
                total_air_pollution_costs_year_abrasion = total_air_pollution_costs_vkm_abrasion * annual_mileage * 1 / 100


                # Calculate total air pollution costs in €-ct/pkm
                total_air_pollution_costs_pkm_total = total_air_pollution_costs_year_total * 100 / (annual_mileage * occupancy_rate)

                # Calculate total air pollution costs driving in €-ct/pkm
                total_air_pollution_costs_pkm_driving = total_air_pollution_costs_year_driving * 100 / (annual_mileage * occupancy_rate)

                # Calculate total air pollution costs idling in €-ct/pkm
                total_air_pollution_costs_pkm_idling = total_air_pollution_costs_year_idling * 100 / (annual_mileage * occupancy_rate) 

                # Calculate air pollution costs by abrasion in €-ct/pkm
                total_air_pollution_costs_pkm_abrasion = total_air_pollution_costs_year_abrasion * 100 / (annual_mileage * occupancy_rate) 


                # Save results for the entire Power Mix
                self.result['cost per vkm'] = total_air_pollution_costs_vkm_total
                self.result['cost per vkm driving'] = total_air_pollution_costs_vkm_driving
                self.result['cost per vkm idling'] = total_air_pollution_costs_vkm_idling
                self.result['cost per vkm abrasion'] = total_air_pollution_costs_vkm_abrasion
                self.result['cost per pkm'] = total_air_pollution_costs_pkm_total
                self.result['cost per pkm driving'] = total_air_pollution_costs_pkm_driving
                self.result['cost per pkm idling'] = total_air_pollution_costs_pkm_idling
                self.result['cost per pkm abrasion'] = total_air_pollution_costs_pkm_abrasion
                self.result['cost per year'] = total_air_pollution_costs_year_total
                self.result['cost per year driving'] = total_air_pollution_costs_year_driving
                self.result['cost per year idling'] = total_air_pollution_costs_year_idling
                self.result['cost per year abrasion'] = total_air_pollution_costs_year_abrasion

                self.result['Energy production cost per vkm by energy type'] = total_energy_production_costs_vkm_per_energy_type
                self.result['Energy production cost per pkm by energy type'] = total_energy_production_costs_pkm_per_energy_type
                self.result['Energy production cost per year by energy type'] = total_energy_production_costs_year_per_energy_type

                return self.result
    
