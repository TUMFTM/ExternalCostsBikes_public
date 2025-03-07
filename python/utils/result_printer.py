# ====================================================================================== #
#       PRIVATE BICYCLE RESULTS
# ====================================================================================== #


def PrintExternalCostsPrivateBicycle(external_costs_results_1_time_pref_private_bicycle):

    print('\n=================================================================================') 
    print('#                         EXTERNAL COSTS PRIVATE BICYCLE                          #')
    print('===================================================================================')
    print('CATEGORIES PRIVATE BICYCLE')
    print('    Air Pollution')
    print('         Air Pollution costs per vkm                               : {:6.2f} €-ct/vkm'.format(external_costs_results_1_time_pref_private_bicycle['Cost by Category']['Air Pollution']['cost per vkm']))
    print('         Air Pollution costs per pkm                               : {:6.2f} €-ct/pkm'.format(external_costs_results_1_time_pref_private_bicycle['Cost by Category']['Air Pollution']['cost per pkm']))
    print('         Air Pollution costs per year                              : {:6.2f} €/year'.format(external_costs_results_1_time_pref_private_bicycle['Cost by Category']['Air Pollution']['cost per year']))
    print('    Climate Change 1% time preference')
    print('         Climate Change 1% time preference costs per vkm           : {:6.2f} €-ct/vkm'.format(external_costs_results_1_time_pref_private_bicycle['Cost by Category']['Climate Change']['cost per vkm']))
    print('         Climate Change 1% time preference costs per pkm           : {:6.2f} €-ct/pkm'.format(external_costs_results_1_time_pref_private_bicycle['Cost by Category']['Climate Change']['cost per pkm']))
    print('         Climate Change 1% time preference costs per year          : {:6.2f} €/year'.format(external_costs_results_1_time_pref_private_bicycle['Cost by Category']['Climate Change']['cost per year']))
    print('    Land Use')
    print('         Land Use costs per vkm                                    : {:6.2f} €-ct/vkm'.format(external_costs_results_1_time_pref_private_bicycle['Cost by Category']['Land Use']['cost per vkm']))
    print('         Land Use costs per pkm                                    : {:6.2f} €-ct/pkm'.format(external_costs_results_1_time_pref_private_bicycle['Cost by Category']['Land Use']['cost per pkm']))
    print('         Land Use costs per year                                   : {:6.2f} €/year'.format(external_costs_results_1_time_pref_private_bicycle['Cost by Category']['Land Use']['cost per year']))
    print('    Collisions Damage Potential')
    print('         Collisions Damage Potential costs per vkm                 : {:6.2f} €-ct/vkm'.format(external_costs_results_1_time_pref_private_bicycle['Cost by Category']['Collisions']['cost per vkm']))
    print('         Collisions Damage Potential costs per pkm                 : {:6.2f} €-ct/pkm'.format(external_costs_results_1_time_pref_private_bicycle['Cost by Category']['Collisions']['cost per pkm']))
    print('         Collisions Damage Potential costs per year                : {:6.2f} €/year'.format(external_costs_results_1_time_pref_private_bicycle['Cost by Category']['Collisions']['cost per year']))
    print('    Barrier Effects')
    print('         Barrier Effects costs per vkm                             : {:6.2f} €-ct/vkm'.format(external_costs_results_1_time_pref_private_bicycle['Cost by Category']['Barrier Effects']['cost per vkm']))
    print('         Barrier Effects costs per pkm                             : {:6.2f} €-ct/pkm'.format(external_costs_results_1_time_pref_private_bicycle['Cost by Category']['Barrier Effects']['cost per pkm']))
    print('         Barrier Effects costs per year                            : {:6.2f} €/year'.format(external_costs_results_1_time_pref_private_bicycle['Cost by Category']['Barrier Effects']['cost per year']))
    print('    Upstream Processes 1% time preference')
    print('         Upstream Processes 1% time preference costs per vkm       : {:6.2f} €-ct/vkm'.format(external_costs_results_1_time_pref_private_bicycle['Cost by Category']['Upstream Processes']['cost per vkm']))
    print('         Upstream Processes 1% time preference costs per pkm       : {:6.2f} €-ct/pkm'.format(external_costs_results_1_time_pref_private_bicycle['Cost by Category']['Upstream Processes']['cost per pkm']))
    print('         Upstream Processes 1% time preference costs per year      : {:6.2f} €/year'.format(external_costs_results_1_time_pref_private_bicycle['Cost by Category']['Upstream Processes']['cost per year']))
    print('    Service Failure')
    print('         Service Failure costs per vkm                             : {:6.2f} €-ct/vkm'.format(external_costs_results_1_time_pref_private_bicycle['Cost by Category']['Service Failure']['cost per vkm']))
    print('         Service Failure costs per pkm                             : {:6.2f} €-ct/pkm'.format(external_costs_results_1_time_pref_private_bicycle['Cost by Category']['Service Failure']['cost per pkm']))
    print('         Service Failure costs per year                            : {:6.2f} €/year'.format(external_costs_results_1_time_pref_private_bicycle['Cost by Category']['Service Failure']['cost per year']))
    print('    Health Benefits')
    print('         Health Benefits costs per vkm                             : {:6.2f} €-ct/vkm'.format(external_costs_results_1_time_pref_private_bicycle['Cost by Category']['Health Benefits']['cost per vkm']))
    print('         Health Benefits  costs per pkm                            : {:6.2f} €-ct/pkm'.format(external_costs_results_1_time_pref_private_bicycle['Cost by Category']['Health Benefits']['cost per pkm']))
    print('         Health Benefits costs per year                            : {:6.2f} €/year'.format(external_costs_results_1_time_pref_private_bicycle['Cost by Category']['Health Benefits']['cost per year']))
    print('TOTAL EXTERNAL COSTS BICYCLE')
    print('    Total cost per vkm                                             : {:6.2f} €-ct/vkm'.format(external_costs_results_1_time_pref_private_bicycle['Total Cost']['total cost per vkm']))
    print('    Total cost per pkm                                             : {:6.2f} €-ct/pkm'.format(external_costs_results_1_time_pref_private_bicycle['Total Cost']['total cost per pkm']))
    print('    Total cost per year                                            : {:6.2f} €/year'.format(external_costs_results_1_time_pref_private_bicycle['Total Cost']['total cost per year']))


