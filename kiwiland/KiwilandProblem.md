#Trains

The local commuter railroad services a number of towns in Kiwiland.  
Because of monetary concerns, all of the tracks are 'one-way.'  
That is, a route from Mumbai to Thane does not imply the existence of a route from Thane to Mumbai  
In fact, even if both of these routes do happen to exist, they are distinct and are not necessarily the same distance  
The purpose of this problem is to help the railroad provide its customers with information about the routes.  
In particular, you will compute the distance along a certain route, the number of different routes between two towns,   
and the shortest route between two towns.

**Input**:  A directed graph where a node represents a town and an edge represents a route between two towns.  
The weighting of the edge represents the distance between the two towns.  
A given route will never appear more than once, and for a given route, the starting and ending town will not be the same town.      

**Output**: For test input 1 through 5, if no such route exists, output _'Route does not exist'_.  
* The distance of the route A-E-B-C-D.
* The distance of the route A-E-D.
* The length of the shortest route (in terms of distance to travel) from A to C.

##Test Input:
Graph: AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7
##_Expected Output_:
Output #1: 22
Output #2: Route does not exist
Output #3: 9