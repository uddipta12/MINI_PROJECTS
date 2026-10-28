# Flight Route Planner

## 1. Project Title

**Flight Route Planner**

Design and Analysis of Algorithms mini project developed in Python.

## 2. Introduction

Flight Route Planner models airports as vertices and flight connections as weighted edges in a graph. The edge weight represents the approximate distance between two airports in kilometers.

The application provides a Tkinter desktop interface for exploring the airport network, finding shortest routes, running graph traversals, comparing algorithms, and studying measured performance.

## 3. Problem Statement

Given a collection of airports and weighted flight connections, determine how graph algorithms can help users explore the network and find the shortest geographical route between two airports. The project also compares traversal and shortest-path algorithms from both theoretical and empirical perspectives.

## 4. Objectives

- Represent an airport network with an adjacency list.
- Implement BFS and DFS manually.
- Implement Dijkstra's shortest-path algorithm manually.
- Demonstrate a priority queue using Python's `heapq` module.
- Display routes, distances, visited airports, and execution times.
- Compare theoretical complexity with measured performance.
- Provide a professional GUI suitable for an academic demonstration.

## 5. Features

- Dashboard with modular navigation.
- Sample network containing 12 Indian airports and weighted routes.
- Shortest route search using Dijkstra's algorithm.
- BFS and DFS traversal from a selected airport.
- Airport network visualization with distance labels.
- Highlighted shortest path in the network visualization.
- Algorithm comparison table with measured execution times.
- Performance analysis for graphs containing 10, 20, 50, and 100 airports.
- Matplotlib execution-time chart.
- Friendly validation for invalid and unreachable routes.

## 6. Technologies Used

- Python 3.10 or newer
- Tkinter for the desktop GUI
- Matplotlib for graph and performance visualization
- Python standard libraries: `collections`, `heapq`, `math`, `random`, and `time`
- No external database
- No NetworkX shortest-path or traversal implementation

## 7. DAA Concepts Used

- Graph representation
- Weighted and unweighted graphs
- Adjacency lists
- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- Dijkstra's shortest-path algorithm
- Priority queues and binary heaps
- Time complexity
- Space complexity
- Empirical performance analysis

## 8. System Requirements

- Windows, macOS, or Linux
- Python 3.10 or newer
- Tkinter installed and available to Python
- At least one terminal or VS Code installation
- Matplotlib installed from `requirements.txt`

On standard Windows Python installations, Tkinter is usually included. If it is missing, install Python again with the Tcl/Tk option enabled.

## 9. Installation

Open a terminal in the project directory and run:

```powershell
cd FlightRoutePlanner
python -m pip install -r requirements.txt
```

## 10. How to Run

From the `FlightRoutePlanner` directory, run:

```powershell
python main.py
```

The dashboard opens with options for shortest routes, traversal, network visualization, algorithm comparison, and project information.

The algorithm modules can also be tested from a terminal:

```python
from airport_data import build_sample_graph
from algorithms import bfs, dfs, dijkstra

graph = build_sample_graph()
print(bfs(graph, "Delhi"))
print(dfs(graph, "Delhi"))
print(dijkstra(graph, "Delhi", "Bengaluru"))
```

## 11. Project Structure

```text
FlightRoutePlanner/
|
|-- main.py                    Application entry point
|-- graph.py                   Weighted adjacency-list Graph class
|-- algorithms.py              BFS, DFS, and Dijkstra
|-- airport_data.py            Airport and route data
|-- performance.py             Benchmark graph generation and measurements
|-- visualization.py           Matplotlib airport-network visualization
|-- requirements.txt            External Python dependency list
|-- README.md                  Project documentation
|
|-- gui/
	|-- dashboard.py           Main dashboard
	|-- shortest_route.py       Dijkstra route page
	|-- traversal.py            BFS and DFS page
	|-- comparison.py           Complexity and timing pages
	|-- about.py                Project information page
```

## 12. Algorithm Explanation

