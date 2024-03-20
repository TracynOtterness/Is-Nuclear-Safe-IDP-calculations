US_TWh_2022 = 4048 # https://www.statista.com/statistics/201794/us-electricity-consumption-since-1975/


coal_deaths_per_TWh = 24.6 # https://ourworldindata.org/safest-sources-of-energy
natural_gas_deaths_per_TWh = 2.8 # https://ourworldindata.org/safest-sources-of-energy
nuclear_deaths_per_TWh = 0.03 # https://ourworldindata.org/safest-sources-of-energy
solar_deaths_per_TWh = 0.02 # https://ourworldindata.org/safest-sources-of-energy
wind_deaths_per_TWh = 0.04 # https://ourworldindata.org/safest-sources-of-energy
hydro_deaths_per_TWh = 1.3 # https://ourworldindata.org/safest-sources-of-energy

# calculate the deaths produced by each energy source
coal_total_deaths = US_TWh_2022 * coal_deaths_per_TWh
natural_gas_total_deaths = US_TWh_2022 * natural_gas_deaths_per_TWh
nuclear_total_deaths = US_TWh_2022 * nuclear_deaths_per_TWh
solar_total_deaths = US_TWh_2022 * solar_deaths_per_TWh
wind_total_deaths = US_TWh_2022 * wind_deaths_per_TWh
hydro_total_deaths = US_TWh_2022 * hydro_deaths_per_TWh

print("The deaths produced by each energy source is:")
print(coal_total_deaths, "deaths from coal")
print(natural_gas_total_deaths, "deaths from natural gas")
print(nuclear_total_deaths, "deaths from nuclear")
print(solar_total_deaths, "deaths from solar")
print(wind_total_deaths, "deaths from wind")
print(hydro_total_deaths, "deaths from hydro")
print("-------------------")

# print out as proportion of total deaths in 2022
total_deaths = coal_total_deaths + natural_gas_total_deaths + nuclear_total_deaths + solar_total_deaths + wind_total_deaths + hydro_total_deaths
print("The proportion of", total_deaths," deaths produced by each energy source is:")
print(coal_total_deaths / total_deaths, "deaths from coal")
print(natural_gas_total_deaths / total_deaths, "deaths from natural gas")
print(nuclear_total_deaths / total_deaths, "deaths from nuclear")
print(solar_total_deaths / total_deaths, "deaths from solar")
print(wind_total_deaths / total_deaths, "deaths from wind")
print(hydro_total_deaths / total_deaths, "deaths from hydro")

#print out the total deaths from green energy sources
total_green_deaths = solar_total_deaths + wind_total_deaths + hydro_total_deaths + nuclear_total_deaths
print("The total deaths from green energy sources is: ", total_green_deaths)
print("The proportion of nuclear deaths among green deaths is: ", nuclear_total_deaths / total_green_deaths)
print("The proportion of solar deaths among green deaths is: ", solar_total_deaths / total_green_deaths)
print("The proportion of wind deaths among green deaths is: ", wind_total_deaths / total_green_deaths)
print("The proportion of hydro deaths among green deaths is: ", hydro_total_deaths / total_green_deaths)
print("-------------------")

person = 281 # 1/20th of all green deaths so we display 20 people
print("fossil fuels kill this many \"people icons\" worth of people every year")
print(coal_total_deaths / person, "people from coal")
print(natural_gas_total_deaths / person, "people from natural gas")


