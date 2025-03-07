import os
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams
from matplotlib.ticker import MultipleLocator, AutoMinorLocator
from matplotlib.patches import Patch  # Import Patch for legend
from mpl_toolkits.axes_grid1.inset_locator import inset_axes, mark_inset
import scienceplots


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

# Set up global plotting parameters
#rcParams['font.family'] = 'Arial'
rcParams['font.size'] = 14
plt.style.use(['science', 'nature'])  # Ensure 'science' and 'nature' styles are installed

# Color Palette using colorblind-friendly colors
color_codes = {
    'Color1': '#D9ED92',  # Light green
    'Color2': '#B5E48C',  # Green
    'Color3': '#99D98C',  # Medium green
    'Color4': '#76C893',  # Darker green
    'Color5': '#52B69A',  # Teal
    'Color6': '#34A0A4',  # Dark teal
    'Color7': '#168AAD',  # Blue-green
    'Color8': '#1A759F',  # Medium blue
    'Color9': '#1E6091',  # Dark blue
    'Color10': '#184E77'  # Darker blue
}


def configure_ax(ax, ylabel, minortick_interval, majortick_interval, show_legend=False, legend_labels=None):
    """
    Configures the axes with unified styling, labels, grid, and ticks.
    """
    ax.set_ylabel(ylabel, fontsize=12)
    ax.yaxis.set_minor_locator(MultipleLocator(minortick_interval))  # Ensure minor tick spacing is consistent
    ax.yaxis.set_major_locator(MultipleLocator(majortick_interval))  # Ensure major tick spacing is consistent
    ax.grid(axis='y', linestyle='--', alpha=0.5, linewidth=1.0, zorder=0)
    ax.tick_params(axis='both', labelsize=12, direction='in', top=True, right=True)

    if show_legend and legend_labels:
        ax.legend(handles=legend_labels, loc='upper left', fontsize=10, frameon=False)


# ====================================================================================== #
#       AIR POLLUTION EXTERNAL COSTS
# ====================================================================================== #


def generate_air_pollution_costs_plot(
        external_costs_results_1_time_pref_private_bicycle,
        external_costs_results_1_time_pref_shared_bicycle,
        external_costs_results_1_time_pref_private_pedelec,
        external_costs_results_1_time_pref_shared_pedelec,
        ax=None):

    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 6))
        plt.rcParams.update({'font.family': 'Arial'})

    # Define modes and bar width
    modes = ['Private c-Bike', 'Shared c-Bike', 'Private e-Bike', 'Shared e-Bike']
    bar_width = 0.4
    bar_positions = np.arange(len(modes))

    data_abrasion = [
        0,
        0,
        external_costs_results_1_time_pref_private_pedelec['Cost by Category']['Air Pollution']['cost per pkm abrasion'],
        external_costs_results_1_time_pref_shared_pedelec['Cost by Category']['Air Pollution']['cost per pkm abrasion']
    ]
    data_idling = [
        0,
        0,
        external_costs_results_1_time_pref_private_pedelec['Cost by Category']['Air Pollution']['cost per pkm idling'],
        external_costs_results_1_time_pref_shared_pedelec['Cost by Category']['Air Pollution']['cost per pkm idling']
    ]
    data_driving = [
        0,
        0,
        external_costs_results_1_time_pref_private_pedelec['Cost by Category']['Air Pollution']['cost per pkm driving'],
        external_costs_results_1_time_pref_shared_pedelec['Cost by Category']['Air Pollution']['cost per pkm driving']
    ]

    # Create stacked bars (no hatching)
    bars_abrasion = ax.bar(bar_positions, data_abrasion, width=bar_width, color=color_codes['Color1'],
                           edgecolor='black', label='Abrasion Costs', zorder=3)
    bars_idling = ax.bar(bar_positions, data_idling, width=bar_width, bottom=data_abrasion,
                         color=color_codes['Color2'], edgecolor='black', label='Energy Production Costs (Idling)', zorder=3)
    bars_driving = ax.bar(bar_positions, data_driving, width=bar_width,
                          bottom=np.array(data_abrasion) + np.array(data_idling),
                          color=color_codes['Color3'], edgecolor='black', label='Energy Production Costs (Driving)', zorder=3)

    # Sum of bar heights for y-axis scaling
    bar_height_sums = np.array(data_abrasion) + np.array(data_idling) + np.array(data_driving)

    # Set dynamic y-axis limit
    max_bar_height = max(bar_height_sums) if max(bar_height_sums) > 0 else 0.01  # Prevent division by zero
    ax.set_ylim(0, max_bar_height * 1.1)

    # Display total external costs on top of bars
    for i in range(len(modes)):
        if bar_height_sums[i] > 0:
            ax.text(bar_positions[i], bar_height_sums[i] + max_bar_height * 0.02,
                    f'{bar_height_sums[i]:.3f}', ha='center', va='bottom',
                    color='black', fontsize=10,
                    bbox=dict(facecolor=color_codes['Color4'], edgecolor=color_codes['Color4'], boxstyle='round,pad=0.3'))

    # Add labels for individual cost segments within stacked bars
    for i in range(len(modes)):
        if data_abrasion[i] > 0:
            ax.text(bar_positions[i], data_abrasion[i] / 2,
                    f'{data_abrasion[i]:.3f}', ha='center', va='center',
                    color='black', fontsize=8,
                    bbox=dict(facecolor=color_codes['Color1'], edgecolor=color_codes['Color1'], boxstyle='round,pad=0.3'))
        if data_idling[i] > 0:
            ax.text(bar_positions[i], data_abrasion[i] + data_idling[i] / 2,
                    f'{data_idling[i]:.3f}', ha='center', va='center',
                    color='black', fontsize=8,
                    bbox=dict(facecolor=color_codes['Color2'], edgecolor=color_codes['Color2'], boxstyle='round,pad=0.3'))
        if data_driving[i] > 0:
            ax.text(bar_positions[i], data_abrasion[i] + data_idling[i] + data_driving[i] / 2,
                    f'{data_driving[i]:.3f}', ha='center', va='center',
                    color='black', fontsize=8,
                    bbox=dict(facecolor=color_codes['Color3'], edgecolor=color_codes['Color3'], boxstyle='round,pad=0.3'))

    ax.set_xticks(bar_positions)
    ax.set_xticklabels(modes, fontsize=12)

    configure_ax(ax, 'External Costs of Air Pollution (€-Cent/pkm)', minortick_interval=0.005, majortick_interval=0.01, show_legend=True)

    legend_labels = [
        Patch(facecolor=color_codes['Color3'], edgecolor='black', label='Energy Production Costs (Driving)'),
        Patch(facecolor=color_codes['Color2'], edgecolor='black', label='Energy Production Costs (Idling)'),
        Patch(facecolor=color_codes['Color1'], edgecolor='black', label='Abrasion Costs')
    ]
    ax.legend(handles=legend_labels, loc='upper left', fontsize=10, frameon=False)

    # Save the plot
    plt.savefig(os.path.join(figures_directory, 'external_costs_results_air_pollution.pdf'))
    plt.savefig(os.path.join(figures_directory, 'external_costs_results_air_pollution.svg'))
    #plt.show()


