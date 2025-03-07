import datetime as dt
import pandas as pd
import numpy as np

class ExternalCostsCalculator:
    def __init__(self):
        """
        Initialize the ExternalCostsCalculator instance.
        """
        # Set the default mode to 'private_bicycle'
        self.mode = 'private_bicycle'
        # Set the default method to 'advanced'
        self.method = 'advanced'
        # Calculator Modules
        self.calculators = {}
        # Result Part
        self.results = {
            'Cost by Category': {},
            'Total Cost': {}
        }

    def append(self, calculation):
        """
        Append a calculation to the calculator.

        Args:
            calculation: The calculation object to append.
        """
        key = calculation.tag
        self.calculators[key] = calculation
        
    def evaluate(self):
        """
        Evaluate the costs and update the results.
        """
        self.results['Total Cost']['total cost per vkm'] = 0
        self.results['Total Cost']['total cost per pkm'] = 0
        self.results['Total Cost']['total cost per year'] = 0
        
        for key, calculator in self.calculators.items():
            self.results['Cost by Category'][key] = calculator.calc_costs()
        
        for key, result in self.results['Cost by Category'].items():
            self.results['Total Cost']['total cost per vkm'] += result['cost per vkm']
            self.results['Total Cost']['total cost per pkm'] += result['cost per pkm']
            self.results['Total Cost']['total cost per year'] += result['cost per year']

            


