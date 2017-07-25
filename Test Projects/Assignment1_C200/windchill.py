#Fahrenheit to Celsius conversion

#import Math module
import math

#ask user for input
TempF = int(input("Enter temperature in Fahrenheit: "))
Velocity = int(input("Enter windspeed in mph: "))

#Calculate temperature in Celsius
TempC = 34.74 + (0.6215 * TempF) - (35.75 * (Velocity ** 0.16)) + (0.4275 * (Velocity ** 0.16))

print("Temperature in Celsius is " + str(TempC))