# ====================================================================================== #
#       CLIMATE CHANGE EXTERNAL COSTS
# ====================================================================================== #


def generate_climate_change_costs_plot(
        external_costs_results_1_time_pref_private_bicycle,
        external_costs_results_0_time_pref_private_bicycle,
        external_costs_results_1_time_pref_shared_bicycle,
        external_costs_results_0_time_pref_shared_bicycle,
        external_costs_results_1_time_pref_private_pedelec,
        external_costs_results_0_time_pref_private_pedelec,
        external_costs_results_1_time_pref_shared_pedelec,
        external_costs_results_0_time_pref_shared_pedelec,
        ax=None):

    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 6))
        #plt.rcParams.update({'font.family': 'Arial'})

    colors_1_time_pref = [color_codes['Color4'], color_codes['Color5']]
    colors_0_time_pref = [color_codes['Color6'], color_codes['Color7']]

    data_1_time_pref_driving = [
        0, 0,
        external_costs_results_1_time_pref_private_pedelec['Cost by Category']['Climate Change']['cost per pkm driving'],
        external_costs_results_1_time_pref_shared_pedelec['Cost by Category']['Climate Change']['cost per pkm driving']
    ]
    data_1_time_pref_idling = [
        0, 0,
        external_costs_results_1_time_pref_private_pedelec['Cost by Category']['Climate Change']['cost per pkm idling'],
        external_costs_results_1_time_pref_shared_pedelec['Cost by Category']['Climate Change']['cost per pkm idling']
    ]

    data_0_time_pref_driving = [
        0, 0,
        external_costs_results_0_time_pref_private_pedelec['Cost by Category']['Climate Change']['cost per pkm driving'],
        external_costs_results_0_time_pref_shared_pedelec['Cost by Category']['Climate Change']['cost per pkm driving']
    ]
    data_0_time_pref_idling = [
        0, 0,
        external_costs_results_0_time_pref_private_pedelec['Cost by Category']['Climate Change']['cost per pkm idling'],
        external_costs_results_0_time_pref_shared_pedelec['Cost by Category']['Climate Change']['cost per pkm idling']
    ]

    bar_width = 0.3
    # Define x-axis modes and spacing
    modes = ['Private c-Bike', 'Shared c-Bike', 'Private e-Bike', 'Shared e-Bike']
    bar_positions = np.arange(len(modes))
    #bar_positions = np.arange(4)
    bar_positions_1_time_pref = bar_positions - bar_width / 2
    bar_positions_0_time_pref = bar_positions + bar_width / 2

    # Create bars for 1% Time Preference with hatch patterns
    bars_1_time_pref_idling = ax.bar(bar_positions_1_time_pref[2:], data_1_time_pref_idling[2:], width=bar_width,
                                     color=colors_1_time_pref[0], edgecolor='black',
                                     label='Energy Production Idling, 1\% Time Preference', hatch='\\\\', zorder=3)
    bars_1_time_pref_driving = ax.bar(bar_positions_1_time_pref, data_1_time_pref_driving, width=bar_width,
                                      bottom=data_1_time_pref_idling, color=colors_1_time_pref[1],
                                      edgecolor='black',
                                      label='Energy Production Driving, 1\% Time Preference', hatch='//', zorder=3)

    # Create bars for 0% Time Preference with hatch patterns
    bars_0_time_pref_idling = ax.bar(bar_positions_0_time_pref[2:], data_0_time_pref_idling[2:], width=bar_width,
                                     color=colors_0_time_pref[0], edgecolor='black',
                                     label='Energy Production Idling, 0\% Time Preference', hatch='\\\\', zorder=3)
    bars_0_time_pref_driving = ax.bar(bar_positions_0_time_pref, data_0_time_pref_driving, width=bar_width,
                                      bottom=data_0_time_pref_idling, color=colors_0_time_pref[1],
                                      edgecolor='black',
                                      label='Energy Production Driving, 0\% Time Preference', hatch='//', zorder=3)

    # Calculate the sum of bar heights for each mode
    bar_height_sums_1_time_pref = np.array(data_1_time_pref_idling) + np.array(data_1_time_pref_driving)
    bar_height_sums_0_time_pref = np.array(data_0_time_pref_idling) + np.array(data_0_time_pref_driving)

    # Set the y-axis limit dynamically
    max_bar_height = max(max(bar_height_sums_1_time_pref), max(bar_height_sums_0_time_pref))
    ax.set_ylim(0, max_bar_height * 1.1)

    # Display the total external costs on top of each bar
    for i in range(len(bar_positions)):
        if bar_height_sums_1_time_pref[i] > 0:
            ax.text(bar_positions_1_time_pref[i], bar_height_sums_1_time_pref[i] + max_bar_height * 0.02,
                    f'{bar_height_sums_1_time_pref[i]:.3f}', ha='center', va='bottom',
                    color='black', fontsize=10,
                    bbox=dict(facecolor=color_codes['Color8'], edgecolor=color_codes['Color8'], boxstyle='round,pad=0.3'))
        if bar_height_sums_0_time_pref[i] > 0:
            ax.text(bar_positions_0_time_pref[i], bar_height_sums_0_time_pref[i] + max_bar_height * 0.02,
                    f'{bar_height_sums_0_time_pref[i]:.3f}', ha='center', va='bottom',
                    color='black', fontsize=10,
                    bbox=dict(facecolor=color_codes['Color8'], edgecolor=color_codes['Color8'], boxstyle='round,pad=0.3'))

    # Add labels for individual cost segments within the bars
    for i in range(2, len(bar_positions)):
        if data_1_time_pref_idling[i] > 0:
            ax.text(bar_positions_1_time_pref[i] - 0.15, data_1_time_pref_idling[i] / 2,
                    f'{data_1_time_pref_idling[i]:.3f}', ha='center', va='center',
                    color='black', fontsize=8,
                    bbox=dict(facecolor=color_codes['Color4'], edgecolor=color_codes['Color4'], boxstyle='round,pad=0.3'))
        if data_1_time_pref_driving[i] > 0:
            ax.text(bar_positions_1_time_pref[i] - 0.15,
                    data_1_time_pref_idling[i] + data_1_time_pref_driving[i] / 2,
                    f'{data_1_time_pref_driving[i]:.3f}', ha='center', va='center',
                    color='black', fontsize=8,
                    bbox=dict(facecolor=color_codes['Color5'], edgecolor=color_codes['Color5'], boxstyle='round,pad=0.3'))

        if data_0_time_pref_idling[i] > 0:
            ax.text(bar_positions_0_time_pref[i] + 0.15, data_0_time_pref_idling[i] / 2,
                    f'{data_0_time_pref_idling[i]:.3f}', ha='center', va='center',
                    color='black', fontsize=8,
                    bbox=dict(facecolor=color_codes['Color6'], edgecolor=color_codes['Color6'], boxstyle='round,pad=0.3'))
        if data_0_time_pref_driving[i] > 0:
            ax.text(bar_positions_0_time_pref[i] + 0.15,
                    data_0_time_pref_idling[i] + data_0_time_pref_driving[i] / 2,
                    f'{data_0_time_pref_driving[i]:.3f}', ha='center', va='center',
                    color='black', fontsize=8,
                    bbox=dict(facecolor=color_codes['Color7'], edgecolor=color_codes['Color7'], boxstyle='round,pad=0.3'))

    ax.set_xticks(bar_positions)
    ax.set_xticklabels(modes, fontsize=12)

    configure_ax(ax, 'External Costs of Climate Change (€-Cent/pkm)', minortick_interval=0.1, majortick_interval=0.2, show_legend=True)

    legend_labels = [
        Patch(facecolor=color_codes['Color7'], edgecolor='black', hatch='//', 
            label='Energy Production (Driving, 0\% Time Preference)'),
        Patch(facecolor=color_codes['Color6'], edgecolor='black', hatch='\\\\', 
            label='Energy Production (Idling, 0\% Time Preference)'),
        Patch(facecolor=color_codes['Color5'], edgecolor='black', hatch='//', 
            label='Energy Production (Driving, 1\% Time Preference)'),
        Patch(facecolor=color_codes['Color4'], edgecolor='black', hatch='\\\\', 
            label='Energy Production (Idling, 1\% Time Preference)')
    ]
    ax.legend(handles=legend_labels, loc='upper left', fontsize=10, frameon=False)

    # Save and show plot
    plt.savefig(os.path.join(figures_directory, 'external_costs_results_climate_change.pdf'))
    plt.savefig(os.path.join(figures_directory, 'external_costs_results_climate_change.svg'))
    #plt.show()


