import datetime as dt
import os
import pandas as pd

class InputHealthBenefits:
    def __init__(self):
        """
        Initialize the InputHealthBenefits instance and load health benefits data for multiple modes.
        """
        # Annual mileages in vkm
        self.annual_mileage_private_bicycle = 1103210000 # Source: D. Schröder, L. Kirn, J. Kinigadner, A. Loder, P. Blum, et al., „Ending the myth of mobility at zero costs: An external cost analysis,“ Research in Transportation Economics, vol. 97, p. 101246, 2022, DOI: 10.1016/j.retrec.2022.101246 + R. Follmer and J. Belz, „Mobilität in Deutschland – MiD Kurzreport Stadt München, Münchner Umland und MVV-Verbundraum,“ 2018.
        self.annual_mileage_shared_bicycle = 1487992.064 # Source: database 
        self.annual_mileage_Munich_shared_bicycle = 2066574.21 # Source: database mileage extrapolated for all shared bicycles in Munich

        self.annual_mileage_private_pedelec = 28290000 # Source: D. Schröder, L. Kirn, J. Kinigadner, A. Loder, P. Blum, et al., „Ending the myth of mobility at zero costs: An external cost analysis,“ Research in Transportation Economics, vol. 97, p. 101246, 2022, DOI: 10.1016/j.retrec.2022.101246 + R. Follmer and J. Belz, „Mobilität in Deutschland – MiD Kurzreport Stadt München, Münchner Umland und MVV-Verbundraum,“ 2018.
        self.annual_mileage_shared_pedelec = 200096.408 # Source: database 
        self.annual_mileage_Munich_shared_pedelec = 299626.408 # Source: database extrapolated for all shared pedelecs in Munich

        # Aggregated mileages
        self.annual_mileage_all_bicycle = self.annual_mileage_private_bicycle + self.annual_mileage_Munich_shared_bicycle
        self.annual_mileage_all_pedelec = self.annual_mileage_private_pedelec + self.annual_mileage_Munich_shared_pedelec

        # Value of statistical life
        self.value_of_statistical_life = 4113334.57 # Source: D. Schröder, L. Kirn, J. Kinigadner, A. Loder, P. Blum, et al., „Ending the myth of mobility at zero costs: An external cost analysis,“ Research in Transportation Economics, vol. 97, p. 101246, 2022, DOI: 10.1016/j.retrec.2022.101246

        # Demographical data
        self.citizens_Munich_20_to_64_years_2020 = 965590 # Source: D. Schröder, L. Kirn, J. Kinigadner, A. Loder, P. Blum, et al., „Ending the myth of mobility at zero costs: An external cost analysis,“ Research in Transportation Economics, vol. 97, p. 101246, 2022, DOI: 10.1016/j.retrec.2022.101246
        self.mortality_rates_20_to_64_years = 0.002650 # Source: D. Schröder, L. Kirn, J. Kinigadner, A. Loder, P. Blum, et al., „Ending the myth of mobility at zero costs: An external cost analysis,“ Research in Transportation Economics, vol. 97, p. 101246, 2022, DOI: 10.1016/j.retrec.2022.101246
        
        self.deaths_per_year_private_bicycle = self.citizens_Munich_20_to_64_years_2020 * self.mortality_rates_20_to_64_years
        self.deaths_per_year_shared_bicycle = self.citizens_Munich_20_to_64_years_2020 * self.mortality_rates_20_to_64_years
        self.deaths_per_year_private_pedelec = self.citizens_Munich_20_to_64_years_2020 * self.mortality_rates_20_to_64_years
        self.deaths_per_year_shared_pedelec = self.citizens_Munich_20_to_64_years_2020 * self.mortality_rates_20_to_64_years



        # HEAT reference scenario parameters
        self.relative_risk_private_bicycle_reference_scenario = 0.903 # Source: D. Schröder, L. Kirn, J. Kinigadner, A. Loder, P. Blum, et al., „Ending the myth of mobility at zero costs: An external cost analysis,“ Research in Transportation Economics, vol. 97, p. 101246, 2022, DOI: 10.1016/j.retrec.2022.101246
        self.relative_risk_shared_bicycle_reference_scenario = 0.903 # Source: D. Schröder, L. Kirn, J. Kinigadner, A. Loder, P. Blum, et al., „Ending the myth of mobility at zero costs: An external cost analysis,“ Research in Transportation Economics, vol. 97, p. 101246, 2022, DOI: 10.1016/j.retrec.2022.101246
        self.relative_risk_private_pedelec_reference_scenario = 0.903 # Source: D. Schröder, L. Kirn, J. Kinigadner, A. Loder, P. Blum, et al., „Ending the myth of mobility at zero costs: An external cost analysis,“ Research in Transportation Economics, vol. 97, p. 101246, 2022, DOI: 10.1016/j.retrec.2022.101246
        self.relative_risk_shared_pedelec_reference_scenario = 0.903 # Source: D. Schröder, L. Kirn, J. Kinigadner, A. Loder, P. Blum, et al., „Ending the myth of mobility at zero costs: An external cost analysis,“ Research in Transportation Economics, vol. 97, p. 101246, 2022, DOI: 10.1016/j.retrec.2022.101246

        self.min_per_d_durance_private_bicycle_reference_scenario = 12.2231 # Source: database
        self.min_per_d_durance_shared_bicycle_reference_scenario = 0.0234 # Source: database
        self.min_per_d_durance_private_pedelec_reference_scenario = 0.3660 # Source: database
        self.min_per_d_durance_shared_pedelec_reference_scenario = 0.0041 # Source: database

        self.km_per_min_speed_private_bicycle_reference_scenario = 0.26 # Source: database
        self.km_per_min_speed_shared_bicycle_reference_scenario = 0.26 # Source: database
        self.km_per_min_speed_private_pedelec_reference_scenario = 0.22 # Source: database
        self.km_per_min_speed_shared_pedelec_reference_scenario = 0.22 # Source: database



        # Occupancy rates # Source: D. Schröder, L. Kirn, J. Kinigadner, A. Loder, P. Blum, et al., „Ending the myth of mobility at zero costs: An external cost analysis,“ Research in Transportation Economics, vol. 97, p. 101246, 2022, DOI: 10.1016/j.retrec.2022.101246
        self.occupancy_rate_private_bicycle = 1.0 
        self.occupancy_rate_shared_bicycle = 1.0 
        self.occupancy_rate_private_pedelec = 1.0 
        self.occupancy_rate_shared_pedelec = 1.0 



        # Helpers for reduced mortality risk and avoided deaths
        self.reduced_mortality_risk_private_bicycle = self.calculate_reduced_mortality_risk(self.annual_mileage_private_bicycle, self.relative_risk_private_bicycle_reference_scenario, self.km_per_min_speed_private_bicycle_reference_scenario, self.min_per_d_durance_private_bicycle_reference_scenario)
        self.reduced_mortality_risk_shared_bicycle = self.calculate_reduced_mortality_risk(self.annual_mileage_Munich_shared_bicycle, self.relative_risk_shared_bicycle_reference_scenario, self.km_per_min_speed_shared_bicycle_reference_scenario, self.min_per_d_durance_shared_bicycle_reference_scenario)
        self.reduced_mortality_risk_private_pedelec = self.calculate_reduced_mortality_risk(self.annual_mileage_private_pedelec, self.relative_risk_private_pedelec_reference_scenario, self.km_per_min_speed_private_pedelec_reference_scenario, self.min_per_d_durance_private_pedelec_reference_scenario)
        self.reduced_mortality_risk_shared_pedelec = self.calculate_reduced_mortality_risk(self.annual_mileage_Munich_shared_pedelec, self.relative_risk_shared_pedelec_reference_scenario, self.km_per_min_speed_shared_pedelec_reference_scenario, self.min_per_d_durance_shared_pedelec_reference_scenario)

        self.avoided_deaths_private_bicycle = self.reduced_mortality_risk_private_bicycle * self.deaths_per_year_private_bicycle
        self.avoided_deaths_shared_bicycle = self.reduced_mortality_risk_shared_bicycle * self.deaths_per_year_shared_bicycle
        self.avoided_deaths_private_pedelec = self.reduced_mortality_risk_private_pedelec * self.deaths_per_year_private_pedelec
        self.avoided_deaths_shared_pedelec = self.reduced_mortality_risk_shared_pedelec * self.deaths_per_year_shared_pedelec



    def calculate_reduced_mortality_risk(self, annual_mileage, relative_risk, km_per_min_speed, min_per_d_durance):
        """
        Calculate the reduced mortality risk for a given annual mileage and mode-specific parameters.
        """
        if ((annual_mileage / 1000000) / 1.488 / 365 / km_per_min_speed * 7) < 450:
            return (1 - relative_risk) * (
                (annual_mileage / 1000000) / 1.488 / 365 / km_per_min_speed / min_per_d_durance
            )
        else:
            return 0.45




