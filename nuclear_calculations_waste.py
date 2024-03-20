import math

US_TWh_2022 = 4048 # https://www.statista.com/statistics/201794/us-electricity-consumption-since-1975/

# https://www.sustainabilitybynumbers.com/p/renewables-waste#footnote-3-138994586
solar_kg_per_MWh = 1.67 
wind_kg_per_MWh = 0.16
nuclear_kg_per_MWh = 0.031
coal_kg_per_MWh = 84

# Calculate the waste in kg produced if powering the entire US with each energy source
Solar_waste_kg = US_TWh_2022 * 1e6 * solar_kg_per_MWh
Wind_waste_kg = US_TWh_2022 * 1e6 * wind_kg_per_MWh
Nuclear_waste_kg = US_TWh_2022 * 1e6 * nuclear_kg_per_MWh
Coal_waste_kg = US_TWh_2022 * 1e6 * coal_kg_per_MWh

# densities of the waste
nuclear_density_kg_per_cubic_m = 19000 # kg/m^3 (based on spent uranium density according to NIH) https://pubmed.ncbi.nlm.nih.gov/11218253/
# https://a1solarstore.com/panasonic-400w-solar-panel-132-cell-evp132gl.html
# 400 W panel (used for waste estimate) is 71.7 inches x 40 inches x 1.2 inches
# 1 inch = 0.0254 meters so thats 1.82 m x 1.02 m x 0.03 m or 0.055 m^3
# it is listed at 45 lbs or 20.4 kg
# so the density is 20.4 kg / 0.055 m^3 = 372.73 kg/m^3
solar_density_kg_per_cubic_m = 372.73 # kg/m^3

# https://www.iberdrola.com/sustainability/wind-turbines-blades
# Most modern wind turbines are made out of fiberglass-renforced polyester or epoxy
# https://www.matweb.com/search/datasheet.aspx?matguid=065c3e17d9f04496a9eb51dedb9fb3bb
# density is ~1.85 g/cm which is 1850 kg/m^3
wind_desnity_kg_per_cubic_m = 1850 # kg/m^3

# https://iopscience.iop.org/article/10.1088/1742-6596/1732/1/012127/pdf
# coal ash density is between 1.9 and 2.9. Let's call it 2.4 g/cm^3 or 2400 kg/m^3
coal_density_kg_per_cubic_m = 2400 # kg/m^3

# calculate the volume of waste produced by each energy source
Solar_waste_cubic_m = Solar_waste_kg / solar_density_kg_per_cubic_m
Wind_waste_cubic_m = Wind_waste_kg / wind_desnity_kg_per_cubic_m
Nuclear_waste_cubic_m = Nuclear_waste_kg / nuclear_density_kg_per_cubic_m
Coal_waste_cubic_m = Coal_waste_kg / coal_density_kg_per_cubic_m

print("The volume of waste produced by each energy source is:")
print(Solar_waste_cubic_m, "cubic meters of solar waste")
print(Wind_waste_cubic_m, "cubic meters of wind waste")
print(Nuclear_waste_cubic_m, "cubic meters of nuclear waste")
print(Coal_waste_cubic_m, "cubic meters of coal waste")
print("-------------------")

# convert to square miles at 1m deep
square_meters_to_square_miles = 3.861e-7
Solar_miles_squared_needed = Solar_waste_cubic_m * square_meters_to_square_miles
Wind_miles_squared_needed = Wind_waste_cubic_m * square_meters_to_square_miles
Nuclear_miles_squared_needed = Nuclear_waste_cubic_m * square_meters_to_square_miles
Coal_miles_squared_needed = Coal_waste_cubic_m * square_meters_to_square_miles

print("The square miles of waste produced at a depth of 1m is:")
print(Solar_miles_squared_needed, "square miles of solar waste")
print(Wind_miles_squared_needed, "square miles of wind waste")
print(Nuclear_miles_squared_needed, "square miles of nuclear waste")
print(Coal_miles_squared_needed, "square miles of coal waste")
print("-------------------")

# convert to football fields at 1m deep 
football_field_area_m_squared = 5350 # https://www.dimensions.com/collection/football-soccer

Solar_football_fields = Solar_waste_cubic_m / football_field_area_m_squared
Wind_football_fields = Wind_waste_cubic_m / football_field_area_m_squared
Nuclear_football_fields = Nuclear_waste_cubic_m / football_field_area_m_squared
Coal_football_fields = Coal_waste_cubic_m / football_field_area_m_squared

print("The volume of waste produced by each energy source is:")
print(Solar_football_fields, "football fields of solar waste")
print(Wind_football_fields, "football fields of wind waste")
print(Nuclear_football_fields, "football fields of nuclear waste")
print(Coal_football_fields, "football fields of coal waste")
print("-------------------")

# 6,604 square meters (m²):
#     About 1.5 acres. A standard football (soccer) field is roughly 7,140 m², so this area is just under the size of a football pitch.
#     Comparable to the footprint of a large supermarket or a small shopping center.

# 350,097 square meters (m²):
#     This is about 86.5 acres. It's roughly equivalent to the base area of the Great Pyramid of Giza (approximately 5.3 hectares or 53,000 m²) multiplied by about 6.6.
#     Similar in size to 50 soccer fields.

# 18,136,881 square meters (m²):
#     This is approximately 4,484 acres or about 7 square miles.
#     It's roughly equivalent to the size of a small town or the island of Manhattan in New York City, which is about 59 km² (though the shape of Manhattan is long and narrow, so the comparison is very approximate in terms of total area).

# 141,680,000 square meters (m²):
#     This area is about 35,000 acres, or about 55 square miles (142.4 km²).
#     It's comparable to the size of Washington, D.C., which is about 68 square miles (176 km²), giving a rough idea of the magnitude.
#     Another comparison is the city of San Francisco, which is about 121 km². This area is somewhat larger, indicating a scale larger than San Francisco but smaller than some major cities.