# ====================================================================================== #
#       SHARED BICYCLE RESULTS
# ====================================================================================== #


def PrintExternalCostsSharedBicycle(external_costs_results_1_time_pref_shared_bicycle):

    print('\n=================================================================================') 
    print('#                         EXTERNAL COSTS SHARED BICYCLE                           #')
    print('===================================================================================')
    print('CATEGORIES SHARED BICYCLE')
    print('    Air Pollution')
    print('         Air Pollution costs per vkm                               : {:6.2f} €-ct/vkm'.format(external_costs_results_1_time_pref_shared_bicycle['Cost by Category']['Air Pollution']['cost per vkm']))
    print('         Air Pollution costs per pkm                               : {:6.2f} €-ct/pkm'.format(external_costs_results_1_time_pref_shared_bicycle['Cost by Category']['Air Pollution']['cost per pkm']))
    print('         Air Pollution costs per year                              : {:6.2f} €/year'.format(external_costs_results_1_time_pref_shared_bicycle['Cost by Category']['Air Pollution']['cost per year']))
    print('    Climate Change 1% time preference')
    print('         Climate Change 1% time preference costs per vkm           : {:6.2f} €-ct/vkm'.format(external_costs_results_1_time_pref_shared_bicycle['Cost by Category']['Climate Change']['cost per vkm']))
    print('         Climate Change 1% time preference costs per pkm           : {:6.2f} €-ct/pkm'.format(external_costs_results_1_time_pref_shared_bicycle['Cost by Category']['Climate Change']['cost per pkm']))
    print('         Climate Change 1% time preference costs per year          : {:6.2f} €/year'.format(external_costs_results_1_time_pref_shared_bicycle['Cost by Category']['Climate Change']['cost per year']))
    print('    Land Use')
    print('         Land Use costs per vkm                                    : {:6.2f} €-ct/vkm'.format(external_costs_results_1_time_pref_shared_bicycle['Cost by Category']['Land Use']['cost per vkm']))
    print('         Land Use costs per pkm                                    : {:6.2f} €-ct/pkm'.format(external_costs_results_1_time_pref_shared_bicycle['Cost by Category']['Land Use']['cost per pkm']))
    print('         Land Use costs per year                                   : {:6.2f} €/year'.format(external_costs_results_1_time_pref_shared_bicycle['Cost by Category']['Land Use']['cost per year']))
    print('    Collisions Damage Potential')
    print('         Collisions Damage Potential costs per vkm                 : {:6.2f} €-ct/vkm'.format(external_costs_results_1_time_pref_shared_bicycle['Cost by Category']['Collisions']['cost per vkm']))
    print('         Collisions Damage Potential costs per pkm                 : {:6.2f} €-ct/pkm'.format(external_costs_results_1_time_pref_shared_bicycle['Cost by Category']['Collisions']['cost per pkm']))
    print('         Collisions Damage Potential costs per year                : {:6.2f} €/year'.format(external_costs_results_1_time_pref_shared_bicycle['Cost by Category']['Collisions']['cost per year']))
    print('    Barrier Effects')
    print('         Barrier Effects costs per vkm                             : {:6.2f} €-ct/vkm'.format(external_costs_results_1_time_pref_shared_bicycle['Cost by Category']['Barrier Effects']['cost per vkm']))
    print('         Barrier Effects costs per pkm                             : {:6.2f} €-ct/pkm'.format(external_costs_results_1_time_pref_shared_bicycle['Cost by Category']['Barrier Effects']['cost per pkm']))
    print('         Barrier Effects costs per year                            : {:6.2f} €/year'.format(external_costs_results_1_time_pref_shared_bicycle['Cost by Category']['Barrier Effects']['cost per year']))
    print('    Upstream Processes 1% time preference')
    print('         Upstream Processes 1% time preference costs per vkm       : {:6.2f} €-ct/vkm'.format(external_costs_results_1_time_pref_shared_bicycle['Cost by Category']['Upstream Processes']['cost per vkm']))
    print('         Upstream Processes 1% time preference costs per pkm       : {:6.2f} €-ct/pkm'.format(external_costs_results_1_time_pref_shared_bicycle['Cost by Category']['Upstream Processes']['cost per pkm']))
    print('         Upstream Processes 1% time preference costs per year      : {:6.2f} €/year'.format(external_costs_results_1_time_pref_shared_bicycle['Cost by Category']['Upstream Processes']['cost per year']))
    print('    Service Failure')
    print('         Service Failure costs per vkm                             : {:6.2f} €-ct/vkm'.format(external_costs_results_1_time_pref_shared_bicycle['Cost by Category']['Service Failure']['cost per vkm']))
    print('         Service Failure costs per pkm                             : {:6.2f} €-ct/pkm'.format(external_costs_results_1_time_pref_shared_bicycle['Cost by Category']['Service Failure']['cost per pkm']))
    print('         Service Failure costs per year                            : {:6.2f} €/year'.format(external_costs_results_1_time_pref_shared_bicycle['Cost by Category']['Service Failure']['cost per year']))
    print('    Health Benefits')
    print('         Health Benefits costs per vkm                             : {:6.2f} €-ct/vkm'.format(external_costs_results_1_time_pref_shared_bicycle['Cost by Category']['Health Benefits']['cost per vkm']))
    print('         Health Benefits  costs per pkm                            : {:6.2f} €-ct/pkm'.format(external_costs_results_1_time_pref_shared_bicycle['Cost by Category']['Health Benefits']['cost per pkm']))
    print('         Health Benefits costs per year                            : {:6.2f} €/year'.format(external_costs_results_1_time_pref_shared_bicycle['Cost by Category']['Health Benefits']['cost per year']))
    print('TOTAL EXTERNAL COSTS BICYCLE')
    print('    Total cost per vkm                                             : {:6.2f} €-ct/vkm'.format(external_costs_results_1_time_pref_shared_bicycle['Total Cost']['total cost per vkm']))
    print('    Total cost per pkm                                             : {:6.2f} €-ct/pkm'.format(external_costs_results_1_time_pref_shared_bicycle['Total Cost']['total cost per pkm']))
    print('    Total cost per year                                            : {:6.2f} €/year'.format(external_costs_results_1_time_pref_shared_bicycle['Total Cost']['total cost per year']))


