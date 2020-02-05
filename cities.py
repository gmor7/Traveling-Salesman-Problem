# Importing math and numpy for random number generation & calculations
from math import *
import random
import numpy as np

# Importing Matplotlib Basemap, Figure and Pyplot for visualisation function
from mpl_toolkits.basemap import Basemap   # please note: requires pip install
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

# Removing unnecessary Matplotlib messages
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

def read_cities(file_name):
    """
    Read in the cities from the given `file_name`, and return them as a list 
    of four-tuples: 
    [(state, city, latitude, longitude), ...]  
    
    Args:
        file_name (.txt file): Reads in states, cities, latitudes and
        longitudes from a given .txt file name.
    
    Returns:
        road_map (List): Returns a list of four-tuples 
                            with city, state, lat, lon.
    """

    try:
        file_cities = open(file_name, 'r')

        # Adding each line into the list road_map        
        road_map = []        
        for line in file_cities:
            road_map.append(tuple(line.strip().split('\t')))
		# floats for lon and lat
        
        file_cities.close()
        return road_map
    
    # Exception to catch erroneous filenames
    except:
        print(" Please ensure that the .txt filename is correct, "
              "that the file exists in the directory and that the "
              "file is not corrupt.", "\n", "\n", "\n", "\n")
        exit
        
def print_cities(road_map):
    """
    Prints a list of cities, along with their locations. Print only one or two 
    digits after the decimal point.
    
    Args:
        road_map (List): List of four-tuples with city, state, lat, lon.
    
    Prints:
        elem (List): A list of cities and their locations is printed with two 
                    digits after the decimal point. Each city is on a new line.
    """

    # Adding each city and its location (rounded to two decimals) into a list
    city_map = []
    for i in road_map:
        city_map.append((i[0], i[1], 
                         round(float(i[2]), 2),
                         round(float(i[3]), 2)))
        
    # Printing each city on a new line
    for elem in city_map:
        print(elem)
        
def compute_each_distance(road_map):
    """
    Returns a list of the individual distances between each city in the 
    road map "circuit". Distances are returned as floating point numbers 
    with 2 decimal places.
    
    Args:
        road_map (List): List of four-tuples with city, state, lat, lon.
    
    Returns:
        all_distances_list (List): List of the distances between each city in
                                    a given road map as floating points numbers
                                    (2 decimal places).
    """
    
    # Creating an empty list
    all_distances_list = []
    
    # Looping through the given road map
    i = -1
    while i < len(road_map) - 1:

        # Current & next longitude and latitude assigned to variables
        # for the "circuit" (i.e. includes last location back to starting point)
        lat1 = str(road_map[i][2])
        lon1 = str(road_map[i][3])
        lat2 = str(road_map[(i+1)%len(road_map)][2])
        lon2 = str(road_map[(i+1)%len(road_map)][3])
        
        # Longitudes and longitudes converted to floating points (2 decimals)
        lat1 = round(float(lat1), 2)
        lon1 = round(float(lon1), 2)
        lat2 = round(float(lat2), 2)
        lon2 = round(float(lon2), 2)
        
        # Calculation of euclidean distance between points
        latitude = (lat1-lat2)**2
        longitude = (lon1-lon2)**2
        dist = sqrt(latitude + longitude)
        dist = round(float(dist), 2)
        
        # Adding each calculated distance to the list (all_distances_list)
        all_distances_list.append(dist)
        i += 1
    
    return all_distances_list

def compute_total_distance(road_map):
    """
    Returns, as a floating point number, the sum of the distances of all
    the connections in the `road_map`. Remember that it's a cycle, so that 
    (for example) in the initial `road_map`, Wyoming connects to Alabama...
    
    Args:
        road_map (List): List of four-tuples with city, state, lat, lon.
    
    Returns:
        distance (Float): Total distance of road map as a 2 decimal float.
    """
    
    # Returns the sum of all distances using the compute_each_distance function
    all_distances_list = compute_each_distance(road_map)
    return round(sum(all_distances_list), 2)

