import xarray

import matplotlib.pyplot as plt
import matplotlib as mpl

ds = xarray.open_dataset("../data/HadCRUT.5.0.0.0_analysis_summary-series_global_monthly.nc")

fig, axs = plt.subplots(1, 1, figsize=(10,6), layout='constrained')

N_years = ds.time.size / 12

alpha = 0.001
delta_alpha = (1.0 - alpha)/N_years

year_group = ds.groupby("time.year")

years = [ year for year, _ in year_group]

first_year = years[0]
last_year = years[-1]

delta_years = last_year - first_year

cmap = mpl.colormaps['rainbow']

for year, year_data in year_group:
    alpha += delta_alpha
    yearly_mean = year_data['tas_mean'].mean()
    axs.plot(year_data.time.dt.strftime("%b"), year_data['tas_mean'], 
             label=year, color=cmap((year - first_year)/delta_years), alpha=alpha)


axs.set_ylabel("Temperature Anomalies Compared to 1961-1990, \N{DEGREE SIGN}C")
axs.set_xlabel("Month")    

colorizer = mpl.colorizer.Colorizer(norm=mpl.colors.Normalize(first_year, last_year), cmap='rainbow')
fig.colorbar(mpl.colorizer.ColorizingArtist(colorizer), ax=axs)

plt.show()
