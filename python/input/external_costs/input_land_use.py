class InputLandUse:
    def __init__(self):
        """
        Initialize the InputLandUse instance and load land use data.
        """
        # Annual mileages in vkm
        self.annual_mileage_private_bicycle = 1103210000 # Source: D. Schröder, L. Kirn, J. Kinigadner, A. Loder, P. Blum, et al., „Ending the myth of mobility at zero costs: An external cost analysis,“ Research in Transportation Economics, vol. 97, p. 101246, 2022, DOI: 10.1016/j.retrec.2022.101246 + R. Follmer and J. Belz, „Mobilität in Deutschland – MiD Kurzreport Stadt München, Münchner Umland und MVV-Verbundraum,“ 2018.
        self.annual_mileage_shared_bicycle = 1487992.064 # Source: database 
        self.annual_mileage_Munich_shared_bicycle = 2066574.21 # Source: database mileage extrapolated for all shared bicycles in Munich

        self.annual_mileage_private_pedelec = 28290000 # Source: D. Schröder, L. Kirn, J. Kinigadner, A. Loder, P. Blum, et al., „Ending the myth of mobility at zero costs: An external cost analysis,“ Research in Transportation Economics, vol. 97, p. 101246, 2022, DOI: 10.1016/j.retrec.2022.101246 + R. Follmer and J. Belz, „Mobilität in Deutschland – MiD Kurzreport Stadt München, Münchner Umland und MVV-Verbundraum,“ 2018.
        self.annual_mileage_shared_pedelec = 200096.408 # Source: database 
        self.annual_mileage_Munich_shared_pedelec = 299626.408 # Source: database extrapolated for all shared pedelecs in Munich

        # Mileages shared vehicles for all shared vehicles in Munich  
        self.annual_mileage_Munich_scooter = 4009954 # Source: database

        self.annual_mileage_active_modes = self.annual_mileage_Munich_scooter + self.annual_mileage_Munich_shared_bicycle + self.annual_mileage_Munich_shared_pedelec + self.annual_mileage_private_bicycle + self.annual_mileage_private_pedelec

        # Number of stations 
        self.nr_stations_shared_bicycle = 337

        # Space consumption stations # Source: database 
        self.space_station_shared_bicycle = 15 # m^2 

        # Costs 
        self.total_infrastructure_cost_active_mobility = 2.3 * 1588330 # Investment per person in €-2022/year for bicycle infrastructure * citizens in Munich urban areas in 2022
        
        # self.opportunity_cost_m2_public_space_annual = 54.32
        self.opportunity_cost_m2_bio_diversity_costs = 4.00
    
        # Parking / idling durations per year 
        self.hours_idling_private_bicycle = 23 * 365 * 975000 # Source: D. Schröder, L. Kirn, J. Kinigadner, A. Loder, P. Blum, et al., „Ending the myth of mobility at zero costs: An external cost analysis,“ Research in Transportation Economics, vol. 97, p. 101246, 2022, DOI: 10.1016/j.retrec.2022.101246 + R. Follmer and J. Belz, „Mobilität in Deutschland – MiD Kurzreport Stadt München, Münchner Umland und MVV-Verbundraum,“ 2018.
        self.hours_idling_shared_bicycle = 46400438.99 # Source: database extrapolated for all shares bicycles in Munich
        self.hours_idling_private_pedelec = 23 * 365 * 25000 # Source: D. Schröder, L. Kirn, J. Kinigadner, A. Loder, P. Blum, et al., „Ending the myth of mobility at zero costs: An external cost analysis,“ Research in Transportation Economics, vol. 97, p. 101246, 2022, DOI: 10.1016/j.retrec.2022.101246 + R. Follmer and J. Belz, „Mobilität in Deutschland – MiD Kurzreport Stadt München, Münchner Umland und MVV-Verbundraum,“ 2018.
        self.hours_idling_shared_pedelec = 6165937.42 # Source: database extrapolated for all shared pedelecs in Munich

        # Space consumption vehicle
        self.space_private_bicycle = 1.6 # m^2 # Source
        self.space_shared_bicycle = 1.6 # m^2 # Source
        self.space_private_pedelec = 1.6 # m^2 # Source
        self.space_shared_pedelec = 1.6 # m^2 # Source

        # Land use per person for vehicle type in m^2 for 30 km/h 
        self.land_use_per_person_30kmh = {
            'Bus Electric': 8.6,
            'Bus Diesel': 8.6,
            'Moped Electric': 41,
            'Moped Gasoline': 41,
            'Motorcycle': 41,
            'Car BEV': 65.2,
            'Car PHEV': 65.2,
            'Car Diesel': 65.2,
            'Car Gasoline': 65.2,
            'Car-Sharing Electric': 65.2,
            'Car-Sharing Gasoline': 65.2,
            'Moped Sharing': 41
        }
 
        # Annual mileage for all vehicle classes in vkm/year # Source: D. Schröder, L. Kirn, J. Kinigadner, A. Loder, P. Blum, et al., „Ending the myth of mobility at zero costs: An external cost analysis,“ Research in Transportation Economics, vol. 97, p. 101246, 2022, DOI: 10.1016/j.retrec.2022.101246
        self.annual_mileage = {
            'Bus Electric': 0,
            'Bus Diesel': 37360000,
            'Moped Electric': 780000,
            'Moped Gasoline': 85010000,
            'Motorcycle': 278200000,
            'Car BEV': 85160000,
            'Car PHEV': 109590000,
            'Car Diesel': 2495820000,
            'Car Gasoline': 4401090000,
            'Car-Sharing Electric': 14590000,
            'Car-Sharing Gasoline': 58380000,
            'Moped Sharing': 1540000
        }

        # Helpers
        self.hours_per_year = 365 * 24

        # Occupancy rates # Source: D. Schröder, L. Kirn, J. Kinigadner, A. Loder, P. Blum, et al., „Ending the myth of mobility at zero costs: An external cost analysis,“ Research in Transportation Economics, vol. 97, p. 101246, 2022, DOI: 10.1016/j.retrec.2022.101246
        self.occupancy_rate_private_bicycle = 1.0
        self.occupancy_rate_shared_bicycle = 1.0
        self.occupancy_rate_private_pedelec = 1.0
        self.occupancy_rate_shared_pedelec = 1.0

       