# ====================================================================================== #
#       LAND USE EXTERNAL COSTS
# ====================================================================================== #


def generate_land_use_costs_plot_standard(
        external_costs_results_1_time_pref_private_bicycle,
        external_costs_results_1_time_pref_shared_bicycle,
        external_costs_results_1_time_pref_private_pedelec,
        external_costs_results_1_time_pref_shared_pedelec,
        ax=None):

    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 6))

    modes = ['Private c-Bike', 'Shared c-Bike', 'Private e-Bike', 'Shared e-Bike']
    bar_positions = np.arange(len(modes))

    data_standard_idling = [
        external_costs_results_1_time_pref_private_bicycle['Cost by Category']['Land Use']['cost per pkm idling'],
        external_costs_results_1_time_pref_shared_bicycle['Cost by Category']['Land Use']['cost per pkm idling'],
        external_costs_results_1_time_pref_private_pedelec['Cost by Category']['Land Use']['cost per pkm idling'],
        external_costs_results_1_time_pref_shared_pedelec['Cost by Category']['Land Use']['cost per pkm idling']
    ]
    data_standard_moving = [
        external_costs_results_1_time_pref_private_bicycle['Cost by Category']['Land Use']['cost per pkm moving'],
        external_costs_results_1_time_pref_shared_bicycle['Cost by Category']['Land Use']['cost per pkm moving'],
        external_costs_results_1_time_pref_private_pedelec['Cost by Category']['Land Use']['cost per pkm moving'],
        external_costs_results_1_time_pref_shared_pedelec['Cost by Category']['Land Use']['cost per pkm moving']
    ]
    data_standard_stations = [
        external_costs_results_1_time_pref_private_bicycle['Cost by Category']['Land Use']['cost per pkm stations'],
        external_costs_results_1_time_pref_shared_bicycle['Cost by Category']['Land Use']['cost per pkm stations'],
        external_costs_results_1_time_pref_private_pedelec['Cost by Category']['Land Use']['cost per pkm stations'],
        external_costs_results_1_time_pref_shared_pedelec['Cost by Category']['Land Use']['cost per pkm stations']
    ]

    # Create stacked bars with hatch patterns for visual clarity
    bars_idling = ax.bar(bar_positions, data_standard_idling, width=0.4,
                         color=color_codes['Color4'], edgecolor='black',
                         label='Idling Costs', hatch='//', zorder=2)
    bars_moving = ax.bar(bar_positions, data_standard_moving, width=0.4,
                         bottom=data_standard_idling,
                         color=color_codes['Color5'], edgecolor='black',
                         label='Moving Costs', hatch='xx', zorder=2)
    bars_stations = ax.bar(bar_positions, data_standard_stations, width=0.4,
                           bottom=np.array(data_standard_idling) + np.array(data_standard_moving),
                           color=color_codes['Color6'], edgecolor='black',
                           label='Station Costs', hatch='\\\\', zorder=2)

    # Compute total external costs for each mode
    bar_height_sums = np.array(data_standard_idling) + np.array(data_standard_moving) + np.array(data_standard_stations)

    # Dynamically adjust the y-axis limit
    max_bar_height = max(bar_height_sums)
    ax.set_ylim(0, max_bar_height * 1.1)

    # Display total external costs above each bar
    for i in range(len(bar_positions)):
        if bar_height_sums[i] > 0:
            ax.text(bar_positions[i], bar_height_sums[i] + max_bar_height * 0.02,
                    f'{bar_height_sums[i]:.3f}', ha='center', va='bottom',
                    color='black', fontsize=10,
                    bbox=dict(facecolor=color_codes['Color8'], edgecolor=color_codes['Color8'], boxstyle='round,pad=0.3'))

    # Add labels for individual cost components within the bars
    for i in range(len(bar_positions)):
        if data_standard_idling[i] > 0:
            ax.text(bar_positions[i] - 0.2, data_standard_idling[i] / 2,
                    f'{data_standard_idling[i]:.3f}', ha='center', va='center',
                    color='black', fontsize=10,
                    bbox=dict(facecolor=color_codes['Color4'], edgecolor=color_codes['Color4'], boxstyle='round,pad=0.3'))
        if data_standard_moving[i] > 0:
            ax.text(bar_positions[i] + 0.2, data_standard_idling[i] + data_standard_moving[i] / 2,
                    f'{data_standard_moving[i]:.3f}', ha='center', va='center',
                    color='black', fontsize=10,
                    bbox=dict(facecolor=color_codes['Color5'], edgecolor=color_codes['Color5'], boxstyle='round,pad=0.3'))
        if data_standard_stations[i] > 0:
            ax.text(bar_positions[i] - 0.2, data_standard_idling[i] + data_standard_moving[i] + data_standard_stations[i] / 2,
                    f'{data_standard_stations[i]:.3f}', ha='center', va='center',
                    color='black', fontsize=10,
                    bbox=dict(facecolor=color_codes['Color6'], edgecolor=color_codes['Color6'], boxstyle='round,pad=0.3'))

    # Set x-axis labels
    ax.set_xticks(bar_positions)
    ax.set_xticklabels(modes, fontsize=12)

    configure_ax(ax, 'External Costs of Land Use (€-Cent/pkm)', minortick_interval=0.15, majortick_interval=0.3, show_legend=False)

    legend_labels = [
        Patch(facecolor=color_codes['Color6'], edgecolor='black', label='Sharing Station Costs', hatch='\\\\'),
        Patch(facecolor=color_codes['Color5'], edgecolor='black', label='Moving Infrastructure Costs', hatch='xx'),
        Patch(facecolor=color_codes['Color4'], edgecolor='black', label='Idling Opportunity Costs', hatch='//')
    ]
    ax.legend(handles=legend_labels, loc='upper right', fontsize=10, frameon=False)

    # Save and display the plot
    plt.savefig(os.path.join(figures_directory, 'external_costs_results_land_use.pdf'))
    plt.savefig(os.path.join(figures_directory, 'external_costs_results_land_use.svg'))
    #plt.show()


