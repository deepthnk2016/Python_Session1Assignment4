#-----------------------------------------------------------------
# Python - Session 1 Assignment 4
# Descr  - Python program to calculate volume of Sphere having
#          diameter 12
#-----------------------------------------------------------------

# Set diameter to 12
diameter = 12

# Calculate radius
radius = diameter / 2

# Set the value of pi
pi = 3.14

# Calculate and print volume
volume = (4 / 3) * pi * radius * radius * radius
print("Volume of Sphere with diameter %.0f is %.2f" %(diameter,volume))