import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from input.external_costs.input_upstream_processes import InputUpstreamProcesses

class UpstreamProcessesCalculator:
    def __init__(self, mode='private_bicycle', method='1_time_pref'):
        """
        Initialize the UpstreamProcessesCalculator instance.

        Args:
            mode (str): Vehicle mode (default: 'private_bicycle').
            method (str): Calculation method (default: '1_time_pref').
        """
        self.mode = mode
        self.method = method
        self.input_upstream_processes = InputUpstreamProcesses()
        self.tag = 'Upstream Processes'
        self.result = {}

        # Call the init_vehicle_modes method to initialize vehicle-specific data
        self.init_vehicle_modes()

    def init_vehicle_modes(self):
        """
        Initialize a dictionary of vehicle modes with associated data.
        """
        self.modes = {
            'private_bicycle': {
                'GHG_emissions_manufacturing_assembly_disposal_vkm': self.input_upstream_processes.GHG_emissions_manufacturing_assembly_disposal_vkm_private_bicycle,
                'GHG_emissions_manufacturing_assembly_disposal_pkm': self.input_upstream_processes.GHG_emissions_manufacturing_assembly_disposal_pkm_private_bicycle,
                'GHG_emissions_delivery_vkm': self.input_upstream_processes.GHG_emissions_delivery_vkm_private_bicycle,
                'GHG_emissions_delivery_pkm': self.input_upstream_processes.GHG_emissions_delivery_pkm_private_bicycle,
                # 'GHG_emissions_operational_services_vkm': self.input_upstream_processes.GHG_emissions_operational_services_vkm_private_bicycle,
                # 'GHG_emissions_operational_services_pkm': self.input_upstream_processes.GHG_emissions_operational_services_pkm_private_bicycle,
                # 'GHG_emissions_infrastructure_network_vkm': self.input_upstream_processes.GHG_emissions_infrastructure_network_vkm_private_bicycle,
                # 'GHG_emissions_infrastructure_network_pkm': self.input_upstream_processes.GHG_emissions_infrastructure_network_pkm_private_bicycle,
                'annual_mileage': self.input_upstream_processes.annual_mileage_private_bicycle,
            },
            'shared_bicycle': {
                'GHG_emissions_manufacturing_assembly_disposal_vkm': self.input_upstream_processes.GHG_emissions_manufacturing_assembly_disposal_vkm_shared_bicycle,
                'GHG_emissions_manufacturing_assembly_disposal_pkm': self.input_upstream_processes.GHG_emissions_manufacturing_assembly_disposal_pkm_shared_bicycle,
                'GHG_emissions_delivery_vkm': self.input_upstream_processes.GHG_emissions_delivery_vkm_shared_bicycle,
                'GHG_emissions_delivery_pkm': self.input_upstream_processes.GHG_emissions_delivery_pkm_shared_bicycle,
                # 'GHG_emissions_operational_services_vkm': self.input_upstream_processes.GHG_emissions_operational_services_vkm_shared_bicycle,
                # 'GHG_emissions_operational_services_pkm': self.input_upstream_processes.GHG_emissions_operational_services_pkm_shared_bicycle,
                # 'GHG_emissions_infrastructure_network_vkm': self.input_upstream_processes.GHG_emissions_infrastructure_network_vkm_shared_bicycle,
                # 'GHG_emissions_infrastructure_network_pkm': self.input_upstream_processes.GHG_emissions_infrastructure_network_pkm_shared_bicycle,
                'annual_mileage': self.input_upstream_processes.annual_mileage_shared_bicycle,
            },
            'private_pedelec': {
                'GHG_emissions_manufacturing_assembly_disposal_vkm': self.input_upstream_processes.GHG_emissions_manufacturing_assembly_disposal_vkm_private_pedelec,
                'GHG_emissions_manufacturing_assembly_disposal_pkm': self.input_upstream_processes.GHG_emissions_manufacturing_assembly_disposal_pkm_private_pedelec,
                'GHG_emissions_delivery_vkm': self.input_upstream_processes.GHG_emissions_delivery_vkm_private_pedelec,
                'GHG_emissions_delivery_pkm': self.input_upstream_processes.GHG_emissions_delivery_pkm_private_pedelec,
                # 'GHG_emissions_operational_services_vkm': self.input_upstream_processes.GHG_emissions_operational_services_vkm_private_pedelec,
                # 'GHG_emissions_operational_services_pkm': self.input_upstream_processes.GHG_emissions_operational_services_pkm_private_pedelec,
                # 'GHG_emissions_infrastructure_network_vkm': self.input_upstream_processes.GHG_emissions_infrastructure_network_vkm_private_pedelec,
                # 'GHG_emissions_infrastructure_network_pkm': self.input_upstream_processes.GHG_emissions_infrastructure_network_pkm_private_pedelec,
                'annual_mileage': self.input_upstream_processes.annual_mileage_private_pedelec,
            },
            'shared_pedelec': {
                'GHG_emissions_manufacturing_assembly_disposal_vkm': self.input_upstream_processes.GHG_emissions_manufacturing_assembly_disposal_vkm_shared_pedelec,
                'GHG_emissions_manufacturing_assembly_disposal_pkm': self.input_upstream_processes.GHG_emissions_manufacturing_assembly_disposal_pkm_shared_pedelec,
                'GHG_emissions_delivery_vkm': self.input_upstream_processes.GHG_emissions_delivery_vkm_shared_pedelec,
                'GHG_emissions_delivery_pkm': self.input_upstream_processes.GHG_emissions_delivery_pkm_shared_pedelec,
                # 'GHG_emissions_operational_services_vkm': self.input_upstream_processes.GHG_emissions_operational_services_vkm_shared_pedelec,
                # 'GHG_emissions_operational_services_pkm': self.input_upstream_processes.GHG_emissions_operational_services_pkm_shared_pedelec,
                # 'GHG_emissions_infrastructure_network_vkm': self.input_upstream_processes.GHG_emissions_infrastructure_network_vkm_shared_pedelec,
                # 'GHG_emissions_infrastructure_network_pkm': self.input_upstream_processes.GHG_emissions_infrastructure_network_pkm_shared_pedelec,
                'annual_mileage': self.input_upstream_processes.annual_mileage_shared_pedelec,
            }

        }


    def calc_costs(self):
            """
            Calculate upstream processes costs based on the selected 'mode' and 'method'.

            Returns:
                dict: Calculated upstream processes costs.
            """
            if self.mode not in self.modes:
                return {'mode': 0}  # Return a default value if the mode is not recognized

            mode_data = self.modes[self.mode]

            GHG_emissions_manufacturing_assembly_disposal_vkm = mode_data['GHG_emissions_manufacturing_assembly_disposal_vkm']
            GHG_emissions_manufacturing_assembly_disposal_pkm = mode_data['GHG_emissions_manufacturing_assembly_disposal_pkm']
            GHG_emissions_delivery_vkm = mode_data['GHG_emissions_delivery_vkm']
            GHG_emissions_delivery_pkm = mode_data['GHG_emissions_delivery_pkm']
            # GHG_emissions_operational_services_vkm = mode_data['GHG_emissions_operational_services_vkm']
            # GHG_emissions_operational_services_pkm = mode_data['GHG_emissions_operational_services_pkm']
            # GHG_emissions_infrastructure_network_vkm = mode_data['GHG_emissions_infrastructure_network_vkm']
            # GHG_emissions_infrastructure_network_pkm = mode_data['GHG_emissions_infrastructure_network_pkm']
            annual_mileage = mode_data['annual_mileage']


            if self.method == '0_time_pref':
                
                # calculate the total upstream processes costs in €-ct/pkm & vkm
                total_upstream_processes_costs_vkm_0_percent = (GHG_emissions_manufacturing_assembly_disposal_vkm + GHG_emissions_delivery_vkm) * (100 / 1000000) * self.input_upstream_processes.cost_rate_GHG_0_percent # + GHG_emissions_operational_services_vkm + GHG_emissions_infrastructure_network_vkm

                total_upstream_processes_costs_pkm_0_percent = (GHG_emissions_manufacturing_assembly_disposal_pkm + GHG_emissions_delivery_pkm) * (100 / 1000000) * self.input_upstream_processes.cost_rate_GHG_0_percent # + GHG_emissions_operational_services_pkm + GHG_emissions_infrastructure_network_pkm

                # calculate the total upstream processes costs in €/year
                total_upstream_processes_costs_year_0_percent = total_upstream_processes_costs_vkm_0_percent  * annual_mileage / 100

                self.result['cost per vkm'] = total_upstream_processes_costs_vkm_0_percent
                self.result['cost per pkm'] = total_upstream_processes_costs_pkm_0_percent
                self.result['cost per year'] = total_upstream_processes_costs_year_0_percent
                    
                return self.result
                
            
            elif self.method == '1_time_pref':
                
                # calculate the total upstream processes costs in €-ct/pkm & vkm
                total_upstream_processes_costs_vkm_1_percent = (GHG_emissions_manufacturing_assembly_disposal_vkm + GHG_emissions_delivery_vkm) * (100 / 1000000) * self.input_upstream_processes.cost_rate_GHG_1_percent # + GHG_emissions_operational_services_vkm + GHG_emissions_infrastructure_network_vkm

                total_upstream_processes_costs_pkm_1_percent = (GHG_emissions_manufacturing_assembly_disposal_pkm + GHG_emissions_delivery_pkm) * (100 / 1000000) * self.input_upstream_processes.cost_rate_GHG_1_percent # + GHG_emissions_operational_services_pkm  + GHG_emissions_infrastructure_network_pkm

                # calculate the total upstream processes costs in €/year
                total_upstream_processes_costs_year_1_percent = total_upstream_processes_costs_vkm_1_percent * annual_mileage / 100

                #return total_upstream_processes_costs_vkm_1_percent & total_upstream_processes_costs_pkm_1_percent & total_upstream_processes_costs_year_1_percent
                self.result['cost per vkm'] = total_upstream_processes_costs_vkm_1_percent
                self.result['cost per pkm'] = total_upstream_processes_costs_pkm_1_percent
                self.result['cost per year'] = total_upstream_processes_costs_year_1_percent
                    
                return self.result


calculator = UpstreamProcessesCalculator(mode='shared_bicycle', method='1_time_pref')

result = calculator.calc_costs()

if calculator.mode == 'shared_bicycle':

    print('Results for mode shared_bicycle:')
    print('Cost per vkm:', result['cost per vkm'])
    print('Cost per pkm:', result['cost per pkm'])
    print('Cost per year:', result['cost per year'])
    