# ====================================================================================== #
#       COLLISIONS EXTERNAL COSTS
# ====================================================================================== #


def generate_collisions_costs_plot(
        external_costs_results_1_time_pref_private_bicycle,
        external_costs_results_causer_private_bicycle,
        external_costs_results_1_time_pref_shared_bicycle,
        external_costs_results_causer_shared_bicycle,
        external_costs_results_1_time_pref_private_pedelec,
        external_costs_results_causer_private_pedelec,
        external_costs_results_1_time_pref_shared_pedelec,
        external_costs_results_causer_shared_pedelec,
        ax=None):

    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 6))

    # Define x-axis labels for consistency with other external cost plots
    modes = ['Private c-Bike', 'Shared c-Bike', 'Private e-Bike', 'Shared e-Bike']
    bar_positions = np.arange(len(modes))
    bar_width = 0.4  # Define the width of each bar

    # Retrieve data for each method
    data_damage_potential = [
        external_costs_results_1_time_pref_private_bicycle['Cost by Category']['Collisions']['cost per pkm'],
        external_costs_results_1_time_pref_shared_bicycle['Cost by Category']['Collisions']['cost per pkm'],
        external_costs_results_1_time_pref_private_pedelec['Cost by Category']['Collisions']['cost per pkm'],
        external_costs_results_1_time_pref_shared_pedelec['Cost by Category']['Collisions']['cost per pkm']
    ]

    data_causer = [
        external_costs_results_causer_private_bicycle['Cost by Category']['Collisions']['cost per pkm'],
        external_costs_results_causer_shared_bicycle['Cost by Category']['Collisions']['cost per pkm'],
        external_costs_results_causer_private_pedelec['Cost by Category']['Collisions']['cost per pkm'],
        external_costs_results_causer_shared_pedelec['Cost by Category']['Collisions']['cost per pkm']
    ]

    # Create bars with hatch patterns for visual differentiation
    ax.bar(bar_positions - bar_width / 2, data_damage_potential, width=bar_width,
           color=color_codes['Color4'], edgecolor='black',
           label='Damage Potential Method', hatch='//', zorder=2)
    ax.bar(bar_positions + bar_width / 2, data_causer, width=bar_width,
           color=color_codes['Color5'], edgecolor='black',
           label='Cost-by-Cause Method', hatch='\\\\', zorder=2)

    # Determine the maximum bar height
    max_bar_height = max(max(data_damage_potential), max(data_causer))

    # Adjust the y-axis dynamically
    ax.set_ylim(0, max_bar_height * 1.1)

    # Display the total external costs above each bar
    for i in range(len(bar_positions)):
        if data_damage_potential[i] > 0:
            ax.text(bar_positions[i] - bar_width / 2, data_damage_potential[i] + max_bar_height * 0.02,
                    f'{data_damage_potential[i]:.2f}', ha='center', va='bottom',
                    color='black', fontsize=10,
                    bbox=dict(facecolor=color_codes['Color4'], edgecolor=color_codes['Color4'], boxstyle='round,pad=0.3'))
        if data_causer[i] > 0:
            ax.text(bar_positions[i] + bar_width / 2, data_causer[i] + max_bar_height * 0.02,
                    f'{data_causer[i]:.2f}', ha='center', va='bottom',
                    color='black', fontsize=10,
                    bbox=dict(facecolor=color_codes['Color5'], edgecolor=color_codes['Color5'], boxstyle='round,pad=0.3'))

    # Configure x-axis labels
    ax.set_xticks(bar_positions)
    ax.set_xticklabels(modes, fontsize=12)

    configure_ax(ax, 'External Costs of Collisions (€-Cent/pkm)', minortick_interval=1.25, majortick_interval=2.5, show_legend=False)

    legend_labels = [
        Patch(facecolor=color_codes['Color5'], edgecolor='black', label='Cost-by-Cause Method', hatch='\\\\'),
        Patch(facecolor=color_codes['Color4'], edgecolor='black', label='Damage Potential Method', hatch='//')
    ]
    ax.legend(handles=legend_labels, loc='upper left', fontsize=10, frameon=False)

    # Save and display the plot
    plt.savefig(os.path.join(figures_directory, 'external_costs_results_collisions.pdf'))
    plt.savefig(os.path.join(figures_directory, 'external_costs_results_collisions.svg'))
    #plt.show()


# ====================================================================================== #
#       BARRIER EFFECTS EXTERNAL COSTS
# ====================================================================================== #


def generate_barrier_effects_costs_plot(
        external_costs_results_1_time_pref_private_bicycle,
        external_costs_results_1_time_pref_shared_bicycle,
        external_costs_results_1_time_pref_private_pedelec,
        external_costs_results_1_time_pref_shared_pedelec,
        ax=None):

    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 6))
        plt.rcParams.update({'font.family': 'Arial'})

    # Define modes and bar width
    modes = ['Private c-Bike', 'Shared c-Bike', 'Private e-Bike', 'Shared e-Bike']
    bar_width = 0.4
    bar_positions = np.arange(len(modes))

    # Define data for barrier effects costs
    barrier_effects_costs = [
        external_costs_results_1_time_pref_private_bicycle['Cost by Category']['Barrier Effects']['cost per pkm'],
        external_costs_results_1_time_pref_shared_bicycle['Cost by Category']['Barrier Effects']['cost per pkm'],
        external_costs_results_1_time_pref_private_pedelec['Cost by Category']['Barrier Effects']['cost per pkm'],
        external_costs_results_1_time_pref_shared_pedelec['Cost by Category']['Barrier Effects']['cost per pkm']
    ]

    # Create bars (no hatching)
    bars = ax.bar(bar_positions, barrier_effects_costs, width=bar_width,
                  color=color_codes['Color5'], edgecolor='black', zorder=3)

    # Sum of bar heights for scaling
    max_bar_height = max(barrier_effects_costs) if max(barrier_effects_costs) > 0 else 0.01

    # Set consistent y-axis limit
    ax.set_ylim(0, max_bar_height * 1.1)

    # Display total external costs on top of bars
    for i in range(len(modes)):
        ax.text(bar_positions[i], barrier_effects_costs[i] + max_bar_height * 0.02,
                f'{barrier_effects_costs[i]:.3f}', ha='center', va='bottom',
                color='black', fontsize=10,
                bbox=dict(facecolor=color_codes['Color5'], edgecolor=color_codes['Color5'], boxstyle='round,pad=0.3'))

    ax.set_xticks(bar_positions)
    ax.set_xticklabels(modes, fontsize=12)

    configure_ax(ax, 'External Costs of Barrier Effects (€-Cent/pkm)', minortick_interval=0.005, majortick_interval=0.01, show_legend=False)

    plt.savefig(os.path.join(figures_directory, 'external_costs_results_barrier_effects.pdf'))
    plt.savefig(os.path.join(figures_directory, 'external_costs_results_barrier_effects.svg'))
    #plt.show()


