import math

US_TWh_2022 = 4048 # https://www.statista.com/statistics/201794/us-electricity-generation-by-energy-source/
US_population_2022 = 331000000 # https://www.census.gov/popclock/
MWh_per_person_per_year = US_TWh_2022 * 1e6 / US_population_2022
Austin_metro_population = 2295303 # https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population
Austin_population = 978908 # https://en.wikipedia.org/wiki/Austin,_Texas
Austin_square_miles = 319 # https://en.wikipedia.org/wiki/Austin,_Texas
Austin_metro_square_miles = 4285.70 # https://en.wikipedia.org/wiki/Austin,_Texas
TWh_for_Austin = US_TWh_2022 #Austin_metro_population * MWh_per_person_per_year / 1e6

print("The US energy consumption in 2022 is", US_TWh_2022, "TWh and the population is", US_population_2022)
print("The energy consumption per person per year is", MWh_per_person_per_year, "MWh")
print("In 2020, Austin had a population of ", Austin_metro_population)
print("The energy consumption for a large city in 2022 is", TWh_for_Austin, "TWh")

# https://ourworldindata.org/land-use-per-energy-source
Coal_square_meters_per_MWh = (21+15)/2 # take average of different types 
Natural_gas_square_meters_per_MWh = (1+1.3)/2 # take average of different types
Nuclear_square_meters_per_MWh = 0.3
Solar_square_meters_per_MWh = (22+19+12.6+3+1.2)/5 # take average of different types
Wind_square_meters_per_MWh = 51.7 # generously use Quartile 1 value, since farms in Q1 are more likely to be main-use wind farms
Hydro_square_meters_per_MWh = (14+33)/2 # take average of different types

#calculate the square meters needed for each energy source to produce entire US energy consumption in 2022
Coal_square_meters_needed = TWh_for_Austin * 1e6 * Coal_square_meters_per_MWh
Natural_gas_square_meters_needed = TWh_for_Austin * 1e6 * Natural_gas_square_meters_per_MWh
Nuclear_square_meters_needed = TWh_for_Austin * 1e6 * Nuclear_square_meters_per_MWh
Solar_square_meters_needed = TWh_for_Austin * 1e6 * Solar_square_meters_per_MWh
Wind_square_meters_needed = TWh_for_Austin * 1e6 * Wind_square_meters_per_MWh
Hydro_square_meters_needed = TWh_for_Austin * 1e6 * Hydro_square_meters_per_MWh

print("To produce the entire US energy consumption in 2022, we would need:")
print(Coal_square_meters_needed, "square meters of coal plants")
print(Natural_gas_square_meters_needed, "square meters of natural gas plants")
print(Nuclear_square_meters_needed, "square meters of nuclear plants")
print(Solar_square_meters_needed, "square meters of solar plants")
print(Wind_square_meters_needed, "square meters of wind plants")
print(Hydro_square_meters_needed, "square meters of hydro plants")
print("-------------------")

#convert square meters to square miles
square_meters_to_square_miles = 3.861e-7
Coal_miles_squared_needed = Coal_square_meters_needed * square_meters_to_square_miles
Natural_gas_miles_squared_needed = Natural_gas_square_meters_needed * square_meters_to_square_miles
Nuclear_miles_squared_needed = Nuclear_square_meters_needed * square_meters_to_square_miles
Solar_miles_squared_needed = Solar_square_meters_needed * square_meters_to_square_miles
Wind_miles_squared_needed = Wind_square_meters_needed * square_meters_to_square_miles
Hydro_miles_squared_needed = Hydro_square_meters_needed * square_meters_to_square_miles

print("To produce the entire US energy consumption in 2022, we would need:")
print(Coal_miles_squared_needed, "square miles of coal plants")
print(Natural_gas_miles_squared_needed, "square miles of natural gas plants")
print(Nuclear_miles_squared_needed, "square miles of nuclear plants")
print(Solar_miles_squared_needed, "square miles of solar plants")
print(Wind_miles_squared_needed, "square miles of wind plants")
print(Hydro_miles_squared_needed, "square miles of hydro plants")
print("-------------------")


#Notes for image creation
Utah_southern_border_length_miles = 270 # https://en.wikipedia.org/wiki/Utah
Utah_southern_border_length_pixels = 1350 # Measuring in photoshop
miles_to_pixels = Utah_southern_border_length_pixels / Utah_southern_border_length_miles
pixels_to_miles = 1 / miles_to_pixels
print("1 mile = ", miles_to_pixels, "pixels")
print("1 pixel = ", pixels_to_miles, "miles")

