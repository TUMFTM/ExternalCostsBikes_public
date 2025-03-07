import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from input.external_costs.input_climate_change import InputClimateChange

class ClimateChangeCalculator:
    ENERGY_TYPES = ['Water power', 'Wind energy', 'Solar power', 'Bio mass', 'Brown coal', 'Black coal', 'Gas', 'Oil', 'Nuclear energy']

    def __init__(self, mode='private_bicycle', method='1_time_pref'):
        """
        Initialize ClimateChangeCalculator instance.

        Args:
            mode (str): Vehicle mode (default: 'private_bicycle').
            method (str): Calculation method (default: '1_time_pref').
        """
        self.mode = mode
        self.method = method
        self.input_climate_change = InputClimateChange()
        self.tag = 'Climate Change'
        self.result = {}

        self.init_vehicle_modes()

    def init_vehicle_modes(self):
        """
        Initialize vehicle modes and associated data.
        """
        # Initialize a dictionary of vehicle modes with associated data
        self.modes = {
            'private_bicycle': {
                'power_consumption_driving_vkm': self.input_climate_change.power_consumption_driving_vkm_private_bicycle,
                'power_consumption_idling_vkm': self.input_climate_change.power_consumption_idling_vkm_private_bicycle,
                'annual_mileage': self.input_climate_change.annual_mileage_private_bicycle,
                'occupancy_rate': self.input_climate_change.occupancy_rate_private_bicycle,
            },
            'shared_bicycle': {
                'power_consumption_driving_vkm': self.input_climate_change.power_consumption_driving_vkm_shared_bicycle,
                'power_consumption_idling_vkm': self.input_climate_change.power_consumption_idling_vkm_shared_bicycle,
                'annual_mileage': self.input_climate_change.annual_mileage_shared_bicycle,
                'occupancy_rate': self.input_climate_change.occupancy_rate_shared_bicycle,
            },
            'private_pedelec': {
                'power_consumption_driving_vkm': self.input_climate_change.power_consumption_driving_vkm_private_pedelec,
                'power_consumption_idling_vkm': self.input_climate_change.power_consumption_idling_vkm_private_pedelec,
                'annual_mileage': self.input_climate_change.annual_mileage_private_pedelec,
                'occupancy_rate': self.input_climate_change.occupancy_rate_private_pedelec,
            },
            'shared_pedelec': {
                'power_consumption_driving_vkm': self.input_climate_change.power_consumption_driving_vkm_shared_pedelec,
                'power_consumption_idling_vkm': self.input_climate_change.power_consumption_idling_vkm_shared_pedelec,
                'annual_mileage': self.input_climate_change.annual_mileage_shared_pedelec,
                'occupancy_rate': self.input_climate_change.occupancy_rate_shared_pedelec,
            },
        }

    def calc_costs(self):
        """
        Calculate climate change costs based on the selected 'mode' and 'method'.

        Returns:
            dict: Calculated climate change costs.
        """
        # Calculate climate change costs based on the selected 'mode'
        if self.mode not in self.modes:
            # Return a default value if the mode is not recognized
            return {'mode': 0}

        mode_data = self.modes[self.mode]

        power_consumption_driving_vkm = mode_data['power_consumption_driving_vkm']
        power_consumption_idling_vkm = mode_data['power_consumption_idling_vkm']
        annual_mileage = mode_data['annual_mileage']
        occupancy_rate = mode_data['occupancy_rate']

        if self.method == '0_time_pref':
        
                total_energy_production_costs_vkm_per_energy_type_0_percent = []
                total_energy_production_costs_pkm_per_energy_type_0_percent = []
                total_energy_production_costs_year_per_energy_type_0_percent = []

                # Calculate for the entire Power Mix
                power_mix_cost_total_0_percent = sum(self.input_climate_change.power_mix_share[energy_type] * self.input_climate_change.climate_costs_0_percent[energy_type] for energy_type in self.ENERGY_TYPES)

                for energy_type in self.ENERGY_TYPES:
                    climate_costs_0_percent = self.input_climate_change.climate_costs_0_percent[energy_type]
                    power_mix_share = self.input_climate_change.power_mix_share[energy_type]

                    energy_production_costs_driving_0_percent = power_consumption_driving_vkm * (power_mix_share * climate_costs_0_percent) * self.input_climate_change.net_loss_factor * self.input_climate_change.charging_loss_factor
                    energy_production_costs_idling_0_percent = power_consumption_idling_vkm * (power_mix_share * climate_costs_0_percent) * self.input_climate_change.net_loss_factor * self.input_climate_change.charging_loss_factor

                    total_energy_production_costs_vkm_0_percent = energy_production_costs_driving_0_percent + energy_production_costs_idling_0_percent
                    total_energy_production_costs_year_0_percent = total_energy_production_costs_vkm_0_percent * annual_mileage * 1 / 100 
                    total_energy_production_costs_pkm_0_percent = total_energy_production_costs_year_0_percent * 100 * 1 / (annual_mileage * occupancy_rate) 

                    total_energy_production_costs_vkm_per_energy_type_0_percent.append(total_energy_production_costs_vkm_0_percent)
                    total_energy_production_costs_year_per_energy_type_0_percent.append(total_energy_production_costs_year_0_percent)
                    total_energy_production_costs_pkm_per_energy_type_0_percent.append(total_energy_production_costs_pkm_0_percent)

                # Calculate total climate change costs in €-ct/vkm at 0% time preference rate
                total_climate_change_costs_vkm_total_0_percent = power_mix_cost_total_0_percent * (power_consumption_driving_vkm + power_consumption_idling_vkm) * self.input_climate_change.net_loss_factor * self.input_climate_change.charging_loss_factor

                # Calculate climate change costs by energy production driving in €-ct/vkm  at 0% time preference rate
                total_climate_change_costs_vkm_driving_0_percent = power_mix_cost_total_0_percent * power_consumption_driving_vkm * self.input_climate_change.net_loss_factor * self.input_climate_change.charging_loss_factor 

                # Calculate climate change costs by energy production idling in €-ct/vkm at 0% time preference rate
                total_climate_change_costs_vkm_idling_0_percent = power_mix_cost_total_0_percent * power_consumption_idling_vkm * self.input_climate_change.net_loss_factor * self.input_climate_change.charging_loss_factor 


                # Calculate total climate change costs in €/year at 0% time preference rate
                total_climate_change_costs_year_total_0_percent = total_climate_change_costs_vkm_total_0_percent * annual_mileage * 1 / 100

                # Calculate total climate change costs driving in €/year at 0% time preference rate
                total_climate_change_costs_year_driving_0_percent = total_climate_change_costs_vkm_driving_0_percent * annual_mileage * 1 / 100

                # Calculate total climate change costs idling in €/year at 0% time preference rate
                total_climate_change_costs_year_idling_0_percent = total_climate_change_costs_vkm_idling_0_percent * annual_mileage * 1 / 100


                # Calculate total climate change costs in €-ct/pkm at 0% time preference rate
                total_climate_change_costs_pkm_total_0_percent = total_climate_change_costs_year_total_0_percent * 100 / (annual_mileage * occupancy_rate)

                # Calculate total climate change costs driving in €-ct/pkm at 0% time preference rate
                total_climate_change_costs_pkm_driving_0_percent = total_climate_change_costs_year_driving_0_percent * 100 / (annual_mileage * occupancy_rate)

                # Calculate total climate change costs idling in €-ct/pkm
                total_climate_change_costs_pkm_idling_0_percent = total_climate_change_costs_year_idling_0_percent * 100 / (annual_mileage * occupancy_rate) 


                # Save results for the entire Power Mix at 0% time preference rate
                self.result['cost per vkm'] = total_climate_change_costs_vkm_total_0_percent
                self.result['cost per vkm driving'] = total_climate_change_costs_vkm_driving_0_percent
                self.result['cost per vkm idling'] = total_climate_change_costs_vkm_idling_0_percent
                self.result['cost per pkm'] = total_climate_change_costs_pkm_total_0_percent
                self.result['cost per pkm driving'] = total_climate_change_costs_pkm_driving_0_percent
                self.result['cost per pkm idling'] = total_climate_change_costs_pkm_idling_0_percent
                self.result['cost per year'] = total_climate_change_costs_year_total_0_percent
                self.result['cost per year driving'] = total_climate_change_costs_year_driving_0_percent
                self.result['cost per year idling'] = total_climate_change_costs_year_idling_0_percent

                self.result['Energy production cost per vkm by energy type'] = total_energy_production_costs_vkm_per_energy_type_0_percent
                self.result['Energy production cost per pkm by energy type'] = total_energy_production_costs_pkm_per_energy_type_0_percent
                self.result['Energy production cost per year by energy type'] = total_energy_production_costs_year_per_energy_type_0_percent

                return self.result
            

        if self.method == '1_time_pref':

            total_energy_production_costs_vkm_per_energy_type_1_percent = []
            total_energy_production_costs_pkm_per_energy_type_1_percent = []
            total_energy_production_costs_year_per_energy_type_1_percent = []

            # Calculate for the entire Power Mix
            power_mix_cost_total_1_percent = sum(self.input_climate_change.power_mix_share[energy_type] * self.input_climate_change.climate_costs_1_percent[energy_type] for energy_type in self.ENERGY_TYPES)

            for energy_type in self.ENERGY_TYPES:
                climate_costs_1_percent = self.input_climate_change.climate_costs_1_percent[energy_type]
                power_mix_share = self.input_climate_change.power_mix_share[energy_type]

                energy_production_costs_driving_1_percent = power_consumption_driving_vkm * (power_mix_share * climate_costs_1_percent) * self.input_climate_change.net_loss_factor * self.input_climate_change.charging_loss_factor
                energy_production_costs_idling_1_percent = power_consumption_idling_vkm * (power_mix_share * climate_costs_1_percent) * self.input_climate_change.net_loss_factor * self.input_climate_change.charging_loss_factor

                total_energy_production_costs_vkm_1_percent = energy_production_costs_driving_1_percent + energy_production_costs_idling_1_percent
                total_energy_production_costs_year_1_percent = total_energy_production_costs_vkm_1_percent * annual_mileage * 1 / 100
                total_energy_production_costs_pkm_1_percent = total_energy_production_costs_year_1_percent * 100 * 1 / (annual_mileage * occupancy_rate)

                total_energy_production_costs_vkm_per_energy_type_1_percent.append(total_energy_production_costs_vkm_1_percent)
                total_energy_production_costs_year_per_energy_type_1_percent.append(total_energy_production_costs_year_1_percent)
                total_energy_production_costs_pkm_per_energy_type_1_percent.append(total_energy_production_costs_pkm_1_percent)

            # Calculate total climate change costs in €-ct/vkm at 1% time preference rate
            total_climate_change_costs_vkm_total_1_percent = power_mix_cost_total_1_percent * (power_consumption_driving_vkm + power_consumption_idling_vkm) * self.input_climate_change.net_loss_factor * self.input_climate_change.charging_loss_factor

            # Calculate climate change costs by energy production driving in €-ct/vkm at 1% time preference rate
            total_climate_change_costs_vkm_driving_1_percent = power_mix_cost_total_1_percent * power_consumption_driving_vkm * self.input_climate_change.net_loss_factor * self.input_climate_change.charging_loss_factor

            # Calculate climate change costs by energy production idling in €-ct/vkm at 1% time preference rate
            total_climate_change_costs_vkm_idling_1_percent = power_mix_cost_total_1_percent * power_consumption_idling_vkm * self.input_climate_change.net_loss_factor * self.input_climate_change.charging_loss_factor


            # Calculate total climate change costs in €/year at 1% time preference rate
            total_climate_change_costs_year_total_1_percent = total_climate_change_costs_vkm_total_1_percent * annual_mileage * 1 / 100

            # Calculate total climate change costs driving in €/year at 1% time preference rate
            total_climate_change_costs_year_driving_1_percent = total_climate_change_costs_vkm_driving_1_percent * annual_mileage * 1 / 100

            # Calculate total climate change costs idling in €/year at 1% time preference rate
            total_climate_change_costs_year_idling_1_percent = total_climate_change_costs_vkm_idling_1_percent * annual_mileage * 1 / 100


            # Calculate total climate change costs in €-ct/pkm at 1% time preference rate
            total_climate_change_costs_pkm_total_1_percent = total_climate_change_costs_year_total_1_percent * 100 / (annual_mileage * occupancy_rate)

            # Calculate total climate change costs driving in €-ct/pkm at 1% time preference rate
            total_climate_change_costs_pkm_driving_1_percent = total_climate_change_costs_year_driving_1_percent * 100 / (annual_mileage * occupancy_rate)

            # Calculate total climate change costs idling in €-ct/pkm at 1% time preference rate
            total_climate_change_costs_pkm_idling_1_percent = total_climate_change_costs_year_idling_1_percent * 100 / (annual_mileage * occupancy_rate)

            # Save results for the entire Power Mix at 1% time preference rate
            self.result['cost per vkm'] = total_climate_change_costs_vkm_total_1_percent
            self.result['cost per vkm driving'] = total_climate_change_costs_vkm_driving_1_percent
            self.result['cost per vkm idling'] = total_climate_change_costs_vkm_idling_1_percent
            self.result['cost per pkm'] = total_climate_change_costs_pkm_total_1_percent
            self.result['cost per pkm driving'] = total_climate_change_costs_pkm_driving_1_percent
            self.result['cost per pkm idling'] = total_climate_change_costs_pkm_idling_1_percent
            self.result['cost per year'] = total_climate_change_costs_year_total_1_percent
            self.result['cost per year driving'] = total_climate_change_costs_year_driving_1_percent
            self.result['cost per year idling'] = total_climate_change_costs_year_idling_1_percent


            self.result['Energy production cost per vkm by energy type'] = total_energy_production_costs_vkm_per_energy_type_1_percent
            self.result['Energy production cost per pkm by energy type'] = total_energy_production_costs_pkm_per_energy_type_1_percent
            self.result['Energy production cost per year by energy type'] = total_energy_production_costs_year_per_energy_type_1_percent

            return self.result
        