# ====================================================================================== #
#       UPSTREAM PROCESSES EXTERNAL COSTS
# ====================================================================================== #


def generate_upstream_processes_costs_plot(
        external_costs_results_1_time_pref_private_bicycle,
        external_costs_results_0_time_pref_private_bicycle,
        external_costs_results_1_time_pref_shared_bicycle,
        external_costs_results_0_time_pref_shared_bicycle,
        external_costs_results_1_time_pref_private_pedelec,
        external_costs_results_0_time_pref_private_pedelec,
        external_costs_results_1_time_pref_shared_pedelec,
        external_costs_results_0_time_pref_shared_pedelec,
        ax=None):

    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 6))
        plt.rcParams.update({'font.family': 'Arial'})

    # Define modes and bar width
    modes = ['Private c-Bike', 'Shared c-Bike', 'Private e-Bike', 'Shared e-Bike']
    bar_width = 0.4
    bar_positions = np.arange(len(modes))

    # Define data
    data_1_time_pref = [
        external_costs_results_1_time_pref_private_bicycle['Cost by Category']['Upstream Processes']['cost per pkm'],
        external_costs_results_1_time_pref_shared_bicycle['Cost by Category']['Upstream Processes']['cost per pkm'],
        external_costs_results_1_time_pref_private_pedelec['Cost by Category']['Upstream Processes']['cost per pkm'],
        external_costs_results_1_time_pref_shared_pedelec['Cost by Category']['Upstream Processes']['cost per pkm']
    ]

    data_0_time_pref = [
        external_costs_results_0_time_pref_private_bicycle['Cost by Category']['Upstream Processes']['cost per pkm'],
        external_costs_results_0_time_pref_shared_bicycle['Cost by Category']['Upstream Processes']['cost per pkm'],
        external_costs_results_0_time_pref_private_pedelec['Cost by Category']['Upstream Processes']['cost per pkm'],
        external_costs_results_0_time_pref_shared_pedelec['Cost by Category']['Upstream Processes']['cost per pkm']
    ]

    # Colors for 1% and 0% Time Preference
    color_1_time_pref = color_codes['Color3']
    color_0_time_pref = color_codes['Color5']

    # Offset for grouped bars
    offset = bar_width / 2

    # Create bars (no hatching)
    bars_1 = ax.bar(bar_positions - offset, data_1_time_pref, width=bar_width, color=color_1_time_pref,
                    edgecolor='black', label='1\% Time Preference', zorder=3)
    bars_0 = ax.bar(bar_positions + offset, data_0_time_pref, width=bar_width, color=color_0_time_pref,
                    edgecolor='black', label='0\% Time Preference', zorder=3)

    # Sum of bar heights for scaling
    max_bar_height = max(max(data_1_time_pref), max(data_0_time_pref)) if max(max(data_1_time_pref), max(data_0_time_pref)) > 0 else 0.01

    # Set consistent y-axis limit
    ax.set_ylim(0, max_bar_height * 1.1)

    # Display total external costs on top of bars
    for bars, data in zip([bars_1, bars_0], [data_1_time_pref, data_0_time_pref]):
        for bar, value in zip(bars, data):
            if value > 0:
                ax.text(bar.get_x() + bar.get_width() / 2, value + max_bar_height * 0.02,
                        f'{value:.3f}', ha='center', va='bottom',
                        color='black', fontsize=10,
                        bbox=dict(facecolor=bar.get_facecolor(), edgecolor=bar.get_facecolor(), boxstyle='round,pad=0.3'))

    # Set x-axis labels correctly
    ax.set_xticks(bar_positions)
    ax.set_xticklabels(modes, fontsize=12)

    configure_ax(ax, 'External Costs of Upstream Processes (€-Cent/pkm)', minortick_interval=0.1, majortick_interval=0.2, show_legend=True)

    legend_labels = [
        Patch(facecolor=color_0_time_pref, edgecolor='black', label='0\% Preference'),
        Patch(facecolor=color_1_time_pref, edgecolor='black', label='1\% Time Preference')
    ]
    ax.legend(handles=legend_labels, loc='upper left', fontsize=10, frameon=False)

    plt.savefig(os.path.join(figures_directory, 'external_costs_results_upstream_processes.pdf'))
    plt.savefig(os.path.join(figures_directory, 'external_costs_results_upstream_processes.svg'))
    #plt.show()


# ====================================================================================== #
#       SERVICE FAILURE EXTERNAL COSTS
# ====================================================================================== #


def generate_service_failure_costs_plot(
        external_costs_results_1_time_pref_private_bicycle,
        external_costs_results_1_time_pref_shared_bicycle,
        external_costs_results_1_time_pref_private_pedelec,
        external_costs_results_1_time_pref_shared_pedelec,
        ax=None):

    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 6))
        plt.rcParams.update({'font.family': 'Arial'})

    # Define modes and bar width
    modes = ['Private c-Bike', 'Shared c-Bike', 'Private e-Bike', 'Shared e-Bike']
    bar_width = 0.4
    bar_positions = np.arange(len(modes))

    # Define data
    service_failure_costs = [
        external_costs_results_1_time_pref_private_bicycle['Cost by Category']['Service Failure']['cost per pkm'],
        external_costs_results_1_time_pref_shared_bicycle['Cost by Category']['Service Failure']['cost per pkm'],
        external_costs_results_1_time_pref_private_pedelec['Cost by Category']['Service Failure']['cost per pkm'],
        external_costs_results_1_time_pref_shared_pedelec['Cost by Category']['Service Failure']['cost per pkm']
    ]

    # Color for bars
    color_service_failure = color_codes['Color3']

    # Create bar plot without hatching
    bars = ax.bar(bar_positions, service_failure_costs, width=bar_width, color=color_service_failure,
                  edgecolor='black', zorder=3)

    # Set consistent y-axis limit
    max_bar_height = max(service_failure_costs) if max(service_failure_costs) > 0 else 0.01
    ax.set_ylim(0, max_bar_height * 1.1)

    # Display total external costs on top of bars
    for bar, value in zip(bars, service_failure_costs):
        if value > 0:
            ax.text(bar.get_x() + bar.get_width() / 2, value + max_bar_height * 0.02,
                    f'{value:.3f}', ha='center', va='bottom',
                    color='black', fontsize=10,
                    bbox=dict(facecolor=color_service_failure, edgecolor=color_service_failure, boxstyle='round,pad=0.3'))

    # Set x-axis labels correctly
    ax.set_xticks(bar_positions)
    ax.set_xticklabels(modes, fontsize=12)

    configure_ax(ax, 'External Costs of Service Failure (€-Cent/pkm)', minortick_interval=0.05, majortick_interval=0.1, show_legend=False)

    # Save the plot
    plt.savefig(os.path.join(figures_directory, 'external_costs_results_service_failure.pdf'))
    plt.savefig(os.path.join(figures_directory, 'external_costs_results_service_failure.svg'))
    plt.show()