alligator_river_nwr_miles = 237.5 #https://en.wikipedia.org/wiki/Alligator_River_National_Wildlife_Refuge

print("100 miles is ", 100 * miles_to_pixels, "pixels")
print("500 miles is ", 500 * miles_to_pixels, "pixels")
print("1000 miles is ", 1000 * miles_to_pixels, "pixels")
print("-------------------")

#compute the radius of a circle in miles with the same area as the square miles needed for each energy source
Coal_radius_miles = math.sqrt(Coal_miles_squared_needed / math.pi)
Natural_gas_radius_miles = math.sqrt(Natural_gas_miles_squared_needed / math.pi)
Nuclear_radius_miles = math.sqrt(Nuclear_miles_squared_needed / math.pi)
Solar_radius_miles = math.sqrt(Solar_miles_squared_needed / math.pi)
Wind_radius_miles = math.sqrt(Wind_miles_squared_needed / math.pi)
Hydro_radius_miles = math.sqrt(Hydro_miles_squared_needed / math.pi)
aligator_radius_miles = math.sqrt(alligator_river_nwr_miles / math.pi)


print("The circle with the same area as the square miles needed for each energy source has a radius of:")
print(Coal_radius_miles, "miles for coal")
print(Natural_gas_radius_miles, "miles for natural gas")
print(Nuclear_radius_miles, "miles for nuclear")
print(Solar_radius_miles, "miles for solar")
print(Wind_radius_miles, "miles for wind")
print(Hydro_radius_miles, "miles for hydro")
print(aligator_radius_miles, "miles for Alligator River NWR")

#compute in pixels
Coal_radius_pixels = Coal_radius_miles * miles_to_pixels
Natural_gas_radius_pixels = Natural_gas_radius_miles * miles_to_pixels
Nuclear_radius_pixels = Nuclear_radius_miles * miles_to_pixels
Solar_radius_pixels = Solar_radius_miles * miles_to_pixels
Wind_radius_pixels = Wind_radius_miles * miles_to_pixels
Hydro_radius_pixels = Hydro_radius_miles * miles_to_pixels
alligator_radius_pixels = aligator_radius_miles * miles_to_pixels

print("The circle with the same area as the square miles needed for each energy source has a radius of:")
print(Coal_radius_pixels, "pixels for coal")
print(Natural_gas_radius_pixels, "pixels for natural gas")
print(Nuclear_radius_pixels, "pixels for nuclear")
print(Solar_radius_pixels, "pixels for solar")
print(Wind_radius_pixels, "pixels for wind")
print(Hydro_radius_pixels, "pixels for hydro")
print(alligator_radius_pixels, "pixels for Alligator River NWR")
print("-------------------")

#print the diameter of each circle in pixels
print("The circle with the same area as the square miles needed for each energy source has a diameter of:")
print(Coal_radius_pixels*2, "pixels for coal")
print(Natural_gas_radius_pixels*2, "pixels for natural gas")
print(Nuclear_radius_pixels*2, "pixels for nuclear")
print(Solar_radius_pixels*2, "pixels for solar")
print(Wind_radius_pixels*2, "pixels for wind")
print(Hydro_radius_pixels*2, "pixels for hydro")
print(alligator_radius_pixels*2, "pixels for Alligator River NWR")
print("-------------------")

#Print how many times more area is used by each energy source compared to nuclear
print("The area used by each energy source compared to nuclear is:")
print(Coal_miles_squared_needed / Nuclear_miles_squared_needed, "times more for coal")
print(Natural_gas_miles_squared_needed / Nuclear_miles_squared_needed, "times more for natural gas")
print(Solar_miles_squared_needed / Nuclear_miles_squared_needed, "times more for solar")
print(Wind_miles_squared_needed / Nuclear_miles_squared_needed, "times more for wind")
print(Hydro_miles_squared_needed / Nuclear_miles_squared_needed, "times more for hydro")
print("-------------------")

#Things to potentially put together 
# - 1. land footprint (compare with renewables) (circles on map)
# - 2. capacity factor (compare with renewables, categorical)
# - 4. waste (compare with both renewables and fossil fuels) (circles on map)

# - 3. emissions (compare w/ fossil fuels, categorical)
# - 5. danger to human life (compare w/ fossil fuels)

