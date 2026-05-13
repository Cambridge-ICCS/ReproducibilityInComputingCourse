import xarray
import matplotlib.pyplot as plt

ds = xarray.open_dataset("../data/CARS2009_temp20-40S_69-88W.nc")

ds['temp'].plot()
plt.show()