# ====================================================================================== #
#       HEALTH BENEFITS EXTERNAL COSTS
# ====================================================================================== #


def generate_health_benefits_costs_plot(
        external_costs_results_1_time_pref_private_bicycle,
        external_costs_results_1_time_pref_shared_bicycle,
        external_costs_results_1_time_pref_private_pedelec,
        external_costs_results_1_time_pref_shared_pedelec, 
        ax=None):   

    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 6), dpi=100)

    # Define x-axis categories for consistency
    modes = ['Private c-Bike', 'Shared c-Bike', 'Private e-Bike', 'Shared e-Bike']
    bar_positions = np.arange(len(modes))
    bar_width = 0.5  # Define bar width

    # Retrieve data (negative values for health benefits)
    health_benefits_costs = [
        external_costs_results_1_time_pref_private_bicycle['Cost by Category']['Health Benefits']['cost per pkm'],
        external_costs_results_1_time_pref_shared_bicycle['Cost by Category']['Health Benefits']['cost per pkm'],
        external_costs_results_1_time_pref_private_pedelec['Cost by Category']['Health Benefits']['cost per pkm'],
        external_costs_results_1_time_pref_shared_pedelec['Cost by Category']['Health Benefits']['cost per pkm']
    ]

    # Color for bars (no hatch pattern)
    color_health_benefits = color_codes['Color2']

    # Create bar chart with unified style
    bars = ax.bar(bar_positions, health_benefits_costs, width=bar_width, color=color_health_benefits,
                  edgecolor='black', zorder=3)

    # Dynamically adjust the y-axis (negative values)
    min_cost = min(health_benefits_costs) * 1.1
    ax.set_ylim(min_cost, 0)

    # Move x-axis labels to the top
    ax.xaxis.tick_top()
    ax.xaxis.set_label_position('top')  

    # Set x-axis ticks and labels
    ax.set_xticks(bar_positions)
    ax.set_xticklabels(modes, fontsize=12)

    # Display values inside bars
    for bar, cost in zip(bars, health_benefits_costs):
        ax.text(bar.get_x() + bar.get_width() / 2, cost - 2, f'{cost:.3f}', 
                ha='center', va='center', color='black', fontsize=10, 
                bbox=dict(facecolor=color_health_benefits, edgecolor=color_health_benefits, boxstyle='round,pad=0.3'))

    configure_ax(ax, 'External Costs of Health Benefits (€-Cent/pkm)', minortick_interval=2.5, majortick_interval=5, show_legend=False)

    plt.savefig(os.path.join(figures_directory, 'external_costs_results_health_benefits.pdf'))
    plt.savefig(os.path.join(figures_directory, 'external_costs_results_health_benefits.svg'))
    #plt.show()


# ====================================================================================== #
#       TOTAL EXTERNAL COSTS INDIVIDUAL PLOTS COMBINED
# ====================================================================================== #


def generate_combined_external_costs_plot(
    external_costs_results_1_time_pref_private_bicycle,
    external_costs_results_0_time_pref_private_bicycle,
    external_costs_results_causer_private_bicycle,
    external_costs_results_1_time_pref_shared_bicycle,
    external_costs_results_0_time_pref_shared_bicycle,
    external_costs_results_causer_shared_bicycle,
    external_costs_results_1_time_pref_private_pedelec,
    external_costs_results_0_time_pref_private_pedelec,
    external_costs_results_causer_private_pedelec,
    external_costs_results_1_time_pref_shared_pedelec,
    external_costs_results_0_time_pref_shared_pedelec,
    external_costs_results_causer_shared_pedelec
):
    """
    Generates a combined plot of external costs across six categories arranged in a 3x2 grid.
    """

    # Set up a 3x2 grid for subplots (3 rows, 2 columns)
    fig, axs = plt.subplots(3, 2, figsize=(18, 24))

    # Generate individual plots using the correct subplot axes
    generate_air_pollution_costs_plot(
        external_costs_results_1_time_pref_private_bicycle,
        external_costs_results_1_time_pref_shared_bicycle,
        external_costs_results_1_time_pref_private_pedelec,
        external_costs_results_1_time_pref_shared_pedelec,
        ax=axs[0, 0]
    )

    generate_climate_change_costs_plot(
        external_costs_results_1_time_pref_private_bicycle,
        external_costs_results_0_time_pref_private_bicycle,
        external_costs_results_1_time_pref_shared_bicycle,
        external_costs_results_0_time_pref_shared_bicycle,
        external_costs_results_1_time_pref_private_pedelec,
        external_costs_results_0_time_pref_private_pedelec,
        external_costs_results_1_time_pref_shared_pedelec,
        external_costs_results_0_time_pref_shared_pedelec,
        ax=axs[0, 1]
    )

    generate_land_use_costs_plot_standard(
        external_costs_results_1_time_pref_private_bicycle,
        external_costs_results_1_time_pref_shared_bicycle,
        external_costs_results_1_time_pref_private_pedelec,
        external_costs_results_1_time_pref_shared_pedelec,
        ax=axs[1, 0]
    )

    generate_collisions_costs_plot(
        external_costs_results_1_time_pref_private_bicycle,
        external_costs_results_causer_private_bicycle,
        external_costs_results_1_time_pref_shared_bicycle,
        external_costs_results_causer_shared_bicycle,
        external_costs_results_1_time_pref_private_pedelec,
        external_costs_results_causer_private_pedelec,
        external_costs_results_1_time_pref_shared_pedelec,
        external_costs_results_causer_shared_pedelec,
        ax=axs[1, 1]
    )

    generate_upstream_processes_costs_plot(
        external_costs_results_1_time_pref_private_bicycle,
        external_costs_results_0_time_pref_private_bicycle,
        external_costs_results_1_time_pref_shared_bicycle,
        external_costs_results_0_time_pref_shared_bicycle,
        external_costs_results_1_time_pref_private_pedelec,
        external_costs_results_0_time_pref_private_pedelec,
        external_costs_results_1_time_pref_shared_pedelec,
        external_costs_results_0_time_pref_shared_pedelec,
        ax=axs[2, 0]
    )

    generate_service_failure_costs_plot(
        external_costs_results_1_time_pref_private_bicycle,
        external_costs_results_1_time_pref_shared_bicycle,
        external_costs_results_1_time_pref_private_pedelec,
        external_costs_results_1_time_pref_shared_pedelec,
        ax=axs[2, 1]
    )

    plt.tight_layout(rect=[0, 0, 1, 0.95])

    plt.savefig(os.path.join(figures_directory, 'combined_external_costs_results.svg'), format="svg")
    plt.savefig(os.path.join(figures_directory, 'combined_external_costs_results.pdf'), format="pdf")
    plt.show()


