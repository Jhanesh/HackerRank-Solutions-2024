import os
import sys

class Car:
    def __init__(self, max_speed, unit):
        self.max_speed = max_speed
        self.unit = unit

    def __str__(self):
        return "Car with the maximum speed of {0} {1}".format(self.max_speed, self.unit)

class Boat:
    def __init__(self, max_speed):
        self.max_speed = max_speed

    def __str__(self):
        return "Boat with the maximum speed of {0} knots".format(self.max_speed)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    # Read all input at once from standard input
    input_data = sys.stdin.read().strip().splitlines()
    
    # The first line contains the number of queries
    q = int(input_data[0])  # Assume the first line is the integer number of queries

    for i in range(1, q + 1):  # Iterate over the subsequent lines
        args = input_data[i].split()  # Split each line by spaces
        vehicle_type = args[0]

        if vehicle_type == "car":
            max_speed = int(args[1])
            speed_unit = args[2]  # The unit can include characters like "km/h"
            vehicle = Car(max_speed, speed_unit)
        elif vehicle_type == "boat":
            max_speed = int(args[1])
            vehicle = Boat(max_speed)
        else:
            raise ValueError("Invalid vehicle type")
        
        fptr.write("%s\n" % vehicle)  # Write the vehicle string to output
    
    fptr.close()
