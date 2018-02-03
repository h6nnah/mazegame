These files contain code for a simple Vpython interactive game developed 
in April 2013 by Hannah Erdevig. 
maze.py builds a graph of some specified square number of nodes 
with random edges between those nodes given the following constraints:
   -Each node has between 1 and 4 edges
   -The arrangement of the nodes is such that the graph can be aligned 
    on an n x n grid, where n is the square root of the number of nodes 
    in the graph.
   -The edges connecting the nodes creates at least one path from one 
    node to the other each specified as an attribute of the graph built.
From this graph data, the program builds a 3-D maze that is navigated by 
a ball that moves with user arrow-key input.
The walls of the maze bisect any two nodes with no edge between them, 
thus creating blank paths that visually represent the paths of the graph.
For any random graph, a Depth First Search algorithm determines the 
shortest path between the chosen "start" and "end" nodes.
If the user follows this path, the words "You won!" appear on the screen.