# ====================================================================================== #
#       TOTAL EXTERNAL COSTS
# ====================================================================================== #


def generate_external_costs_plot(
        external_costs_results_1_time_pref_private_bicycle,
        external_costs_results_1_time_pref_shared_bicycle,
        external_costs_results_1_time_pref_private_pedelec,
        external_costs_results_1_time_pref_shared_pedelec, 
        show_plot=True):

    # Define colors for each cost category
    colors = [
        color_codes['Color1'], color_codes['Color2'], color_codes['Color3'], 
        color_codes['Color4'], color_codes['Color5'], color_codes['Color6'], 
        color_codes['Color7'], color_codes['Color8']
    ]

    # Define external cost categories
    cost_categories = [
        "Air Pollution", "Climate Change", "Land Use", "Collisions", 
        "Barrier Effects", "Upstream Processes", "Service Failure"
    ]

    # Transport modes
    modes = ['Private c-Bike', 'Shared c-Bike', 'Private e-Bike', 'Shared e-Bike']
    num_modes = len(modes)
    bar_width = 0.5
    bar_positions = np.arange(num_modes)

    # Retrieve data for each category
    cost_data = [
        [external_costs_results_1_time_pref_private_bicycle['Cost by Category'][category]['cost per pkm'],
         external_costs_results_1_time_pref_shared_bicycle['Cost by Category'][category]['cost per pkm'],
         external_costs_results_1_time_pref_private_pedelec['Cost by Category'][category]['cost per pkm'],
         external_costs_results_1_time_pref_shared_pedelec['Cost by Category'][category]['cost per pkm']]
        for category in cost_categories
    ]

    # Create figure and axis
    fig, ax = plt.subplots(figsize=(10, 6))

    # Stacked bar chart with unified styling
    bottom_values = np.zeros(num_modes)
    for i, category in enumerate(cost_categories):
        bars = ax.bar(bar_positions, cost_data[i], width=bar_width, bottom=bottom_values,
                      label=f"{category} Costs", color=colors[i], zorder=3)

        # Add value labels, alternating left and right for better readability
        for j in range(num_modes):
            if cost_data[i][j] > 0:
                horizontal_offset = -0.3 if i % 2 == 0 else 0.3  # Alternate left/right
                ax.text(bar_positions[j] + horizontal_offset, bottom_values[j] + cost_data[i][j] / 2,
                        f'{cost_data[i][j]:.3f}', ha='center', va='center',
                        fontsize=10, color='black',zorder=5,
                        bbox=dict(facecolor=colors[i], edgecolor=colors[i], boxstyle='round,pad=0.3'))

        bottom_values += np.array(cost_data[i])

    # Display total external costs above bars
    max_bar_height = max(bottom_values)
    for i in range(num_modes):
        ax.text(bar_positions[i], bottom_values[i] + max_bar_height * 0.02,
                f'{bottom_values[i]:.2f}', ha='center', va='bottom',
                color='black', fontsize=10, zorder=5,
                bbox=dict(facecolor=colors[-1], edgecolor=colors[-1], boxstyle='round,pad=0.3'))

    # Configure axis labels, ticks, and grid
    ax.set_ylabel('Positive External Costs (€-Cent/pkm)', fontsize=12)
    ax.set_xticks(bar_positions)
    ax.set_xticklabels(modes, fontsize=12)
    ax.set_ylim(0, max_bar_height * 1.1)

    # Remove x-axis ticks
    ax.tick_params(axis='x', length=0)

    # Set tick spacing and minor/micro ticks
    ax.yaxis.set_major_locator(MultipleLocator(3))  # Major ticks every 1
    ax.yaxis.set_minor_locator(MultipleLocator(1.5))  # Minor ticks every 0.2

    # Grid settings
    ax.grid(axis='y', linestyle='--', alpha=0.5, linewidth=1.0, zorder=0)

    # Update legend with full category names
    legend_labels = [Patch(facecolor=colors[i], label=f"{cost_categories[i]} Costs") for i in range(len(cost_categories))]
    ax.legend(handles=legend_labels, loc='upper left', fontsize=10, frameon=False)
    
    plt.tight_layout()
    plt.savefig(os.path.join(figures_directory, 'external_costs_results.pdf'))
    plt.savefig(os.path.join(figures_directory, 'external_costs_results.svg'))
    plt.show()


# ====================================================================================== #
#       TOTAL EXTERNAL COSTS WITHOUT COLLISIONS COSTS
# ====================================================================================== #


