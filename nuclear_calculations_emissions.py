
US_TWh_2022 = 4048 # https://www.statista.com/statistics/201794/us-electricity-consumption-since-1975/

# https://ourworldindata.org/safest-sources-of-energy
coal_Tonnes_CO2_per_TWh = 820 * 1000
natural_gas_Tonnes_CO2_per_TWh = 490 * 1000
nuclear_Tonnes_CO2_per_TWh = 3 * 1000
solar_Tonnes_CO2_per_TWh = 5 * 1000
wind_Tonnes_CO2_per_TWh = 4 * 1000
hydro_Tonnes_CO2_per_TWh = 34 * 1000

# calculate the CO2 produced by each energy source
coal_total_tonnes_CO2 = US_TWh_2022 * coal_Tonnes_CO2_per_TWh
natural_gas_total_tonnes_CO2 = US_TWh_2022 * natural_gas_Tonnes_CO2_per_TWh
nuclear_total_tonnes_CO2 = US_TWh_2022 * nuclear_Tonnes_CO2_per_TWh
solar_total_tonnes_CO2 = US_TWh_2022 * solar_Tonnes_CO2_per_TWh
wind_total_tonnes_CO2 = US_TWh_2022 * wind_Tonnes_CO2_per_TWh
hydro_total_tonnes_CO2 = US_TWh_2022 * hydro_Tonnes_CO2_per_TWh

print("The CO2 produced by each energy source is:")
print(coal_total_tonnes_CO2, "tonnes of CO2 from coal")
print(natural_gas_total_tonnes_CO2, "tonnes of CO2 from natural gas")
print(nuclear_total_tonnes_CO2, "tonnes of CO2 from nuclear")
print(solar_total_tonnes_CO2, "tonnes of CO2 from solar")
print(wind_total_tonnes_CO2, "tonnes of CO2 from wind")
print(hydro_total_tonnes_CO2, "tonnes of CO2 from hydro")
print("-------------------")

# print out same data in mega tonnes
print("The CO2 produced by each energy source is:")
print(coal_total_tonnes_CO2 / 1e6, "mega tonnes of CO2 from coal")
print(natural_gas_total_tonnes_CO2 / 1e6, "mega tonnes of CO2 from natural gas")
print(nuclear_total_tonnes_CO2 / 1e6, "mega tonnes of CO2 from nuclear")
print(solar_total_tonnes_CO2 / 1e6, "mega tonnes of CO2 from solar")
print(wind_total_tonnes_CO2 / 1e6, "mega tonnes of CO2 from wind")
print(hydro_total_tonnes_CO2 / 1e6, "mega tonnes of CO2 from hydro")
print("-------------------")