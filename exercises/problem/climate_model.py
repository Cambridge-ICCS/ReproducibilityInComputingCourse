solar_constant = 1370
sigma = 5.67e-8 # Stefan-Boltzmann constant

def absorbed_solar_radiation(albedo):
    return solar_constant*(1-albedo)/4

def emitted_radiation(emissivity, temperature):
    return emissivity * sigma * temperature**4

def energy_balanced_temperature(emissivity, albedo):
    # dT/dt = 0 => in = out
    return (solar_constant*(1-albedo)/(4*emissivity * sigma))**0.25

def emissivity_given_temp(albedo, temperature):
    return solar_constant*(1-albedo)/(4*sigma*temperature**4)
