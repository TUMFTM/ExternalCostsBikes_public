import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from input.external_costs.input_barrier_effects import InputBarrierEffects

class BarrierEffectsCalculator:
    def __init__(self, mode='private_bicycle', method='advanced'):
        """
        Initialize BarrierEffectsCalculator instance.

        Args:
            mode (str): Vehicle mode (default: 'private_bicycle').
            method (str): Calculation method (default: 'advanced').
        """
        self.mode = mode
        self.method = method
        self.input_barrier_effects = InputBarrierEffects()
        self.tag = 'Barrier Effects'
        self.result = {}

        self.init_vehicle_modes()

    def init_vehicle_modes(self):
        """
        Initialize vehicle modes and associated data.
        """
        # Initialize a dictionary of vehicle modes with associated data
        self.modes = {
            'private_bicycle': {
                'barrier_effects_vkm_2022': self.input_barrier_effects.barrier_effects_vkm_2022_private_bicycle,
                'annual_mileage': self.input_barrier_effects.annual_mileage_private_bicycle,
                'occupancy_rate': self.input_barrier_effects.occupancy_rate_private_bicycle,
            },
            'shared_bicycle': {
                'barrier_effects_vkm_2022': self.input_barrier_effects.barrier_effects_vkm_2022_shared_bicycle,
                'annual_mileage': self.input_barrier_effects.annual_mileage_Munich_shared_bicycle,
                'occupancy_rate': self.input_barrier_effects.occupancy_rate_shared_bicycle,
            },
            'private_pedelec': {
                'barrier_effects_vkm_2022': self.input_barrier_effects.barrier_effects_vkm_2022_private_pedelec,
                'annual_mileage': self.input_barrier_effects.annual_mileage_private_pedelec,
                'occupancy_rate': self.input_barrier_effects.occupancy_rate_private_pedelec,
            },
            'shared_pedelec': {
                'barrier_effects_vkm_2022': self.input_barrier_effects.barrier_effects_vkm_2022_shared_pedelec,
                'annual_mileage': self.input_barrier_effects.annual_mileage_Munich_shared_pedelec,
                'occupancy_rate': self.input_barrier_effects.occupancy_rate_shared_pedelec,
            },
        }

    def calc_costs(self):
        """
        Calculate barrier effects costs based on the selected 'mode'.

        Returns:
            dict: Calculated barrier effects costs.
        """
        # Calculate barrier effects costs based on the selected 'mode'
        if self.mode not in self.modes:
            # Return a default value if the mode is not recognized
            return {'mode': 0}

        mode_data = self.modes[self.mode]

        barrier_effects_vkm_2022 = mode_data['barrier_effects_vkm_2022']
        annual_mileage = mode_data['annual_mileage']
        occupancy_rate = mode_data['occupancy_rate']

        # Calculate total barrier effects costs per vehicle-kilometer (vkm) in €-ct2022/vkm
        total_barrier_effects_costs_vkm = barrier_effects_vkm_2022

        # Calculate total barrier effects costs per year in €
        total_barrier_effects_costs_year = (
            total_barrier_effects_costs_vkm
            * annual_mileage
            * 1 / 100
        )

        # Calculate total barrier effects costs per passenger-kilometer (pkm)
        total_barrier_effects_costs_pkm = (
            total_barrier_effects_costs_year
            * 100
            / (annual_mileage * occupancy_rate)
        )
    
        # Store the results in the 'result' dictionary
        self.result['cost per vkm'] = total_barrier_effects_costs_vkm
        self.result['cost per pkm'] = total_barrier_effects_costs_pkm
        self.result['cost per year'] = total_barrier_effects_costs_year

        # Return the calculated results
        return self.result