def generate_external_costs_without_collisions_plot(
        external_costs_results_1_time_pref_private_bicycle,
        external_costs_results_1_time_pref_shared_bicycle,
        external_costs_results_1_time_pref_private_pedelec,
        external_costs_results_1_time_pref_shared_pedelec,
        show_plot=True):
    
    # Define colors for each cost category
    colors = [
        color_codes['Color1'], color_codes['Color2'], color_codes['Color3'], 
        color_codes['Color4'], color_codes['Color5'], color_codes['Color6'], 
        color_codes['Color7']
    ]

    # External cost categories (excluding collision costs)
    categories = {
        "Air Pollution": [],
        "Climate Change": [],
        "Land Use": [],
        "Barrier Effects": [],
        "Upstream Processes": [],
        "Service Failure": []
    }

    # Extract data from results
    modes = ['Private c-Bike', 'Shared c-Bike', 'Private e-Bike', 'Shared e-Bike']
    sources = [external_costs_results_1_time_pref_private_bicycle, external_costs_results_1_time_pref_shared_bicycle,
               external_costs_results_1_time_pref_private_pedelec, external_costs_results_1_time_pref_shared_pedelec]

    for category in categories.keys():
        for source in sources:
            categories[category].append(source['Cost by Category'][category]['cost per pkm'])

    # Number of bars and bar positions
    num_bars = len(modes)
    bar_width = 0.5
    bar_positions = np.arange(num_bars)

    # Create plot
    fig, ax = plt.subplots(figsize=(10, 6))
    #plt.rcParams.update({'font.family': 'Arial'})

    # Stack bars for each category
    cumulative_heights = np.zeros(num_bars)
    bar_handles = []
    
    for i, (category, values) in enumerate(categories.items()):
        bars = ax.bar(bar_positions, values, width=bar_width, bottom=cumulative_heights,
                      label=category, color=colors[i], zorder=3)
        bar_handles.append(bars)
        cumulative_heights += np.array(values)

        # Add labels with alternating left/right placement
        for j in range(num_bars):
            if values[j] > 0:
                horizontal_offset = -0.2 if i % 2 == 0 else 0.2
                ax.text(bar_positions[j] + horizontal_offset, cumulative_heights[j] - values[j] / 2,
                        f'{values[j]:.3f}', ha='center', va='center',
                        fontsize=10, color='black', zorder=5,
                        bbox=dict(facecolor=colors[i], edgecolor=colors[i], boxstyle='round,pad=0.3'))

    # Display total external costs above bars
    max_bar_height = max(cumulative_heights)
    for i in range(num_bars):
        ax.text(bar_positions[i], cumulative_heights[i] + max_bar_height * 0.02,
                f'{cumulative_heights[i]:.2f}', ha='center', va='bottom',
                color='white', fontsize=10, zorder=5,
                bbox=dict(facecolor=colors[-1], edgecolor=colors[-1], boxstyle='round,pad=0.3'))

    # Configure axis labels, ticks, and grid
    ax.set_ylabel('Positive External Costs Without Collisions (€-Cent/pkm)', fontsize=12)
    ax.set_xticks(bar_positions)
    ax.set_xticklabels(modes, fontsize=12)
    ax.set_ylim(0, max_bar_height * 1.1)

    # Remove x-axis ticks
    ax.tick_params(axis='x', length=0)

    # Set tick spacing and minor/micro ticks
    ax.yaxis.set_major_locator(MultipleLocator(1))  
    ax.yaxis.set_minor_locator(MultipleLocator(0.2))  
    ax.yaxis.set_minor_locator(AutoMinorLocator(5))  

    # Grid settings
    ax.grid(axis='y', linestyle='--', alpha=0.5, linewidth=1.0, zorder=0)

    legend_labels = [Patch(facecolor=colors[i], label=f"{list(categories.keys())[i]} Costs") for i in range(len(categories))]
    ax.legend(handles=legend_labels, loc='upper left', fontsize=10, frameon=False)

    plt.tight_layout()
    plt.savefig(os.path.join(figures_directory, 'external_costs_results_without_collisions.pdf'))
    plt.savefig(os.path.join(figures_directory, 'external_costs_results_without_collisions.svg'))
    plt.show()


# ====================================================================================== #
#       TOTAL EXTERNAL COSTS WITH HEALTH BENEFITS
# ====================================================================================== #


def generate_external_costs_with_health_benefits_plot(
        external_costs_results_1_time_pref_private_bicycle,
        external_costs_results_1_time_pref_shared_bicycle,
        external_costs_results_1_time_pref_private_pedelec,
        external_costs_results_1_time_pref_shared_pedelec, 
        show_plot=True):

    colors = [
        color_codes['Color1'], color_codes['Color2'], color_codes['Color3'], 
        color_codes['Color4'], color_codes['Color5'], color_codes['Color6'], 
        color_codes['Color7'], color_codes['Color8'], color_codes['Color9']
    ]

    categories = {
        "Air Pollution": [],
        "Climate Change": [],
        "Land Use": [],
        "Collisions": [],
        "Barrier Effects": [],
        "Upstream Processes": [],
        "Service Failure": [],
        "Health Benefits": []  # Negativer Wert
    }

    modes = ['Private c-Bike', 'Shared c-Bike', 'Private e-Bike', 'Shared e-Bike']
    sources = [external_costs_results_1_time_pref_private_bicycle, external_costs_results_1_time_pref_shared_bicycle,
               external_costs_results_1_time_pref_private_pedelec, external_costs_results_1_time_pref_shared_pedelec]

    for category in categories.keys():
        for source in sources:
            categories[category].append(source['Cost by Category'][category]['cost per pkm'])

    num_bars = len(modes)
    bar_width = 0.5
    bar_positions = np.arange(num_bars)

    fig, ax = plt.subplots(figsize=(10, 6))
    plt.rcParams.update({'font.family': 'Arial'})

    cumulative_heights = np.zeros(num_bars)
    bar_handles = []
    
    for i, (category, values) in enumerate(categories.items()):
        if category == "Health Benefits":
            continue  # Health Benefits als eigene Balken

        bars = ax.bar(bar_positions, values, width=bar_width, bottom=cumulative_heights,
                      label=category, color=colors[i], edgecolor='black', zorder=3)
        bar_handles.append(bars)
        cumulative_heights += np.array(values)

    # Health Benefits als eigene Balken unterhalb der x-Achse
    bars_health = ax.bar(bar_positions, categories["Health Benefits"], width=bar_width,
                         color=colors[-1], edgecolor='black', label="Health Benefits", zorder=3)
    bar_handles.append(bars_health)

    # Gesamtwerte für externe Kosten (ohne Health Benefits)
    max_bar_height = max(cumulative_heights)
    min_bar_height = min(categories["Health Benefits"])  # Negative Werte berücksichtigen

    # Werte auf den Balken anzeigen (nur für positive Kosten)
    for i in range(num_bars):
        ax.text(bar_positions[i], cumulative_heights[i] + max_bar_height * 0.02,
                f'{cumulative_heights[i]:.2f}', ha='center', va='bottom',
                color='black', fontsize=10,
                bbox=dict(facecolor=colors[7], edgecolor=colors[7], boxstyle='round,pad=0.3'))

    # Werte für Health Benefits direkt im Balken anzeigen
    for i in range(num_bars):
        ax.text(bar_positions[i], categories["Health Benefits"][i] - max_bar_height * 0.02,
                f'{categories["Health Benefits"][i]:.2f}', ha='center', va='top',
                color='black', fontsize=10,
                bbox=dict(facecolor=colors[-1], edgecolor=colors[-1], boxstyle='round,pad=0.3'))

    ax.set_ylabel('External Costs (€-Cent/pkm)', fontsize=12)
    ax.set_xticks(bar_positions)
    ax.set_xticklabels(modes, fontsize=12)
    ax.set_ylim(min_bar_height * 1.2, max_bar_height * 1.1) 
    ax.yaxis.set_minor_locator(MultipleLocator(1))
    ax.grid(axis='y', linestyle='--', alpha=0.5, linewidth=1.0, zorder=0)

    ax.legend(handles=[bars[0] for bars in bar_handles], loc='upper left', fontsize=10, frameon=False)

    plt.tight_layout()
    plt.savefig(os.path.join(figures_directory, 'external_costs_results_with_health_benefits.pdf'))
    plt.savefig(os.path.join(figures_directory, 'external_costs_results_with_health_benefits.svg'))
    plt.show()
