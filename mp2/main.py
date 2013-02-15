# MP2 - Driver
# Brian T. Bailey

import planets.planet_utils

# Parse Planet Data Files into Planet Objects, Store in SolarSystem Dictionary
datalist = ['data/mercury.txt', 'data/venus.txt', 'data/earth.txt', 
            'data/mars.txt', 'data/jupiter.txt', 'data/saturn.txt', 
            'data/uranus.txt', 'data/neptune.txt', 'data/pluto.txt']
# Create SolarSystem Dictionary with a Dictionary Comprehension using an
# nested List Comprehension to parse the data into a Planet Object List
SolarSystem = {j.name : j for j in [planets.planet_utils.parsePlanetDatafile(i) 
               for i in datalist]}


# Sort Planets by Each Data Field in Ascending Order
# Store the resulting Planet Names in Lists
sortedByMass = [x.name for x in sorted(SolarSystem.values(), 
                key=lambda p: p.mass)]
sortedByDiameter = [x.name for x in sorted(SolarSystem.values(), 
                    key=lambda p: p.diameter)]
sortedByEscapeVelocity = [x.name for x in sorted(SolarSystem.values(), 
                          key=lambda p: p.escapeVelocity)]
sortedByRevolutionPeriod = [x.name for x in sorted(SolarSystem.values(), 
                            key=lambda p: p.revolutionPeriod)]
sortedByMeanTemperature = [x.name for x in sorted(SolarSystem.values(), 
                           key=lambda p: p.meanSurfaceTemp)]


# Write Results to file and display Results to Screen
outfile = open('data/mp2out.txt', 'w')

# Output Header
print('ITM 513 - MP2')
outfile.write('ITM 513 - MP2\n')
print('Brian T. Bailey\n')
outfile.write('Brian T. Bailey\n\n')

# Output Planet Object Data Attributes
print("Planet Attributes")
outfile.write("Planet Attributes\n")
for planet in SolarSystem.values():
  planets.planet_utils.outputPlanetAttributes(outfile, planet)

# Output Sorted Planet Names Based on Ascending Data Attributes
planets.planet_utils.outputNewline(outfile)
print("Planet Names Sorted by Attribute")
outfile.write("Planet Names Sorted by Attribute\n")
planets.planet_utils.outputSortedHeader(outfile, "Planets Sorted " +
                                        "By Mass (Ascending)")
planets.planet_utils.outputSortedList(outfile, sortedByMass)
planets.planet_utils.outputSortedHeader(outfile, "Planets Sorted " +
                                        "By Diameter (Ascending)")
planets.planet_utils.outputSortedList(outfile, sortedByDiameter)
planets.planet_utils.outputSortedHeader(outfile, "Planets Sorted " +
                                        "By Escape Velocity (Ascending)")
planets.planet_utils.outputSortedList(outfile, sortedByEscapeVelocity)
planets.planet_utils.outputSortedHeader(outfile, "Planets Sorted " +
                                        "By Revolution Period (Ascending)")
planets.planet_utils.outputSortedList(outfile, sortedByRevolutionPeriod)
planets.planet_utils.outputSortedHeader(outfile, "Planets Sorted " +
                                        "By Mean Surface Temp (Ascending)")
planets.planet_utils.outputSortedList(outfile, sortedByMeanTemperature)

# Output the SolarSystem Dictionary Hash
planets.planet_utils.outputNewline(outfile)
print("SolarSystem Dictionary Hash")
print(("-" * 35))
outfile.write("SolarSystem Dictionary Hash\n")
outfile.write(("-" * 35) + "\n")
print(SolarSystem)
outfile.write(str(SolarSystem))
planets.planet_utils.outputNewline(outfile)

# Close File
outfile.close()