# ====================================================================================== #
#       PRIVATE PEDELEC RESULTS
# ====================================================================================== #


def PrintExternalCostsPrivatePedelec(external_costs_results_1_time_pref_private_pedelec):

    print('\n=================================================================================') 
    print('#                         EXTERNAL COSTS PRIVATE PEDELEC                          #')
    print('===================================================================================')
    print('CATEGORIES PRIVATE PEDELEC')
    print('    Air Pollution')
    print('         Air Pollution costs per vkm                               : {:6.2f} €-ct/vkm'.format(external_costs_results_1_time_pref_private_pedelec['Cost by Category']['Air Pollution']['cost per vkm']))
    print('         Air Pollution costs per pkm                               : {:6.2f} €-ct/pkm'.format(external_costs_results_1_time_pref_private_pedelec['Cost by Category']['Air Pollution']['cost per pkm']))
    print('         Air Pollution costs per year                              : {:6.2f} €/year'.format(external_costs_results_1_time_pref_private_pedelec['Cost by Category']['Air Pollution']['cost per year']))
    print('    Climate Change 1% time preference')
    print('         Climate Change 1% time preference costs per vkm           : {:6.2f} €-ct/vkm'.format(external_costs_results_1_time_pref_private_pedelec['Cost by Category']['Climate Change']['cost per vkm']))
    print('         Climate Change 1% time preference costs per pkm           : {:6.2f} €-ct/pkm'.format(external_costs_results_1_time_pref_private_pedelec['Cost by Category']['Climate Change']['cost per pkm']))
    print('         Climate Change 1% time preference costs per year          : {:6.2f} €/year'.format(external_costs_results_1_time_pref_private_pedelec['Cost by Category']['Climate Change']['cost per year']))
    print('    Land Use')
    print('         Land Use costs per vkm                                    : {:6.2f} €-ct/vkm'.format(external_costs_results_1_time_pref_private_pedelec['Cost by Category']['Land Use']['cost per vkm']))
    print('         Land Use costs per pkm                                    : {:6.2f} €-ct/pkm'.format(external_costs_results_1_time_pref_private_pedelec['Cost by Category']['Land Use']['cost per pkm']))
    print('         Land Use costs per year                                   : {:6.2f} €/year'.format(external_costs_results_1_time_pref_private_pedelec['Cost by Category']['Land Use']['cost per year']))
    print('    Collisions Damage Potential')
    print('         Collisions Damage Potential costs per vkm                  : {:6.2f} €-ct/vkm'.format(external_costs_results_1_time_pref_private_pedelec['Cost by Category']['Collisions']['cost per vkm']))
    print('         Collisions Damage Potential costs per pkm                  : {:6.2f} €-ct/pkm'.format(external_costs_results_1_time_pref_private_pedelec['Cost by Category']['Collisions']['cost per pkm']))
    print('         Collisions Damage Potential costs per year                 : {:6.2f} €/year'.format(external_costs_results_1_time_pref_private_pedelec['Cost by Category']['Collisions']['cost per year']))
    print('    Barrier Effects')
    print('         Barrier Effects costs per vkm                             : {:6.2f} €-ct/vkm'.format(external_costs_results_1_time_pref_private_pedelec['Cost by Category']['Barrier Effects']['cost per vkm']))
    print('         Barrier Effects costs per pkm                             : {:6.2f} €-ct/pkm'.format(external_costs_results_1_time_pref_private_pedelec['Cost by Category']['Barrier Effects']['cost per pkm']))
    print('         Barrier Effects costs per year                            : {:6.2f} €/year'.format(external_costs_results_1_time_pref_private_pedelec['Cost by Category']['Barrier Effects']['cost per year']))
    print('    Upstream Processes 1% time preference')
    print('         Upstream Processes 1% time preference costs per vkm       : {:6.2f} €-ct/vkm'.format(external_costs_results_1_time_pref_private_pedelec['Cost by Category']['Upstream Processes']['cost per vkm']))
    print('         Upstream Processes 1% time preference costs per pkm       : {:6.2f} €-ct/pkm'.format(external_costs_results_1_time_pref_private_pedelec['Cost by Category']['Upstream Processes']['cost per pkm']))
    print('         Upstream Processes 1% time preference costs per year      : {:6.2f} €/year'.format(external_costs_results_1_time_pref_private_pedelec['Cost by Category']['Upstream Processes']['cost per year']))
    print('    Service Failure')
    print('         Service Failure costs per vkm                             : {:6.2f} €-ct/vkm'.format(external_costs_results_1_time_pref_private_pedelec['Cost by Category']['Service Failure']['cost per vkm']))
    print('         Service Failure costs per pkm                             : {:6.2f} €-ct/pkm'.format(external_costs_results_1_time_pref_private_pedelec['Cost by Category']['Service Failure']['cost per pkm']))
    print('         Service Failure costs per year                            : {:6.2f} €/year'.format(external_costs_results_1_time_pref_private_pedelec['Cost by Category']['Service Failure']['cost per year']))
    print('    Health Benefits')
    print('         Health Benefits costs per vkm                             : {:6.2f} €-ct/vkm'.format(external_costs_results_1_time_pref_private_pedelec['Cost by Category']['Health Benefits']['cost per vkm']))
    print('         Health Benefits  costs per pkm                            : {:6.2f} €-ct/pkm'.format(external_costs_results_1_time_pref_private_pedelec['Cost by Category']['Health Benefits']['cost per pkm']))
    print('         Health Benefits costs per year                            : {:6.2f} €/year'.format(external_costs_results_1_time_pref_private_pedelec['Cost by Category']['Health Benefits']['cost per year']))
    print('TOTAL EXTERNAL COSTS PEDELEC')
    print('    Total cost per vkm                                             : {:6.2f} €-ct/vkm'.format(external_costs_results_1_time_pref_private_pedelec['Total Cost']['total cost per vkm']))
    print('    Total cost per pkm                                             : {:6.2f} €-ct/pkm'.format(external_costs_results_1_time_pref_private_pedelec['Total Cost']['total cost per pkm']))
    print('    Total cost per year                                            : {:6.2f} €/year'.format(external_costs_results_1_time_pref_private_pedelec['Total Cost']['total cost per year']))


