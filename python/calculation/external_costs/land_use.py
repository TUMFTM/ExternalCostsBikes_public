import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from input.external_costs.input_land_use import InputLandUse

class LandUseCalculator:
    def __init__(self, mode='private_bicycle', method='standard'):
        """
        Initialize the LandUseCalculator instance.

        Args:
            mode (str): Vehicle mode (default: 'private_bicycle').
            method (str): Calculation method (default: 'standard').
        """
        self.mode = mode
        self.method = method
        self.input_land_use = InputLandUse()
        self.tag = 'Land Use'
        self.result = {}

        # Call the init_vehicle_modes method to initialize vehicle-specific data
        self.init_vehicle_modes()

    def init_vehicle_modes(self):
        """
        Initialize the vehicle mode data.

        Returns:
            dict: Data for the selected vehicle mode.
        """
        self.modes = {
            'private_bicycle': {
                'annual_mileage': self.input_land_use.annual_mileage_private_bicycle,
                'annual_mileage_Munich': self.input_land_use.annual_mileage_private_bicycle,
                'hours_idling': self.input_land_use.hours_idling_private_bicycle,
                'occupancy_rate': self.input_land_use.occupancy_rate_private_bicycle,
                'space': self.input_land_use.space_private_bicycle,
                'nr_stations': 0,
                'space_station': 0,
            },
            'shared_bicycle': {
                'annual_mileage': self.input_land_use.annual_mileage_shared_bicycle,
                'annual_mileage_Munich': self.input_land_use.annual_mileage_Munich_shared_bicycle,
                'hours_idling': self.input_land_use.hours_idling_shared_bicycle,
                'occupancy_rate': self.input_land_use.occupancy_rate_shared_bicycle,
                'space': self.input_land_use.space_shared_bicycle,
                'nr_stations': self.input_land_use.nr_stations_shared_bicycle,
                'space_station': self.input_land_use.space_station_shared_bicycle,
            },
            'private_pedelec': {
                'annual_mileage': self.input_land_use.annual_mileage_private_pedelec,
                'annual_mileage_Munich': self.input_land_use.annual_mileage_private_pedelec,
                'hours_idling': self.input_land_use.hours_idling_private_pedelec,
                'occupancy_rate': self.input_land_use.occupancy_rate_private_pedelec,
                'space': self.input_land_use.space_private_pedelec,
                'nr_stations': 0,
                'space_station': 0,
            },
            'shared_pedelec': {
                'annual_mileage': self.input_land_use.annual_mileage_shared_pedelec,
                'annual_mileage_Munich': self.input_land_use.annual_mileage_Munich_shared_pedelec,
                'hours_idling': self.input_land_use.hours_idling_shared_pedelec,
                'occupancy_rate': self.input_land_use.occupancy_rate_shared_pedelec,
                'space': self.input_land_use.space_shared_pedelec,
                'nr_stations': 0,
                'space_station': 0,
            }
        }

    def calc_costs(self):
        """
        Calculate land use costs based on the selected 'mode' and 'method'.

        Returns:
            dict: Calculated land use costs.
        """
        # Calculate land use costs based on the selected 'mode'
        if self.mode not in self.modes:
            # Return a default value if the mode is not recognized
            return {'mode': 0}

        mode_data = self.modes[self.mode]

        annual_mileage = mode_data['annual_mileage']
        annual_mileage_Munich = mode_data['annual_mileage_Munich']
        hours_idling = mode_data['hours_idling']
        occupancy_rate = mode_data['occupancy_rate']
        space = mode_data['space']
        nr_stations = mode_data['nr_stations']
        space_station = mode_data['space_station']

        sum_street_costs = sum(self.input_land_use.land_use_per_person_30kmh[type_i] * self.input_land_use.annual_mileage[type_i] for type_i in self.input_land_use.land_use_per_person_30kmh)
            
        if self.method == 'standard': # Methodology Daniel Schröder

            # Calculate the total cost of land use while moving
            total_land_use_costs_moving_year = self.input_land_use.total_infrastructure_cost_active_mobility * (annual_mileage_Munich / self.input_land_use.annual_mileage_active_modes) 

            # Calculate the land use cost of land use while parking of free-floating vehicle
            total_land_use_costs_parking_ff_year = (hours_idling / self.input_land_use.hours_per_year) * (self.input_land_use.opportunity_cost_m2_bio_diversity_costs * space)

            # Calculate the land use cost of land use while parking of station-based vehicle
            total_land_use_costs_stations_year = nr_stations * space_station * self.input_land_use.opportunity_cost_m2_bio_diversity_costs 

            total_land_use_costs_year = total_land_use_costs_moving_year + total_land_use_costs_parking_ff_year + total_land_use_costs_stations_year

            total_land_use_costs_pkm = total_land_use_costs_year / (annual_mileage * occupancy_rate) * 100
            total_land_use_costs_vkm = total_land_use_costs_year / annual_mileage * 100

            # Calculate the parking land use costs for vehicle mode in €-ct/pkm and €-ct/vkm
            total_land_use_costs_parking_pkm = total_land_use_costs_parking_ff_year / (annual_mileage * occupancy_rate) * 100
            total_land_use_costs_parking_vkm = total_land_use_costs_parking_ff_year / annual_mileage * 100

            # Calculate the stations land use costs for vehicle mode in €-ct/pkm and €-ct/vkm
            total_land_use_costs_stations_pkm = total_land_use_costs_stations_year / (annual_mileage * occupancy_rate) * 100
            total_land_use_costs_stations_vkm = total_land_use_costs_stations_year / annual_mileage * 100

            # Calculate the moving land use costs for vehicle mode in €-ct/pkm and €-ct/vkm
            total_land_use_costs_moving_pkm = total_land_use_costs_moving_year / (annual_mileage * occupancy_rate) * 100
            total_land_use_costs_moving_vkm = total_land_use_costs_moving_year / annual_mileage * 100

            self.result['cost per vkm'] = total_land_use_costs_vkm
            self.result['cost per pkm'] = total_land_use_costs_pkm
            self.result['cost per year'] = total_land_use_costs_year
                
            self.result['cost per vkm idling'] = total_land_use_costs_parking_vkm
            self.result['cost per vkm moving'] = total_land_use_costs_moving_vkm
            self.result['cost per vkm stations'] = total_land_use_costs_stations_vkm
            self.result['cost per pkm idling'] = total_land_use_costs_parking_pkm
            self.result['cost per pkm moving'] = total_land_use_costs_moving_pkm
            self.result['cost per pkm stations'] = total_land_use_costs_stations_pkm
            self.result['cost per year idling'] = total_land_use_costs_parking_ff_year
            self.result['cost per year moving'] = total_land_use_costs_moving_year
            self.result['cost per year stations'] = total_land_use_costs_stations_year

            return self.result





