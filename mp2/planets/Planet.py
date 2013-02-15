# Planet Class
# Brian T. Bailey

class Planet:
  """A Class object that models a Planet from the Solar System
  
  Attributes:
      name: A String representing the Planet name
      mass: A floating point value representing the Planet's mass in kg
      diameter: A floating point value representing the Planet's diameter in km
      escapeVelocity: A floating point value representing the Planet's escape
        velocity in m/s
      revolutionPeriod: A floating point value representing the Planet's 
        revolution period in Earth Days
      meanSurfaceTemp: A floating point value representing the Planet's mean
        surface temperature in K
  """
  
  def __init__(self, name, mass, diameter, escapeVelocity, revolutionPeriod, 
               meanSurfaceTemp):
    self.name = name
    self.mass = mass
    self.diameter = diameter
    self.escapeVelocity = escapeVelocity
    self.revolutionPeriod = revolutionPeriod
    self.meanSurfaceTemp = meanSurfaceTemp

  # String Method
  def __str__(self):
    return "Planet %s" % (self.name)

  # repr Method
  def __repr__(self):
    return "<%s Planet Instance at %s>" % (self.name, hex(id(self)))

  # Display Attributes Method
  def display(self):
    print("-" * 35)
    print("Planet: %s" % (self.name))
    print("-" * 35)
    print("Mass: %s kg" % (self.mass))
    print("Diameter: %s km" % (self.diameter))
    print("Escape Velocity: %s m/s" % (self.escapeVelocity))
    print("Revolution Period: %s Earth Days" % (self.revolutionPeriod))
    print("Mean Surface Temperature: %s K" % (self.meanSurfaceTemp))

  # Getters and Setters
  def setName(self, name):
    self.name = name

  def getName(self):
    return self.name

  def setMass(self, mass):
    self.mass = mass

  def getMass(self):
    return self.mass

  def setDiameter(self, diameter):
    self.diameter = diameter

  def getDiameter(self):
    return self.diameter

  def setEscapeVelocity(self, escapeVelocity):
    self.escapeVelocity = escapeVelocity

  def getEscapeVelocity(self):
    return self.escapeVelocity

  def setRevolutionPeriod(self, revolutionPeriod):
    self.revolutionPeriod = revolutionPeriod

  def getRevolutionPeriod(self):
    return self.revolutionPeriod

  def setMeanSurfaceTemp(self, meanSurfaceTemp):
    self.meanSurfaceTemp = meanSurfaceTemp

  def getMeanSurfaceTemp(self):
    return self.meanSurfaceTemp


# Test Code
if __name__ == '__main__':
  aPlanet = Planet("Earth", 5.98e24, 12756, 11200, 365.26, 281)
  aPlanet.display()