# ====================================================================================== #
#       SHARED PEDELEC RESULTS
# ====================================================================================== #


def PrintExternalCostsSharedPedelec(external_costs_results_1_time_pref_shared_pedelec):

    print('\n=================================================================================') 
    print('#                         EXTERNAL COSTS SHARED PEDELEC                           #')
    print('===================================================================================')
    print('CATEGORIES SHARED PEDELEC')
    print('    Air Pollution')
    print('         Air Pollution costs per vkm                               : {:6.2f} €-ct/vkm'.format(external_costs_results_1_time_pref_shared_pedelec['Cost by Category']['Air Pollution']['cost per vkm']))
    print('         Air Pollution costs per pkm                               : {:6.2f} €-ct/pkm'.format(external_costs_results_1_time_pref_shared_pedelec['Cost by Category']['Air Pollution']['cost per pkm']))
    print('         Air Pollution costs per year                              : {:6.2f} €/year'.format(external_costs_results_1_time_pref_shared_pedelec['Cost by Category']['Air Pollution']['cost per year']))
    print('    Climate Change 1% time preference')
    print('         Climate Change 1% time preference costs per vkm           : {:6.2f} €-ct/vkm'.format(external_costs_results_1_time_pref_shared_pedelec['Cost by Category']['Climate Change']['cost per vkm']))
    print('         Climate Change 1% time preference costs per pkm           : {:6.2f} €-ct/pkm'.format(external_costs_results_1_time_pref_shared_pedelec['Cost by Category']['Climate Change']['cost per pkm']))
    print('         Climate Change 1% time preference costs per year          : {:6.2f} €/year'.format(external_costs_results_1_time_pref_shared_pedelec['Cost by Category']['Climate Change']['cost per year']))
    print('    Land Use')
    print('         Land Use costs per vkm                                    : {:6.2f} €-ct/vkm'.format(external_costs_results_1_time_pref_shared_pedelec['Cost by Category']['Land Use']['cost per vkm']))
    print('         Land Use costs per pkm                                    : {:6.2f} €-ct/pkm'.format(external_costs_results_1_time_pref_shared_pedelec['Cost by Category']['Land Use']['cost per pkm']))
    print('         Land Use costs per year                                   : {:6.2f} €/year'.format(external_costs_results_1_time_pref_shared_pedelec['Cost by Category']['Land Use']['cost per year']))
    print('    Collisions Damage Potential')
    print('         Collisions Damage Potential costs per vkm                  : {:6.2f} €-ct/vkm'.format(external_costs_results_1_time_pref_shared_pedelec['Cost by Category']['Collisions']['cost per vkm']))
    print('         Collisions Damage Potential costs per pkm                  : {:6.2f} €-ct/pkm'.format(external_costs_results_1_time_pref_shared_pedelec['Cost by Category']['Collisions']['cost per pkm']))
    print('         Collisions Damage Potential costs per year                 : {:6.2f} €/year'.format(external_costs_results_1_time_pref_shared_pedelec['Cost by Category']['Collisions']['cost per year']))
    print('    Barrier Effects')
    print('         Barrier Effects costs per vkm                             : {:6.2f} €-ct/vkm'.format(external_costs_results_1_time_pref_shared_pedelec['Cost by Category']['Barrier Effects']['cost per vkm']))
    print('         Barrier Effects costs per pkm                             : {:6.2f} €-ct/pkm'.format(external_costs_results_1_time_pref_shared_pedelec['Cost by Category']['Barrier Effects']['cost per pkm']))
    print('         Barrier Effects costs per year                            : {:6.2f} €/year'.format(external_costs_results_1_time_pref_shared_pedelec['Cost by Category']['Barrier Effects']['cost per year']))
    print('    Upstream Processes 1% time preference')
    print('         Upstream Processes 1% time preference costs per vkm       : {:6.2f} €-ct/vkm'.format(external_costs_results_1_time_pref_shared_pedelec['Cost by Category']['Upstream Processes']['cost per vkm']))
    print('         Upstream Processes 1% time preference costs per pkm       : {:6.2f} €-ct/pkm'.format(external_costs_results_1_time_pref_shared_pedelec['Cost by Category']['Upstream Processes']['cost per pkm']))
    print('         Upstream Processes 1% time preference costs per year      : {:6.2f} €/year'.format(external_costs_results_1_time_pref_shared_pedelec['Cost by Category']['Upstream Processes']['cost per year']))
    print('    Service Failure')
    print('         Service Failure costs per vkm                             : {:6.2f} €-ct/vkm'.format(external_costs_results_1_time_pref_shared_pedelec['Cost by Category']['Service Failure']['cost per vkm']))
    print('         Service Failure costs per pkm                             : {:6.2f} €-ct/pkm'.format(external_costs_results_1_time_pref_shared_pedelec['Cost by Category']['Service Failure']['cost per pkm']))
    print('         Service Failure costs per year                            : {:6.2f} €/year'.format(external_costs_results_1_time_pref_shared_pedelec['Cost by Category']['Service Failure']['cost per year']))
    print('    Health Benefits')
    print('         Health Benefits costs per vkm                             : {:6.2f} €-ct/vkm'.format(external_costs_results_1_time_pref_shared_pedelec['Cost by Category']['Health Benefits']['cost per vkm']))
    print('         Health Benefits  costs per pkm                            : {:6.2f} €-ct/pkm'.format(external_costs_results_1_time_pref_shared_pedelec['Cost by Category']['Health Benefits']['cost per pkm']))
    print('         Health Benefits costs per year                            : {:6.2f} €/year'.format(external_costs_results_1_time_pref_shared_pedelec['Cost by Category']['Health Benefits']['cost per year']))
    print('TOTAL EXTERNAL COSTS PEDELEC')
    print('    Total cost per vkm                                             : {:6.2f} €-ct/vkm'.format(external_costs_results_1_time_pref_shared_pedelec['Total Cost']['total cost per vkm']))
    print('    Total cost per pkm                                             : {:6.2f} €-ct/pkm'.format(external_costs_results_1_time_pref_shared_pedelec['Total Cost']['total cost per pkm']))
    print('    Total cost per year                                            : {:6.2f} €/year'.format(external_costs_results_1_time_pref_shared_pedelec['Total Cost']['total cost per year']))
