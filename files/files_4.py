
##############################
# Files
##############################

from math import *
import os


##############################
# Activity 4 - Distances between to town
##############################

from math import *

## Question 1 ##

def distance_xy(x1,y1,x2,y2):
    return sqrt( (x2-x1)**2 + (y2-y1)**2 )

## Question 2 ##

def file_distances_xy(filename):
    # Input file
    fi_in = open(filename,"r")

    list_cities = []

    for line in fi_in:
        list_cities = list_cities + [line.split()]
        
    # Close input file
    fi_in.close()

    # Files à écrire
    name, extension = os.path.splitext(filename)
    new_name = name + "_distances" + ".txt"
    fi_out = open(new_name,"w")

    line = '{:>10s}'.format("")
    for c in list_cities: 
        name = c[0]
        line = line + '{:>10s}'.format(name) +" "

    fi_out.write(line + "\n")

    for c1 in list_cities:
        name1 = c1[0]
        x1 = float(c1[1])
        y1 = float(c1[2])

        line = '{:10s}'.format(name1)

        for c2 in list_cities:
            name2 = c2[0]
            x2 = float(c2[1])
            y2 = float(c2[2])

            d = distance_xy(x1,y1,x2,y2)

            line = line + '{:10d}'.format(round(d)) + " "

        fi_out.write(line + "\n")

    return

print("--- Cities xy ---")
file_distances_xy("cities_xy.txt")


## Question 3 ##

def degrees_to_radians(a):
    return 2*pi*a/360

def distance_approx_lat_long(lat1,long1,lat2,long2):
    R = 6371  # radius (average) of Earth in km
    x = (long2-long1)*cos( (lat1+lat2)/2 )
    y = lat2-lat1
    d = R * sqrt( x**2 + y**2 )
    return d

# Test 
Paris = (48.853,2.350)  # (lat,long) in degrees
Paris_radians = (degrees_to_radians(Paris[0]),degrees_to_radians(Paris[1]))

New_York = (40.713,-74.006)  # (lat,long) in degrees
New_York_radians = (degrees_to_radians(New_York[0]),degrees_to_radians(New_York[1]))

print("--- Approximate distances Earth ---")
d = distance_approx_lat_long(*Paris_radians,*New_York_radians)
print(d)


def distance_lat_long(lat1,long1,lat2,long2):
    R = 6371  # radius (average) of Earth in km
    a = (sin((lat2-lat1)/2))**2 + cos(lat1)*cos(lat2)*(sin((long2-long1)/2))**2
    d = 2 * R * atan2(sqrt(a),sqrt(1-a))
    return d

# Test 
print("--- Exact distances Earth ---")
d = distance_lat_long(*Paris_radians,*New_York_radians)
print(d)


## Question 3 ##

def file_distances_lat_long(filename):
    # Input file
    fi_in = open(filename,"r")

    list_cities = []

    for line in fi_in:
        list_cities = list_cities + [line.split()]
        
    # Close input file
    fi_in.close()

    # Output file
    name, extension = os.path.splitext(filename)
    new_name = name + "_distances" + ".txt"
    fi_out = open(new_name,"w")

    line = '{:>12s}'.format("")
    for v in list_cities:
        name = v[0]
        line = line + '{:>12s}'.format(name) +" "

    fi_out.write(line + "\n")

    for c1 in list_cities:
        name1 = c1[0]
        lat1 = degrees_to_radians(float(c1[1]))
        long1 = degrees_to_radians(float(c1[2]))

        line = '{:12s}'.format(name1)

        for c2 in list_cities:
            name2 = c2[0]
            lat2 = degrees_to_radians(float(c2[1]))
            long2 = degrees_to_radians(float(c2[2]))

            d = distance_lat_long(lat1,long1,lat2,long2)

            line = line + '{:12d}'.format(round(d)) + " "

        fi_out.write(line + "\n")

    return

print("--- Cities lat_long ---")
file_distances_lat_long("cities_lat_long.txt")