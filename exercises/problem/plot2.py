import xarray
import matplotlib.pyplot as plt

global_ds = xarray.open_dataset("../data/HadCRUT.5.0.0.0_analysis_summary-series_global_annual.nc")
northern_ds = xarray.open_dataset("../data/HadCRUT.5.0.0.0_analysis_summary-series_northern-hemisphere_annual.nc")
southern_ds = xarray.open_dataset("../data/HadCRUT.5.0.0.0_analysis_summary-series_southern-hemisphere_annual.nc")

def plot_temp_with_error(ax, ds, label):
    axs.fill_between(ds['time'].data, ds['tas_lower'].data, ds['tas_upper'].data,
                     color="grey", alpha=0.3, edgecolor=None)
    axs.plot(ds['time'].data, ds['tas_mean'].data)


fig, axs = plt.subplots(1, 1, figsize=(10,6), layout='constrained')

plot_temp_with_error(axs, global_ds, label="global")
plot_temp_with_error(axs, northern_ds, label="northern")
plot_temp_with_error(axs, southern_ds, label="southern")

t_min = global_ds['time'].min()
t_max = global_ds['time'].max()

axs.hlines(0.0, t_min, t_max, color="black", linestyle="--")

axs.set_xlabel("Year")
axs.set_ylabel("Annual Temperature Anomalies Compared to 1961-1990, \N{DEGREE SIGN}C")

plt.show()
