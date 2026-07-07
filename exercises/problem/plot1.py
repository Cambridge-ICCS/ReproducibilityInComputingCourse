import xarray
import matplotlib.pyplot as plt

# Recreate the "warming stripes" visualisation
# https://showyourstripes.info/

ds = xarray.open_dataset("../data/HadCRUT.5.0.0.0_analysis_summary-series_global_annual.nc")

fig, axs = plt.subplots(2, 1, figsize=(10,6), layout='constrained')

x = ds['time'].data

y_lower = ds['tas_lower'].data
y = ds['tas_mean'].data
y_upper = ds['tas_upper'].data

axs[0].pcolor(y.reshape(1, -1), cmap="coolwarm")
axs[0].axis('off')

axs[1].errorbar(x, y, yerr=[y - y_lower, y_upper - y])
axs[1].set_ylabel("Annual Temperature Anomalies Compared to 1961-1990, \N{DEGREE SIGN}C")
axs[1].set_xlabel("Year")

plt.show()
