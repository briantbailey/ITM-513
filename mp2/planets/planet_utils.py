# Planet Class Utilities Module
# Brian T. Bailey

from Planet import Planet

def parsePlanetDatafile(dataPath):
  """Returns a Planet Object
  
  Takes Planet Data File Path as Argument
  Planet Data File is a csv file with first line as field names
  """
  data = []
  # Loop through file line by line, separate at ',', strip whitespace, 
  # append resulting list to data list object
  for line in open(dataPath):
    data.append([x.strip() for x in line.split(',')])
  
  # Create and return Planet Object using second list in data list as arguments
  aPlanet = Planet(data[1][0], float(data[1][1]), float(data[1][2]), 
                   float(data[1][3]), float(data[1][4]), float(data[1][5]))
  return aPlanet

def outputPlanetAttributes(file, planet):
  """Outputs the Attributes of a Planet Object to the Console and a File
  
  First Argument is the file object to write the data to and the second
  Argument is the Planet object whose attributes we want to output.
  """
  planet.display()
  print('')
  file.write(("-" * 35) + "\n")
  file.write("Planet: %s\n" % (planet.name))
  file.write(("-" * 35) + "\n")
  file.write("Mass: %s kg\n" % (planet.mass))
  file.write("Diameter: %s km\n" % (planet.diameter))
  file.write("Escape Velocity: %s m/s\n" % (planet.escapeVelocity))
  file.write("Revolution Period: %s Earth Days\n" % (planet.revolutionPeriod))
  file.write("Mean Surface Temperature: %s K\n" % (planet.meanSurfaceTemp))
  file.write('\n')

def outputSortedList(file, list):
  """Outputs a List one item per line to both the Console and a File
  
  First Argument is the file object to write the List to and the second
  Argument is the List.
  """
  for x in list:
    print(x)
    file.write(x + '\n')
  print('')
  file.write('\n')
    
def outputSortedHeader(file, string):
  """Outputs a formated Header for the Sorted Planet Lists to
  both the Console and a File
  
  First Argument is the file object to write the Header to and the second
  Argument is the String for the text of the Header.
  """
  print("-" * 35)
  print(string)
  print("-" * 35)
  file.write(("-" * 35) + "\n")
  file.write(string + '\n')
  file.write(("-" * 35) + "\n")

def outputNewline(file):
  """Outputs a Newline Character to both the Console and a File
  
  Argument is a writeable file object that you want the newline character
  output to.
  """
  print('')
  file.write('\n')


# Test Code
if __name__ == '__main__':
  aPlanet = parsePlanetDatafile('../data/earth.txt')
  aPlanet.display()