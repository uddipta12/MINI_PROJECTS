"""Graph data structure for airports and flight routes."""

from __future__ import annotations

from typing import Dict, List, Tuple


class Graph:
	"""A weighted graph represented with an adjacency list.

	Airports are stored as vertices and routes are stored as weighted edges.
	Routes are bidirectional by default because a flight connection can be
	travelled in either direction in this sample project.
	"""

	def __init__(self) -> None:
		self.adjacency_list: Dict[str, List[Tuple[str, int]]] = {}

	def add_airport(self, airport: str) -> None:
		"""Add an airport if it is not already present."""
		airport = airport.strip()
		if not airport:
			raise ValueError("Airport name cannot be empty.")

		self.adjacency_list.setdefault(airport, [])

	def add_route(
		self,
		source: str,
		destination: str,
		distance: int,
		bidirectional: bool = True,
	) -> None:
		"""Add a weighted route between two existing airports."""
		source = source.strip()
		destination = destination.strip()

		if source not in self.adjacency_list:
			raise ValueError(f"Unknown source airport: {source}")
		if destination not in self.adjacency_list:
			raise ValueError(f"Unknown destination airport: {destination}")
		if source == destination:
			raise ValueError("A route must connect two different airports.")
		if not isinstance(distance, (int, float)) or distance <= 0:
			raise ValueError("Route distance must be a positive number.")

		self._add_or_update_neighbor(source, destination, int(distance))
		if bidirectional:
			self._add_or_update_neighbor(destination, source, int(distance))

	def _add_or_update_neighbor(
		self, source: str, destination: str, distance: int
	) -> None:
		"""Add a neighbor or update its distance if the route already exists."""
		neighbors = self.adjacency_list[source]
		for index, (neighbor, _) in enumerate(neighbors):
			if neighbor == destination:
				neighbors[index] = (destination, distance)
				return

		neighbors.append((destination, distance))

	def get_neighbors(self, airport: str) -> List[Tuple[str, int]]:
		"""Return the neighboring airports and distances for an airport."""
		if airport not in self.adjacency_list:
			raise ValueError(f"Unknown airport: {airport}")

		return list(self.adjacency_list[airport])

	def get_airports(self) -> List[str]:
		"""Return all airport names in insertion order."""
		return list(self.adjacency_list.keys())

	def display_graph(self) -> str:
		"""Return the adjacency list in a readable format."""
		if not self.adjacency_list:
			return "The graph is empty."

		lines = []
		for airport, neighbors in self.adjacency_list.items():
			if neighbors:
				routes = ", ".join(
					f"{neighbor} ({distance} km)"
					for neighbor, distance in neighbors
				)
				lines.append(f"{airport} -> {routes}")
			else:
				lines.append(f"{airport} -> No routes")

		return "\n".join(lines)
