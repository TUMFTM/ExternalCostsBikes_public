import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from input.external_costs.input_health_benefits import InputHealthBenefits

class HealthBenefitsCalculator:
    def __init__(self, mode='private_bicycle', method='advanced'):
        """
        Initialize the HealthBenefitsCalculator instance.

        Args:
            mode (str): Vehicle mode (default: 'private_bicycle').
            method (str): Calculation method (default: 'advanced').
        """
        self.mode = mode
        self.method = method
        self.input_health_benefits = InputHealthBenefits()
        self.tag = 'Health Benefits'
        self.result = {}

        # Call the init_vehicle_modes method to initialize vehicle-specific data
        self.init_vehicle_modes()

    def init_vehicle_modes(self):
        """
        Initialize a dictionary of vehicle modes with associated data.
        """
        self.modes = {
            'private_bicycle': {
                'avoided_deaths': self.input_health_benefits.avoided_deaths_private_bicycle,
                'annual_mileage': self.input_health_benefits.annual_mileage_private_bicycle,
                'occupancy_rate': self.input_health_benefits.occupancy_rate_private_bicycle,
            },
            'shared_bicycle': {
                'avoided_deaths': self.input_health_benefits.avoided_deaths_shared_bicycle,
                'annual_mileage': self.input_health_benefits.annual_mileage_shared_bicycle,
                'occupancy_rate': self.input_health_benefits.occupancy_rate_shared_bicycle,
            },
            'private_pedelec': {
                'avoided_deaths': self.input_health_benefits.avoided_deaths_private_pedelec,
                'annual_mileage': self.input_health_benefits.annual_mileage_private_pedelec,
                'occupancy_rate': self.input_health_benefits.occupancy_rate_private_pedelec,
            },
            'shared_pedelec': {
                'avoided_deaths': self.input_health_benefits.avoided_deaths_shared_pedelec,
                'annual_mileage': self.input_health_benefits.annual_mileage_shared_pedelec,
                'occupancy_rate': self.input_health_benefits.occupancy_rate_shared_pedelec,
            },
        }

    def calc_costs(self):
        """
        Calculate health benefits costs based on the selected 'mode'.

        Returns:
            dict: Calculated health benefits costs.
        """
        if self.mode not in self.modes:
            return {'mode': 0}  # Return a default value if the mode is not recognized

        mode_data = self.modes[self.mode]

        avoided_deaths = mode_data['avoided_deaths']
        annual_mileage = mode_data['annual_mileage']
        occupancy_rate = mode_data['occupancy_rate']
        value_of_statistical_life = self.input_health_benefits.value_of_statistical_life

        # Calculate total health benefits costs per year in €
        total_health_benefits_costs_year = -(
            avoided_deaths
            * value_of_statistical_life
            * annual_mileage
            / (
                self.input_health_benefits.annual_mileage_private_bicycle
                + self.input_health_benefits.annual_mileage_shared_bicycle
                + self.input_health_benefits.annual_mileage_private_pedelec
                + self.input_health_benefits.annual_mileage_shared_pedelec
            )
        )

        # Calculate total health benefits costs per passenger-kilometer (pkm) and vehicle-kilometer (vkm)
        total_health_benefits_costs_pkm = (
            total_health_benefits_costs_year * 100 / (annual_mileage * occupancy_rate)
        )
        total_health_benefits_costs_vkm = (
            total_health_benefits_costs_year * 100 / annual_mileage
        )

        # Store the results in the 'result' dictionary
        self.result['cost per vkm'] = total_health_benefits_costs_vkm
        self.result['cost per pkm'] = total_health_benefits_costs_pkm
        self.result['cost per year'] = total_health_benefits_costs_year

        # Return the calculated results
        return self.result

