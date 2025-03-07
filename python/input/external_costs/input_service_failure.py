class InputServiceFailure:
    def __init__(self):
        """
        Initialize the InputServiceFailure instance and load service failure data.
        """
        # Annual mileages in vkm
        self.annual_mileage_private_bicycle = 1103210000 # Source: D. Schröder, L. Kirn, J. Kinigadner, A. Loder, P. Blum, et al., „Ending the myth of mobility at zero costs: An external cost analysis,“ Research in Transportation Economics, vol. 97, p. 101246, 2022, DOI: 10.1016/j.retrec.2022.101246 + R. Follmer and J. Belz, „Mobilität in Deutschland – MiD Kurzreport Stadt München, Münchner Umland und MVV-Verbundraum,“ 2018.
        self.annual_mileage_shared_bicycle = 1487992.064 # Source: database 
        self.annual_mileage_Munich_shared_bicycle = 2066574.21 # Source: database mileage extrapolated for all shared bicycles in Munich

        self.annual_mileage_private_pedelec = 28290000 # Source: D. Schröder, L. Kirn, J. Kinigadner, A. Loder, P. Blum, et al., „Ending the myth of mobility at zero costs: An external cost analysis,“ Research in Transportation Economics, vol. 97, p. 101246, 2022, DOI: 10.1016/j.retrec.2022.101246 + R. Follmer and J. Belz, „Mobilität in Deutschland – MiD Kurzreport Stadt München, Münchner Umland und MVV-Verbundraum,“ 2018.
        self.annual_mileage_shared_pedelec = 200096.408 # Source: database 
        self.annual_mileage_Munich_shared_pedelec = 299626.408 # Source: database extrapolated for all shared pedelecs in Munich

        # Total usage times
        self.usage_time_private_bicycle = 0 # no service privided
        self.usage_time_shared_bicycle = 435366.42 # Source: database extrapolated for all shared bicycles in Munich
        self.usage_time_private_pedelec = 0 # no service privided
        self.usage_time_shared_pedelec = 31367.82 # Source: database extrapolated for all shared pedelecs in Munich

        # Service failure factors
        self.service_failure_factor_private_bicycle = 0
        self.service_failure_factor_shared_bicycle = 0.004 # Source: MVGBike expert interview
        self.service_failure_factor_private_pedelec = 0
        self.service_failure_factor_shared_pedelec = 0.002 # Source: own assumption to be 50% of MVGBike

        # Costs in €2022 in €/h
        self.cost_per_hour_delay = 10.01 

        # Occupancy rates # Source: D. Schröder, L. Kirn, J. Kinigadner, A. Loder, P. Blum, et al., „Ending the myth of mobility at zero costs: An external cost analysis,“ Research in Transportation Economics, vol. 97, p. 101246, 2022, DOI: 10.1016/j.retrec.2022.101246
        self.occupancy_rate_private_bicycle = 1.0
        self.occupancy_rate_shared_bicycle = 1.0
        self.occupancy_rate_private_pedelec = 1.0
        self.occupancy_rate_shared_pedelec = 1.0

