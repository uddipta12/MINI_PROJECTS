"""BFS, DFS, and Dijkstra algorithm implementations."""

from __future__ import annotations

from collections import deque
from heapq import heappop, heappush
from math import inf
from time import perf_counter
from typing import Dict, List

from graph import Graph


def bfs(graph: Graph, source: str) -> Dict[str, object]:
	"""Traverse the graph breadth-first from ``source``.

	BFS visits all immediately connected airports before moving to the next
	level. Route distances are intentionally ignored during this traversal.
	"""
	if not graph.get_airports():
		raise ValueError("Cannot run BFS on an empty graph.")
	if source not in graph.get_airports():
		raise ValueError(f"Unknown starting airport: {source}")

	start_time = perf_counter()
	visited = {source}
	traversal_order: List[str] = []
	queue = deque([source])

	while queue:
		current_airport = queue.popleft()
		traversal_order.append(current_airport)

		for neighbor, _ in graph.get_neighbors(current_airport):
			if neighbor not in visited:
				visited.add(neighbor)
				queue.append(neighbor)

	execution_time = perf_counter() - start_time
	return {
		"traversal_order": traversal_order,
		"visited_nodes": traversal_order.copy(),
		"nodes_visited": len(traversal_order),
		"execution_time": execution_time,
	}


def dfs(graph: Graph, source: str) -> Dict[str, object]:
	"""Traverse the graph depth-first from ``source``."""
	if not graph.get_airports():
		raise ValueError("Cannot run DFS on an empty graph.")
	if source not in graph.get_airports():
		raise ValueError(f"Unknown starting airport: {source}")

	start_time = perf_counter()
	visited = set()
	traversal_order: List[str] = []
	stack = [source]

	while stack:
		current_airport = stack.pop()
		if current_airport in visited:
			continue

		visited.add(current_airport)
		traversal_order.append(current_airport)

		# Reverse neighbors so the first listed route is explored first.
		neighbors = graph.get_neighbors(current_airport)
		for neighbor, _ in reversed(neighbors):
			if neighbor not in visited:
				stack.append(neighbor)

	execution_time = perf_counter() - start_time
	return {
		"traversal_order": traversal_order,
		"visited_nodes": traversal_order.copy(),
		"nodes_visited": len(traversal_order),
		"execution_time": execution_time,
	}


def dijkstra(graph: Graph, source: str, destination: str) -> Dict[str, object]:
	"""Find the shortest weighted route between two airports.

	The priority queue always processes the airport with the smallest known
	distance. The graph stores only positive route distances, so Dijkstra's
	algorithm is suitable for this network.
	"""
	if not graph.get_airports():
		raise ValueError("Cannot run Dijkstra on an empty graph.")
	if source not in graph.get_airports():
		raise ValueError(f"Unknown source airport: {source}")
	if destination not in graph.get_airports():
		raise ValueError(f"Unknown destination airport: {destination}")

	start_time = perf_counter()
	airports = graph.get_airports()
	distances = {airport: inf for airport in airports}
	previous_airport: Dict[str, str] = {}
	distances[source] = 0

	priority_queue = [(0, source)]
	visited_nodes: List[str] = []
	visited = set()

	while priority_queue:
		current_distance, current_airport = heappop(priority_queue)
		if current_airport in visited:
			continue

		visited.add(current_airport)
		visited_nodes.append(current_airport)

		if current_airport == destination:
			break

		for neighbor, route_distance in graph.get_neighbors(current_airport):
			new_distance = current_distance + route_distance
			if new_distance < distances[neighbor]:
				distances[neighbor] = new_distance
				previous_airport[neighbor] = current_airport
				heappush(priority_queue, (new_distance, neighbor))

	shortest_distance = distances[destination]
	path: List[str] = []
	if shortest_distance != inf:
		current_airport = destination
		while current_airport != source:
			path.append(current_airport)
			current_airport = previous_airport[current_airport]
		path.append(source)
		path.reverse()
	else:
		shortest_distance = None

	execution_time = perf_counter() - start_time
	return {
		"shortest_distance": shortest_distance,
		"path": path,
		"visited_nodes": visited_nodes,
		"nodes_processed": len(visited_nodes),
		"execution_time": execution_time,
	}
