import datetime as dt
import os
import pandas as pd

class InputBarrierEffects:
    def __init__(self):
        """
        Initialize the InputBarrierEffects instance and load barrier effects data.
        """
        # Annual mileages in vkm
        self.annual_mileage_private_bicycle = 1103210000 # Source: D. Schröder, L. Kirn, J. Kinigadner, A. Loder, P. Blum, et al., „Ending the myth of mobility at zero costs: An external cost analysis,“ Research in Transportation Economics, vol. 97, p. 101246, 2022, DOI: 10.1016/j.retrec.2022.101246 + R. Follmer and J. Belz, „Mobilität in Deutschland – MiD Kurzreport Stadt München, Münchner Umland und MVV-Verbundraum,“ 2018.
        self.annual_mileage_shared_bicycle = 1487992.064 # Source: database 
        self.annual_mileage_Munich_shared_bicycle = 2066574.21 # Source: database mileage extrapolated for all shared bicycles in Munich

        self.annual_mileage_private_pedelec = 28290000 # Source: D. Schröder, L. Kirn, J. Kinigadner, A. Loder, P. Blum, et al., „Ending the myth of mobility at zero costs: An external cost analysis,“ Research in Transportation Economics, vol. 97, p. 101246, 2022, DOI: 10.1016/j.retrec.2022.101246 + R. Follmer and J. Belz, „Mobilität in Deutschland – MiD Kurzreport Stadt München, Münchner Umland und MVV-Verbundraum,“ 2018.
        self.annual_mileage_shared_pedelec = 200096.408 # Source: database 
        self.annual_mileage_Munich_shared_pedelec = 299626.408 # Source: database extrapolated for all shared pedelecs in Munich

        # Barrier effects costs for €-ct-2022/vkm # Source: Victoria Transport Policy Institute, 2022. Transportation Cost and Benefit Analysis II – Barrier Effect. https://www.vtpi.org/tca/tca0513.pdf.
        self.barrier_effects_vkm_2022_private_bicycle = 0.16 * 1.031 * 1.079 
        self.barrier_effects_vkm_2022_shared_bicycle = 0.16 * 1.031 * 1.079 
        self.barrier_effects_vkm_2022_private_pedelec = 0.16 * 1.031 * 1.079 
        self.barrier_effects_vkm_2022_shared_pedelec = 0.16 * 1.031 * 1.079 

        # Barrier effects costs for $/vmile-2007/vkm # Calculations by Schröder based on Victoria Transport Policy Institute 
        self.barrier_effects_dollar_mile_2007_private_bicycle = 0.001
        self.barrier_effects_dollar_mile_2007_shared_bicycle = 0.001
        self.barrier_effects_dollar_mile_2007_private_pedelec = 0.001
        self.barrier_effects_dollar_mile_2007_shared_pedelec = 0.001
        
        # Inflation rates Germany of different base years in €-ct2022
        self.inflation_rate_2007_to_2022 = 1.1849 * 1.031 * 1.079 
        self.inflation_rate_2020_to_2022 = 1.069 * 1.031 * 1.079 

        # Currency exchange rates base year 2022
        self.currency_exchange_dollar_to_euro = 0.8458

        # Occupancy rates # Source: D. Schröder, L. Kirn, J. Kinigadner, A. Loder, P. Blum, et al., „Ending the myth of mobility at zero costs: An external cost analysis,“ Research in Transportation Economics, vol. 97, p. 101246, 2022, DOI: 10.1016/j.retrec.2022.101246
        self.occupancy_rate_private_bicycle = 1.0
        self.occupancy_rate_shared_bicycle = 1.0
        self.occupancy_rate_private_pedelec = 1.0
        self.occupancy_rate_shared_pedelec = 1.0
