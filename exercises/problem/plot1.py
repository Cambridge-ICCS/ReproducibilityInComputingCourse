import xarray
import matplotlib.pyplot as plt

ds = xarray.open_dataset("../data/HadCRUT.5.0.0.0_analysis_summary-series_180E-0N-180W-30N_annual.nc")

plt.fill_between(ds['time'].data, ds['tas_lower'].data, ds['tas_upper'])
plt.show()
