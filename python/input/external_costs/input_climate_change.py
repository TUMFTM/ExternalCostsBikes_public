class InputClimateChange:
    def __init__(self):
        """
        Initialize the InputClimateChange instance and load climate change data.
        """
        # Annual mileages in vkm
        self.annual_mileage_private_bicycle = 1103210000 # Source: D. Schröder, L. Kirn, J. Kinigadner, A. Loder, P. Blum, et al., „Ending the myth of mobility at zero costs: An external cost analysis,“ Research in Transportation Economics, vol. 97, p. 101246, 2022, DOI: 10.1016/j.retrec.2022.101246 + R. Follmer and J. Belz, „Mobilität in Deutschland – MiD Kurzreport Stadt München, Münchner Umland und MVV-Verbundraum,“ 2018.
        self.annual_mileage_shared_bicycle = 1487992.064 # Source: database 
        self.annual_mileage_Munich_shared_bicycle = 2066574.21 # Source: database mileage extrapolated for all shared bicycles in Munich

        self.annual_mileage_private_pedelec = 28290000 # Source: D. Schröder, L. Kirn, J. Kinigadner, A. Loder, P. Blum, et al., „Ending the myth of mobility at zero costs: An external cost analysis,“ Research in Transportation Economics, vol. 97, p. 101246, 2022, DOI: 10.1016/j.retrec.2022.101246 + R. Follmer and J. Belz, „Mobilität in Deutschland – MiD Kurzreport Stadt München, Münchner Umland und MVV-Verbundraum,“ 2018.
        self.annual_mileage_shared_pedelec = 200096.408 # Source: database 
        self.annual_mileage_Munich_shared_pedelec = 299626.408 # Source: database extrapolated for all shared pedelecs in Munich

        # Power consumptions driving in kWh/vkm
        self.power_consumption_driving_vkm_private_bicycle = 0
        self.power_consumption_driving_vkm_shared_bicycle = 0
        self.power_consumption_driving_vkm_private_pedelec = 0.007 # König, A., Nicoletti, L., Schröder, D., Wolff, S., Waclaw, A., Lienkamp, M., 2021b. An Overview of Parameter and Cost for Battery Electric Vehicles. WEVJ 12, 21. 10.3390/wevj12010021
        self.power_consumption_driving_vkm_shared_pedelec = 0.0222 # Source: database

        # Power consumptions idling in kWh/vkm
        self.power_consumption_idling_vkm_private_bicycle = 0
        self.power_consumption_idling_vkm_shared_bicycle = 0
        self.power_consumption_idling_vkm_private_pedelec = 0 # Source: D. Schröder, L. Kirn, J. Kinigadner, A. Loder, P. Blum, et al., „Ending the myth of mobility at zero costs: An external cost analysis,“ Research in Transportation Economics, vol. 97, p. 101246, 2022, DOI: 10.1016/j.retrec.2022.101246
        self.power_consumption_idling_vkm_shared_pedelec = 0.0351 # Source: database
 

        # Share of electric power generation type in power mix Germany # Source: Fraunhofer-Institut für Solare Energiesysteme ISE, Presseinformation: Nettostromerzeugung in deutschland 2022: Wind und photovoltaik haben deutlich zugelegt, 2023.
        self.power_mix_share = {
            'Water power': 0.04,
            'Wind energy': 0.26,
            'Solar power': 0.12,
            'Bio mass': 0.09,
            'Brown coal': 0.22,
            'Black coal': 0.11,
            'Gas': 0.09,
            'Oil': 0,
            'Nuclear energy': 0.07
        }


        # Climate costs for 680€/t CO^2-eq (0% time preference) # Source: A. Matthey and B. Bünger, Methodenkonvention 3.1 zur ermittlung von umweltkosten: Kostensätze: Stand 12/2020, Dessau-Roßlau, 2020.
        self.climate_costs_0_percent = {
            'Water power': 1.01233,
            'Wind energy': 0.75539,
            'Solar power': 5.19190,
            'Bio mass': 18.63009,
            'Brown coal': 79.64893,
            'Black coal': 74.43612,
            'Gas': 32.79154,
            'Oil': 63.87865,
            'Nuclear energy': 79.64893
        }

        # Climate costs for 195€/t CO^2-eq (1% time preference) # Source: A. Matthey and B. Bünger, Methodenkonvention 3.1 zur ermittlung von umweltkosten: Kostensätze: Stand 12/2020, Dessau-Roßlau, 2020.
        self.climate_costs_1_percent = {
            'Water power': 0.28816,
            'Wind energy': 0.22249,
            'Solar power': 1.50181,
            'Bio mass': 5.39008,
            'Brown coal': 22.98718,
            'Black coal': 20.92226,
            'Gas': 9.45938,
            'Oil': 18.40489,
            'Nuclear energy': 22.98718
        }


        # Loss factors
        self.net_loss_factor = 1.05 # Source: Sohn Associates Limited, “Electricity distribution systems losses: Non-technical overview,” 2009
        self.charging_loss_factor = 1.12 # Source: E. Apostolaki-Iosifidou, P. Codani, and W. Kempton, “Measurement of power loss during electric vehicle charging and discharging,” Energy, vol. 127, pp. 730–742, 2017, issn: 03605442. doi: 10.1016/j.energy.2017.03.015.

        # Occupancy rates # Source: D. Schröder, L. Kirn, J. Kinigadner, A. Loder, P. Blum, et al., „Ending the myth of mobility at zero costs: An external cost analysis,“ Research in Transportation Economics, vol. 97, p. 101246, 2022, DOI: 10.1016/j.retrec.2022.101246
        self.occupancy_rate_private_bicycle = 1.0
        self.occupancy_rate_shared_bicycle = 1.0
        self.occupancy_rate_private_pedelec = 1.0
        self.occupancy_rate_shared_pedelec = 1.0