def swap_cities(road_map, index1, index2):
    """
    Take the city at location `index1` in the `road_map`, and the 
    city at location `index2`, swap their positions in the `road_map`, 
    compute the new total distance, and return the tuple 

    (new_road_map, new_total_distance)

    Allow for the possibility that `index1=index2`, 
    and handle this case correctly.
    
    Args:
        road_map (List): List of four-tuples with city, state, lat, lon.
        index1 (Integer): Integer to reference a location in the road_map.
        index2 (Integer): Integer to reference a location in the road_map.
    
    Returns:
        (new_road_map, new_total_distance) (Tuple):
        List of four-tuples with city, state, lat, lon after index1 and index2 
        have been swapped, and the total distance of the new_road_map as a
        floating point number (2 decimal places).                          
    """
    
    # New list created
    new_road_map = list(road_map[:])
    
    # If indexes are identical then nothing happens: the function carries on
    if index1 == index2:
        pass
    
    # Swapping the locations at index1 and index2
    (new_road_map[index1], new_road_map[index2]) = (new_road_map[index2], 
                                                    new_road_map[index1])
    
    # Returning the new_road_map and the total distance of that map
    return (new_road_map, compute_total_distance(new_road_map))

def shift_cities(road_map):
    """
    For every index i in the `road_map`, the city at the position i moves
    to the position i+1. The city at the last position moves to the position
    0. Return the the new road map.
    
    Args:
        road_map (List): List of four-tuples with city, state, lat, lon.
        
    Returns:
        new_road_map (List): List of four-tuples with city, state, lat, lon
                             after the cities have been shifted up one place.
    """
    # New list created
    new_road_map = list(road_map[:])
    
    # City at last position moves to position 0, other cities at i move to i+1 
    new_road_map.insert(0,new_road_map.pop())
    
    return new_road_map

def find_best_cycle(road_map):
    """
    Using a combination of `swap_cities` and `shift_cities`, 
    try `10000` swaps/shifts, and each time keep the best cycle found so far. 
    After `10000` swaps/shifts, return the best cycle found so far.
    Use randomly generated indices for swapping.
    
    Args:
        road_map (List): List of four-tuples with city, state, lat, lon.
        
    Returns:
        newer_road_map (List): List of four-tuples with city, state, lat, lon.
                                after the best cycle is found by using swap
                                cities x8000 and shift cities x2000.
    """
    
    current_distance = None
    newer_road_map = road_map[:]
    
    # 8000 loops of swap_cities function. Heavier weighting on swap cities due 
    # to better results being yielded
    for i in range(0, 8000):
        # Random index1 and index2 integers generated
        index1 = random.randint(0, len(road_map) - 1)
        index2 = random.randint(0, len(road_map) - 1)
        
        # Passing index1 and index2 through the swap_cities function and
        # assigning returns to variables
        (best_cycle, best_cycle_distance) = swap_cities(newer_road_map, 
                                                            index1, index2)
        
        # If the best_cycle_distance is lower than the current_distance
        if current_distance is None or best_cycle_distance < current_distance:
            
            # The current_distance becomes the best_cycle_distance
            current_distance = best_cycle_distance
            
            # The best_cycle (with the lowest distance) becomes the
            # newer_road_map to be run through the loop next
            newer_road_map = best_cycle
    
    # 2000 loops of shift_cities function
    for i in range(0, 2000):
        # Putting the best cycle (newer_road_map) through shift_cities
        new_shifted_map = shift_cities(newer_road_map)
        
        # Computing the total distance of the shifted map
        newest_cycle_distance2 = compute_total_distance(new_shifted_map)
        
        # If the total distance is lower than the current (lowest) distance
        # (from the swap cities loop) then this road map is assigned as the
        # return variable (newer_road_map)
        if newest_cycle_distance2 < current_distance:
            current_distance = newest_cycle_distance2
            newer_road_map = new_shifted_map
    
    # The best cycle is returned
    return newer_road_map

def print_map(road_map):
    """
    Prints, in an easily understandable textual format, the cities and 
    their connections, along with the cost for each connection 
    and the total cost.
    
    Args:
        road_map (List): List of four-tuples with city, state, lat, lon.
    
    Prints:
        city_to_next_city (Tuple): City and next city printed along with the;
        cost_per_connection (Float): The cost of the city to next city connect.
        total_distance (Float): The total cost of the road_map.
    """
    
    # Total distance and cost per connection computed
    total_distance = compute_total_distance(road_map)
    cost_per_connection = compute_each_distance(road_map)

    # Looping over the road_map and printing each city to next city connection
    # along with the cost of the connection
    for i in range(0, len(road_map)):
        city_to_next_city = (road_map[i][0:2], "->", 
                            road_map[(i+1)%len(road_map)][0:2])
        x = cost_per_connection[i]
        print(city_to_next_city,": The cost of this connection is", x)
    
    # Printing the total distance of the road_map
    print("\n","The total cost of the best route is", total_distance,"\n")

