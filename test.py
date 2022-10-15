import math
from cmath import pi

absoluteDistance = 10000
altitude = "20.000000°"
altitude = altitude[0:-1]
altitude = math.radians(float(altitude))
cloudheight = math.tan(altitude)*absoluteDistance
print(cloudheight)