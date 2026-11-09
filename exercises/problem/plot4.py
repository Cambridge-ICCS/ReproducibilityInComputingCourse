import climate_model

import xarray
import matplotlib.pyplot as plt

global_ds = xarray.open_dataset("../data/HadCRUT.5.0.0.0_analysis_summary-series_global_annual.nc")

fig, axs = plt.subplots(1, 1, figsize=(10,6), layout='constrained')

# Absolute mean temperature between 1961 and 1990
# https://crudata.uea.ac.uk/cru/data/temperature/abs_glnhsh.txt
absolute_value = 13.974 + 273.15
time = global_ds['time'].data
temperature = global_ds['tas_mean'].data + absolute_value
albedo = 0.3

epsilon = climate_model.emissivity_given_temp(albedo, temperature)

axs.plot(time, epsilon)

axs.set_xlabel("Year")
axs.set_ylabel("Effective emissivity of Earth")

plt.show()

