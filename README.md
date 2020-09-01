This considers a simplified version of the travelling salesman problem:

"Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city and returns to the origin city?"

**General idea of the assignment**

Suppose there are a number of "cities", as in shown in Figure 1:

![alt text](https://camo.githubusercontent.com/aa86ccb224b243d6b171bd6baf28f5ed2fd55b70/68747470733a2f2f7777772e6463732e62626b2e61632e756b2f7e766c61642f7075622f706f70312f70726f6a2f466967757265312e706e67)

The distance between any two cities with the coordinates (x1, y1) and (x2,y2) is the standard Euclidean distance, that is,

sqrt((x1-x2)^2 + (y1-y2)^2)

Thus, we assume that the Earth is "flat" for the purposes of this assignment. A traveling salesman wishes to visit every city exactly once, then return to their starting point. (It doesn't matter what city is the starting point.) Such a path is called a circuit, as in Figure 2:

![alt text](https://camo.githubusercontent.com/668c0bd15e9c1dab390da0bfba4dc7cdbf3498b8/68747470733a2f2f7777772e6463732e62626b2e61632e756b2f7e766c61642f7075622f706f70312f70726f6a2f466967757265322e706e67)

However, the salesman also wishes to minimise the total distance that must be traveled.

**Specific requirements**

Data representation
We are providing a file, city-data.txt, containing the latitudes and longitudes of the fifty state capitals of the U.S.A. Each line contains:

the name of the state,
the name of the city,
the latitude, and
the longitude.
These four items are separated by tabs (\t symbol). Read this file in as a list of four-tuples. The list tuples will be referred to as a "road map". It represents the path the salesman follows, starting with the first city in the list and ending back at the first city in the list. You can assume that the format of the input file as above.

Note however that the file name as well as its contents can be arbitrary (e.g., it can be a file Brazil.txt with the info on Brazilian states/cities).

While we will require these particular data representations as function parameters and function results, this does not imply that you have to work with these representations as you solve the problems. What you do inside the functions is up to you, as long as they work as expected. (Python makes it easy to convert from one kind of sequence to another.)

**Required functions (file cities.py)**

*def read_cities(file_name)*

Read in the cities from the given file_name, and return them as a list of four-tuples:

[(state, city, latitude, longitude), ...] 
Note that the list above will be used as your initial road_map, that is,

Alabama -> Alaska -> Arizona -> ... -> Wyoming.
as in the example of the file city-data.txt

*def print_cities(road_map)*

Prints a list of cities, along with their locations. Print up to two digits after the decimal point.

*def compute_total_distance(road_map)*

Returns, as a floating point number, the sum of the distances of all the connections in the road_map. Remember that it's a cycle, so that for example in the initial road_map above, Wyoming connects to Alabama...

def swap_cities(road_map, index1, index2)

Take the city at location index in the road_map, and the city at location index2, swap their positions in the road_map, compute the new total distance, and return the tuple

(new_road_map, new_total_distance)
Allow for the possibility that index1=index2, and handle this case correctly.

*def shift_cities(road_map)*

For every index i in the road_map, the city at the position i moves to the position i+1. The city at the last position moves to the position 0. Return the the new road map.

*def find_best_cycle(road_map)*

Using a combination of swap_cities and shift_cities, try 10000 swaps/shifts, and each time keep the best cycle found so far. After 10000 swaps/shifts, return the best cycle found so far. Use randomly generated indices for swapping.

*def print_map(road_map)*

Prints, in an easily understandable textual format, the cities and their connections, along with the cost for each connection and the total cost. This can also be visualised for additional credits.

*def main()*

Requests to specify the file to load (make sure the file exists and valid), reads in and prints out the city data, creates the "best" cycle, prints it out.

**Output**

The end output is a list of the cities visited, along with the precise (shortest) distance between each city. A visualisation of the map and routes is then created using Matplotlib:

![Image description](https://github.com/gmor7/Travelling-Salesman-Problem/blob/master/Travelling%20Salesman%20Visualisation%20copy.png)
