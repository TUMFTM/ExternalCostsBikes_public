import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from input.external_costs.input_service_failure import InputServiceFailure

class ServiceFailureCalculator:
    def __init__(self, mode='e_scooter', method='advanced'):
        """
        Initialize the ServiceFailureCalculator instance.

        Args:
            mode (str): Vehicle mode (default: 'e_scooter').
            method (str): Calculation method (default: 'advanced').
        """
        self.mode = mode
        self.method = method
        self.input_service_failure = InputServiceFailure()
        self.tag = 'Service Failure'
        self.result = {}

        # Call the init_vehicle_modes method to initialize vehicle-specific data
        self.init_vehicle_modes()

    def init_vehicle_modes(self):
        """
        Initialize a dictionary of vehicle modes with associated data.
        """
        self.modes = {
            'private_bicycle': {
                'service_failure_factor': self.input_service_failure.service_failure_factor_private_bicycle,
                'usage_time': self.input_service_failure.usage_time_private_bicycle,
                'annual_mileage': self.input_service_failure.annual_mileage_private_bicycle,
                'occupancy_rate': self.input_service_failure.occupancy_rate_private_bicycle,
            },
            'shared_bicycle': {
                'service_failure_factor': self.input_service_failure.service_failure_factor_shared_bicycle,
                'usage_time': self.input_service_failure.usage_time_shared_bicycle,
                'annual_mileage': self.input_service_failure.annual_mileage_shared_bicycle,
                'occupancy_rate': self.input_service_failure.occupancy_rate_shared_bicycle,
            },
            'private_pedelec': {
                'service_failure_factor': self.input_service_failure.service_failure_factor_private_pedelec,
                'usage_time': self.input_service_failure.usage_time_private_pedelec,
                'annual_mileage': self.input_service_failure.annual_mileage_private_pedelec,
                'occupancy_rate': self.input_service_failure.occupancy_rate_private_pedelec,
            },
            'shared_pedelec': {
                'service_failure_factor': self.input_service_failure.service_failure_factor_shared_pedelec,
                'usage_time': self.input_service_failure.usage_time_shared_pedelec,
                'annual_mileage': self.input_service_failure.annual_mileage_shared_pedelec,
                'occupancy_rate': self.input_service_failure.occupancy_rate_shared_pedelec,
            },
        }

    def calc_costs(self):
        """
        Calculate service failure costs based on the selected 'mode'.

        Returns:
            dict: Calculated service failure costs.
        """
        if self.mode not in self.modes:
            return {'mode': 0}  # Return a default value if the mode is not recognized

        mode_data = self.modes[self.mode]

        service_failure_factor = mode_data['service_failure_factor']
        usage_time = mode_data['usage_time']
        annual_mileage = mode_data['annual_mileage']
        occupancy_rate = mode_data['occupancy_rate']

        # Calculate total service_failure costs per year in €
        total_service_failure_costs_year = (
            service_failure_factor
            * usage_time
            * self.input_service_failure.cost_per_hour_delay
        )

        # Calculate total service_failure costs per passenger-kilometer (pkm) and vehicle-kilometer (vkm)
        total_service_failure_costs_pkm = (
            total_service_failure_costs_year * 100 / (annual_mileage * occupancy_rate)
        )
        total_service_failure_costs_vkm = (
            total_service_failure_costs_year * 100 / annual_mileage
        )

        # Store the results in the 'result' dictionary
        self.result['cost per vkm'] = total_service_failure_costs_vkm
        self.result['cost per pkm'] = total_service_failure_costs_pkm
        self.result['cost per year'] = total_service_failure_costs_year

        # Return the calculated results
        return self.result
    




    
