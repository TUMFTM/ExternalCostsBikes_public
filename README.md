# Reducing health and economic burdens of bicycle collision costs through dedicated cycling infrastructure: a city-wide safety and mobility analysis
**Author:**  Anna Paper

## Introduction

This repository contains the source code for the paper *"Reducing health and economic burdens of bicycle collision costs through dedicated cycling infrastructure: a city-wide safety and mobility analysis"*. The code enables the analysis of shared and private micromobility data, with a focus on bicycles and pedelecs, to calculate external cost categories including air pollution, barrier effects, climate change, collisions, health benefits, land use, service failure, and upstream processes.


## Features

- Calculation of external costs associated with micromobility vehicles in the city of Munich.
- Modular design supporting different vehicle types and cost factors.
- Extensible structure allowing the addition of new cost calculations, data sources, mobility modes, or locations.


## Installation

1. Ensure **Python 3.12.x** is installed on your system.
2. Clone this repository to your local machine:
   ```bash
   git clone <repository-url>
3. Install the required Python packages listed in environment.yml
conda env create -f environment.yml
conda activate <env-name>
    Alternatively, install dependencies manually using pip based on the modules' requirements.


## Usage

1. Run main.py to process data and generate visualizations.
2. Use specific modules for individual vehicle types or cost calculations as needed.
3. Each cost category has its own dedicated calculation and input module (e.g., collision.py, input_collisions.py).
4. To change between the both cyling infrastructure scenarios, the words 'path' and 'lane' need to be exchanged in all places where you can currently read the following task '#TODO: adapt for cycle path scenario'


## Data

The data used in this project was compiled from existing literature and databases provided by shared micromobility providers TIER GmbH and MVG, adhering to the best scientific standards. However, unforeseen errors may still occur.

Note: Due to data privacy regulations, police accident data from Munich has been removed from the public version of this repository. Placeholders have been inserted at relevant points in the code, indicating the expected structure of the underlying data.


## Common Issues and Troubleshooting

- Module Imports: Ensure all required Python modules are installed and correctly imported. This code runs on Python 3.12.2.
- File Paths: Verify file paths in the code, especially when loading or saving data, to avoid errors.


## Acknowledgments

Special thanks to TIER GmbH and MVG for providing access to their valuable data, which made this analysis possible.


