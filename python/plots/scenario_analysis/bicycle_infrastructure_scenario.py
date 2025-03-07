import os
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator
from matplotlib.patches import Patch

# ====================================================================================== #
#       GLOBAL CONFIGURATION
# ====================================================================================== #

try:
    current_notebook = os.path.realpath(__file__)
except NameError:
    current_notebook = os.getcwd()
current_directory = os.path.dirname(current_notebook)
figures_directory = os.path.join(current_directory, '..', 'figures')
os.makedirs(figures_directory, exist_ok=True)

# Set global plotting parameters
plt.rcParams['font.size'] = 16
plt.style.use(['science', 'nature'])

# Color palette using colorblind-friendly colors
color_codes = {
    'Color1': '#D9ED92',  # Light green
    'Color2': '#B5E48C',  # Green
    'Color3': '#99D98C',  # Medium green
    'Color4': '#76C893',  # Darker green  - Damage Potential
    'Color5': '#52B69A',  # Teal  - Cost-by-Cause
    'Color6': '#34A0A4',  # Dark teal
    'Color7': '#168AAD',  # Blue-green
    'Color8': '#1A759F',  # Medium blue - Damage Potential (Infrastructure)
    'Color9': '#1E6091',  # Dark blue
    'Color10': '#184E77'  # Darker blue - Cost-by-Cause (Infrastructure)
}

def generate_bicycle_infrastructure_collisions_costs_plot(
        external_costs_results_1_time_pref_all_bicycle,
        external_costs_results_damage_potential_all_bicycle_infrastructure,
        external_costs_results_causer_all_bicycle,
        external_costs_results_causer_all_bicycle_infrastructure,
        external_costs_results_1_time_pref_all_pedelec,
        external_costs_results_damage_potential_all_pedelec_infrastructure,
        external_costs_results_causer_all_pedelec,
        external_costs_results_causer_all_pedelec_infrastructure):
    
    # Define transport modes and bar width
    modes = ['c-Bike', 'e-Bike']
    bar_width = 0.18
    offset = bar_width * 1.6

    # Define colors for different bars
    colors = [
        color_codes['Color4'],  # Damage Potential Method
        color_codes['Color8'],  # Damage Potential Method (Infrastructure)
        color_codes['Color5'],  # Cost-by-Cause Method
        color_codes['Color10']  # Cost-by-Cause Method (Infrastructure)
    ]

    # Define hatching patterns for improved readability
    hatch_patterns = ['//', 'xx', '\\\\', '||']

    # Data setup
    data_sets = {
        "Damage Potential Method": [
            external_costs_results_1_time_pref_all_bicycle['Cost by Category']['Collisions']['cost per pkm'],
            external_costs_results_1_time_pref_all_pedelec['Cost by Category']['Collisions']['cost per pkm']
        ],
        "Damage Potential Method (Infrastructure)": [
            external_costs_results_damage_potential_all_bicycle_infrastructure['Cost by Category']['Collisions']['cost per pkm'],
            external_costs_results_damage_potential_all_pedelec_infrastructure['Cost by Category']['Collisions']['cost per pkm']
        ],
        "Cost-by-Cause Method": [
            external_costs_results_causer_all_bicycle['Cost by Category']['Collisions']['cost per pkm'],
            external_costs_results_causer_all_pedelec['Cost by Category']['Collisions']['cost per pkm']
        ],
        "Cost-by-Cause Method (Infrastructure)": [
            external_costs_results_causer_all_bicycle_infrastructure['Cost by Category']['Collisions']['cost per pkm'],
            external_costs_results_causer_all_pedelec_infrastructure['Cost by Category']['Collisions']['cost per pkm']
        ]
    }

    # Create figure and axis
    fig, ax = plt.subplots(figsize=(10, 6))
    base_positions = np.arange(len(modes))

    # Define positions for different bars
    positions = [
        base_positions - offset - bar_width / 4,
        base_positions - offset / 2,
        base_positions + offset / 2,
        base_positions + offset + bar_width / 4
    ]

    # Generate bars with hatching
    bars = []
    for i, (key, values) in enumerate(data_sets.items()):
        bars.append(
            ax.bar(positions[i], values, bar_width, label=key, color=colors[i], hatch=hatch_patterns[i], edgecolor='black', zorder=3)
        )

    # Annotate values inside the bars
    for i, (bar_group, values, color) in enumerate(zip(bars, data_sets.values(), colors)):
        for j, (bar, value) in enumerate(zip(bar_group, values)):
            text_color = 'white' if color in [color_codes['Color8'], color_codes['Color10']] else 'black'
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 2.0, 
                    f'{value:.2f}', ha='center', va='center', fontsize=10, zorder=5,
                    bbox=dict(facecolor=color, edgecolor=color, boxstyle='round,pad=0.3'), color=text_color)

    # Add percentage change lines between bars for both methods
    line_width = 1.5  

    for i in range(len(modes)):
        for method, pos1, pos2, dataset_key in [
            ("Damage Potential", positions[0][i], positions[1][i], "Damage Potential Method"),
            ("Cost-by-Cause", positions[2][i], positions[3][i], "Cost-by-Cause Method")
        ]:
            percent_diff = (data_sets[f"{dataset_key} (Infrastructure)"][i] - data_sets[dataset_key][i]) / data_sets[dataset_key][i] * 100

            ax.plot([pos1, pos2], 
                    [data_sets[dataset_key][i] + 1.5, data_sets[dataset_key][i] + 3], color='black', lw=line_width, zorder=1)
            ax.annotate("", xy=(pos2, data_sets[f"{dataset_key} (Infrastructure)"][i] + 2.6),
                        xytext=(pos2, data_sets[dataset_key][i] + 3),
                        arrowprops=dict(arrowstyle="-|>", color='black', linewidth=line_width, shrinkA=0, shrinkB=0))
            ax.text(pos2, data_sets[dataset_key][i] + 2.2, f'{percent_diff:.1f}\%',
                    ha='center', va='bottom', fontsize=10, bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3'))

    # Configure axes
    ax.set_ylabel('External Costs of Collisions Cycle Path Scenario (€-Cent/pkm)', fontsize=14) #TODO: - exchange for other scenario
    ax.set_xticks(base_positions)
    ax.set_xticklabels(modes, fontsize=14)
    ax.set_ylim(bottom=0, top=40)

    ax.grid(axis='y', linestyle='--', alpha=0.5, linewidth=1.0, zorder=0)

    # Add legend
    ax.legend(handles=[Patch(facecolor=colors[i], label=list(data_sets.keys())[i], hatch=hatch_patterns[i]) for i in range(len(data_sets))], loc='upper left', fontsize=12, frameon=False)

    # Save and show plot
    plt.tight_layout()
    plt.savefig(os.path.join(figures_directory, 'external_costs_results_collisions_bicycle_infrastructure_cycle_path.pdf')) #TODO: - exchange for other scenario
    plt.savefig(os.path.join(figures_directory, 'external_costs_results_collisions_bicycle_infrastructure_cycle_path.svg')) #TODO: - exchange for other scenario
    plt.show()





