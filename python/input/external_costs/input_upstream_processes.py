class InputUpstreamProcesses:
    def __init__(self):
        """
        Initialize the InputUpstreamProcesses instance and load upstream processes data.
        """
        # Annual mileages in vkm
        self.annual_mileage_private_bicycle = 1103210000 # Source: D. Schröder, L. Kirn, J. Kinigadner, A. Loder, P. Blum, et al., „Ending the myth of mobility at zero costs: An external cost analysis,“ Research in Transportation Economics, vol. 97, p. 101246, 2022, DOI: 10.1016/j.retrec.2022.101246 + R. Follmer and J. Belz, „Mobilität in Deutschland – MiD Kurzreport Stadt München, Münchner Umland und MVV-Verbundraum,“ 2018.
        self.annual_mileage_shared_bicycle = 1487992.064 # Source: database 
        self.annual_mileage_Munich_shared_bicycle = 2066574.21 # Source: database mileage extrapolated for all shared bicycles in Munich

        self.annual_mileage_private_pedelec = 28290000 # Source: D. Schröder, L. Kirn, J. Kinigadner, A. Loder, P. Blum, et al., „Ending the myth of mobility at zero costs: An external cost analysis,“ Research in Transportation Economics, vol. 97, p. 101246, 2022, DOI: 10.1016/j.retrec.2022.101246 + R. Follmer and J. Belz, „Mobilität in Deutschland – MiD Kurzreport Stadt München, Münchner Umland und MVV-Verbundraum,“ 2018.
        self.annual_mileage_shared_pedelec = 200096.408 # Source: database 
        self.annual_mileage_Munich_shared_pedelec = 299626.408 # Source: database extrapolated for all shared pedelecs in Munich


        # life-cycle greenhouse gas emissions of private bicycle in g CO2 eq/vkm # Source:OECD/ITF, Good to go? assessing the environmental performance of new mobility, 2020
        self.GHG_emissions_manufacturing_assembly_disposal_vkm_private_bicycle = 6.688177 # GHG emissions consumption for vehicle and battery manufacturing, assembly and disposal - including fluids in [g CO2 eq/vkm]
        self.GHG_emissions_delivery_vkm_private_bicycle = 0.778913 # GHG emissions consumption for vehicle delivery at point of purchase in [g CO2 eq/vkm] 
        self.GHG_emissions_operational_services_vkm_private_bicycle = 0 # GHG emissions consumption for operational services in [g CO2 eq/vkm
        self.GHG_emissions_infrastructure_network_vkm_private_bicycle = 9.471155 # GHG emissions consumption for infrastructure network (from the vehicle perspective) in [g CO2 eq/vkm]

        # life-cycle greenhouse gas emissions of private bicycle in g CO2 eq/pkm # Sourcce: 
        self.GHG_emissions_manufacturing_assembly_disposal_pkm_private_bicycle = 6.688177
        self.GHG_emissions_delivery_pkm_private_bicycle = 0.778913
        self.GHG_emissions_operational_services_pkm_private_bicycle = 0
        self.GHG_emissions_infrastructure_network_pkm_private_bicycle = 9.471155


        # life-cycle greenhouse gas emissions of shared bicycle in g CO2 eq/vkm
        self.GHG_emissions_manufacturing_assembly_disposal_vkm_shared_bicycle = 20.760955 # GHG emissions consumption for vehicle and battery manufacturing, assembly and disposal - including fluids in [g CO2 eq/vkm]
        self.GHG_emissions_delivery_vkm_shared_bicycle = 2.551952 # GHG emissions consumption for vehicle delivery at point of purchase in [g CO2 eq/vkm] 
        self.GHG_emissions_operational_services_vkm_shared_bicycle = 24.702442 # GHG emissions consumption for operational services in [g CO2 eq/vkm
        self.GHG_emissions_infrastructure_network_vkm_shared_bicycle = 9.4896886 # GHG emissions consumption for infrastructure network (from the vehicle perspective) in [g CO2 eq/vkm]

        # life-cycle greenhouse gas emissions of shared bicycle in g CO2 eq/pkm 
        self.GHG_emissions_manufacturing_assembly_disposal_pkm_shared_bicycle = 20.760955
        self.GHG_emissions_delivery_pkm_shared_bicycle = 2.551952
        self.GHG_emissions_operational_services_pkm_shared_bicycle = 24.702442
        self.GHG_emissions_infrastructure_network_pkm_shared_bicycle = 9.4896886


        # life-cycle greenhouse gas emissions of private pedelec in g CO2 eq/vkm 
        self.GHG_emissions_manufacturing_assembly_disposal_vkm_private_pedelec = 11.4917
        self.GHG_emissions_delivery_vkm_private_pedelec = 1.046224
        self.GHG_emissions_operational_services_vkm_private_pedelec = 0
        self.GHG_emissions_infrastructure_network_vkm_private_pedelec = 9.47936

        # life-cycle greenhouse gas emissions of private pedelec in g CO2 eq/pkm
        self.GHG_emissions_manufacturing_assembly_disposal_pkm_private_pedelec = 11.4917
        self.GHG_emissions_delivery_pkm_private_pedelec = 1.046224
        self.GHG_emissions_operational_services_pkm_private_pedelec = 0
        self.GHG_emissions_infrastructure_network_pkm_private_pedelec = 9.47936


        # life-cycle greenhouse gas emissions of shared pedelec in g CO2 eq/vkm 
        self.GHG_emissions_manufacturing_assembly_disposal_vkm_shared_pedelec = 34.11538
        self.GHG_emissions_delivery_vkm_shared_pedelec = 3.0161386
        self.GHG_emissions_operational_services_vkm_shared_pedelec = 24.702442
        self.GHG_emissions_infrastructure_network_vkm_shared_pedelec = 9.5026866

        # life-cycle greenhouse gas emissions of shared pedelec in g CO2 eq/pkm
        self.GHG_emissions_manufacturing_assembly_disposal_pkm_shared_pedelec = 34.11538
        self.GHG_emissions_delivery_pkm_shared_pedelec = 3.0161386
        self.GHG_emissions_operational_services_pkm_shared_pedelec = 24.702442
        self.GHG_emissions_infrastructure_network_pkm_shared_pedelec = 9.5026866
    

        # Cost rate for carbon dioxide and other greenhouse gas emissions for 684 €-2022/t CO2-eq (0% time preference) # Source: A. Matthey and B. Bünger, Methodenkonvention 3.1 zur ermittlung von umweltkosten: Kostensätze: Stand 12/2020, Dessau-Roßlau, 2020.
        self.cost_rate_GHG_0_percent = 684

        # Cost rate for carbon dioxide and other greenhouse gas emissions for 199 €-2022/t CO2-eq (1% time preference) # Source: A. Matthey and B. Bünger, Methodenkonvention 3.1 zur ermittlung von umweltkosten: Kostensätze: Stand 12/2020, Dessau-Roßlau, 2020.
        self.cost_rate_GHG_1_percent = 199


        # Occupancy rates # Source: D. Schröder, L. Kirn, J. Kinigadner, A. Loder, P. Blum, et al., „Ending the myth of mobility at zero costs: An external cost analysis,“ Research in Transportation Economics, vol. 97, p. 101246, 2022, DOI: 10.1016/j.retrec.2022.101246
        self.occupancy_rate_private_bicycle = 1.0
        self.occupancy_rate_shared_bicycle = 1.0
        self.occupancy_rate_private_pedelec = 1.0
        self.occupancy_rate_shared_pedelec = 1.0

