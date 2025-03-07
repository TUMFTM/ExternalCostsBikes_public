class InputAirPollution:
    def __init__(self):
        """
        Initialize the InputAirPollution instance and load air pollution data.
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
 

        # Share of electric power generation type in power mix Germany in 2022 # Source: Fraunhofer-Institut für Solare Energiesysteme ISE, Presseinformation: Nettostromerzeugung in deutschland 2022: Wind und photovoltaik haben deutlich zugelegt, 2023.
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

        # Air pollution costs of electric power generation type i in €-ct2022/kWh (inflation adapted based on €-ct2020 values) # Source: A. Matthey and B. Bünger, Methodenkonvention 3.1 zur ermittlung von umweltkosten: Kostensätze: Stand 12/2020, Dessau-Roßlau, 2020.
        self.pollution_costs = {
            'Water power': 0.06675,
            'Wind energy': 0.12237,
            'Solar power': 0.47835,
            'Bio mass': 4.38413,
            'Brown coal': 2.28156,
            'Black coal': 1.86805,
            'Gas': 0.96761,
            'Oil': 5.76249,
            'Nuclear energy': 2.28156
        }

        # Exhaust costs in €-ct2022/vkm --> non-existant for given modes of transport
        self.exhaust_cost_private_bicycle = 0.0
        self.exhaust_cost_shared_bicycle = 0.0
        self.exhaust_cost_private_pedelec = 0.0
        self.exhaust_cost_shared_pedelec = 0.0

        # Abrasion costs in €-ct2022/vkm # Source: A. Matthey and B. Bünger, Methodenkonvention 3.1 zur ermittlung von umweltkosten: Kostensätze: Stand 12/2020, Dessau-Roßlau, 2020.
        self.abrasion_cost_private_bicycle = 0.0
        self.abrasion_cost_shared_bicycle = 0.0
        self.abrasion_cost_private_pedelec = 0.02
        self.abrasion_cost_shared_pedelec = 0.02

        # Loss factors
        self.net_loss_factor = 1.05 # Source: Sohn Associates Limited, “Electricity distribution systems losses: Non-technical overview,” 2009
        self.charging_loss_factor = 1.12 # Source: E. Apostolaki-Iosifidou, P. Codani, and W. Kempton, “Measurement of power loss during electric vehicle charging and discharging,” Energy, vol. 127, pp. 730–742, 2017, issn: 03605442. doi: 10.1016/j.energy.2017.03.015.

        # Occupancy rates # Source: D. Schröder, L. Kirn, J. Kinigadner, A. Loder, P. Blum, et al., „Ending the myth of mobility at zero costs: An external cost analysis,“ Research in Transportation Economics, vol. 97, p. 101246, 2022, DOI: 10.1016/j.retrec.2022.101246
        self.occupancy_rate_private_bicycle = 1.0
        self.occupancy_rate_shared_bicycle = 1.0
        self.occupancy_rate_private_pedelec = 1.0
        self.occupancy_rate_shared_pedelec = 1.0