### Graph Representation

The `Graph` class stores an adjacency list:

```text
Delhi -> Mumbai (1148 km), Jaipur (268 km), Lucknow (500 km)
```

Each airport is a vertex. Each route is stored as a neighboring airport and a distance. Sample routes are bidirectional.

### BFS

BFS uses a queue. It visits all airports at the current level before moving to the next level. BFS is useful for finding the minimum number of edges in an unweighted graph. It does not guarantee the minimum geographical distance when routes have different weights.

### DFS

DFS uses a stack. It follows one route as deeply as possible before backtracking to explore another route. DFS is useful for exploring connectivity and graph structure.

### Dijkstra

Dijkstra maintains the smallest known distance for every airport. A binary-heap priority queue selects the airport with the smallest current distance. A predecessor map reconstructs the complete shortest path after the destination is reached.

## 13. BFS Complexity

- Time complexity: `O(V + E)`
- Space complexity: `O(V)`

Here, `V` is the number of airports and `E` is the number of routes.

For a connected graph, the best, average, and worst cases are generally analyzed as `O(V + E)` because the traversal may need to inspect the entire reachable component. An early destination can reduce practical runtime, but it does not change the standard upper bound.

## 14. DFS Complexity

- Time complexity: `O(V + E)`
- Space complexity: `O(V)`

The stack and visited set require space proportional to the number of airports. As with BFS, the complete traversal upper bound is `O(V + E)`.

## 15. Dijkstra Complexity

This project uses an adjacency list and a binary heap priority queue:

- Time complexity: `O((V + E) log V)`
- Space complexity: `O(V + E)`

The distance table, predecessor table, visited set, priority queue, and adjacency list contribute to the space usage. Dijkstra assumes non-negative edge weights, which is satisfied because route distances are positive.

## 16. Sample Input

```text
Source airport: Delhi (DEL)
Destination airport: Bengaluru (BLR)
```

## 17. Sample Output

```text
Shortest Route: Delhi -> Bengaluru
Total Distance: 1740 km
Airports in Route: 2
Nodes Processed: 10
Execution Time: measured at runtime
Algorithm: Dijkstra's Algorithm
```

Execution time depends on the computer and current Python process, so the application measures it instead of using a fixed value.

## 18. Performance Analysis

The Performance Analysis window generates connected graphs containing 10, 20, 50, and 100 airports. Each algorithm is run repeatedly and the measured times are averaged. The table reports graph size, route count, and visited or processed node counts. A Matplotlib line chart plots graph size against execution time for BFS, DFS, and Dijkstra.

The measured values depend on the computer, Python version, system load, and generated test data. They should be used for empirical comparison rather than as universal benchmarks.

## 19. Advantages

- Clear modular architecture.
- Uses standard Python data structures.
- Demonstrates algorithms without hiding them behind NetworkX.
- Provides both theoretical and measured analysis.
- Includes visual and interactive demonstrations.
- Easy to modify airport and route data.
- Suitable for MCA DAA practical demonstrations.

## 20. Limitations

- The airport data is sample data and does not represent live airline schedules.
- Distances are approximate and do not include ticket price, duration, weather, or availability.
- Routes are treated as bidirectional sample connections.
- No user accounts, booking features, or external database are included.
- Measured runtimes vary between computers and are meaningful mainly for relative comparison.

## 21. Future Scope

- Import airport data from CSV or an API.
- Add flight time, fare, airline, and layover constraints.
- Support directed routes and one-way flights.
- Add A* search using geographical coordinates.
- Add route export and report generation.
- Add automated unit tests and larger benchmark datasets.
- Add interactive route selection directly on the network visualization.

## 22. Conclusion

Flight Route Planner demonstrates how graph theory and algorithm design can solve a practical route-planning problem. The project combines adjacency-list representation, BFS, DFS, Dijkstra's algorithm, priority queues, complexity analysis, GUI development, visualization, and empirical performance measurement in one modular Python application.