def visualise(road_map):
    """
    Extension of the implementation allowing for visualisation of road maps 
    using matplotlib.
    
    Args:
        road_map (List): List of four-tuples with city, state, lat, lon.
    
    Visualised:
        best route (Figure): A map of the world is drawn and the locations are 
        circled in yellow, numbered in black and named in grey. The red lines 
        indicate a connection between cities.
    """
    
    # Given road_map (full "circuit") is added to a list
    points = list(road_map)
    points.insert(len(points), points[0])

    # Map of the world is drawn using Basemap
    plt.figure(figsize=(13,7))
    m = Basemap(llcrnrlon=-180,
                llcrnrlat=-90,
                urcrnrlon=180,
                urcrnrlat=90,
                projection='mill',
                resolution ='l')
    
    # Colours and features added to the map
    m.drawcoastlines(color='palegreen')
    m.drawcountries(color='honeydew', linewidth=1)
    m.fillcontinents(color='palegreen',lake_color='lightcyan')
    m.drawstates(color='honeydew')
    
    
    # Creation of list of states and cities for map name labels
    cities_of_cycle = list(x[0:2] for x in points)
    
    # Creation of dictionary for map number labels
    cities_of_cycle_1 = {index: x for index, 
                         x in enumerate(cities_of_cycle, start=1)}
    # Removal of number 51 (as route ends at number 1)
    cities_of_cycle_2 = list(cities_of_cycle_1)[:-1]
    
    # Numbering and states+cities combined
    cities_of_cycle_3 = [(cities_of_cycle_2[i], cities_of_cycle[i]) 
                            for i in range(0, len(cities_of_cycle_2))]

    # Coordinates of each city added to xpt and ypt variables for plotting
    coordinates_of_cycle = [x[2:] for x in points]
    lat = [x[:1] for x in coordinates_of_cycle]
    lon = [x[1] for x in coordinates_of_cycle]
    lat = np.array(lat, dtype=float)
    lon = np.array(lon, dtype=float)
    xpt, ypt = m(lon, lat)

    # Plotting city connection lines
    m.plot(xpt, ypt, 'c', markersize=1, color='orangered')
    # Plotting circle for each city
    m.plot(xpt, ypt, 'o', markersize=5, color='yellow')
        
    # Adding a space before each 1-9 number to ensure names are lined up
    # with numbers correctly
    label_numbering = [i[0] for i in cities_of_cycle_3]
    label_numbering2 = []
    for i in label_numbering[0:9]:
        x = " " + str(i)
        label_numbering2.append(x)
    for i in label_numbering[9:50]:
        y = i
        label_numbering2.append(y)
    
    # Names of each city for labels with spaces for correct formatting
    labels_cities = ["     "+i[1] for i in cities_of_cycle]
    
    # Labelling each location with number
    for label, x, y in zip(label_numbering2, xpt, ypt):
        plt.text(x, y, label, size=8, fontweight='bold', color='black')
    
    # Labelling each location with city name
    for label, x, y in zip(labels_cities, xpt, ypt):
        plt.text(x, y, label, size=6, fontweight='bold', color='dimgrey') 
    
    # Tile of map
    plt.title("Best Route \n Please zoom into the zone of your road map")
    
    plt.show()

def main():
    """
    Requests to specify the file to load (make sure the file exists and valid), 
    reads in and prints out the city data, creates the *"best"* cycle, 
    prints it out.
    """
    
    # Reading the filename of user's desired road map
    print("\n")
    filename = input(" Please enter the road map .txt file name: ")
    print("\n")
    
    # Printing the user selected road map
    road_map = read_cities(filename)
    print(" The road map you have selected is: ","\n")
    print_cities(road_map)
    
    # Message to user during calculation of best route
    print("\n","Please wait while the best route is calculated...", "\n")
    
    # Road map for visualisation set to the best route by default
    new_road_map = find_best_cycle(road_map)
    
    # Printing the best route and opening the matplotlib visualisation of same
    print(" The connections & costs per connection of the best route are: ",
          "\n")
    print_map(new_road_map)
    visualise(new_road_map)

if __name__ == "__main__":
    main()
