"""Sample airport and route data for the Flight Route Planner."""

from __future__ import annotations

from typing import Dict, List, Tuple

from graph import Graph


# Each airport is stored as (display name, airport code).
AIRPORTS: List[Tuple[str, str]] = [
	("Delhi", "DEL"),
	("Mumbai", "BOM"),
	("Kolkata", "CCU"),
	("Chennai", "MAA"),
	("Bengaluru", "BLR"),
	("Hyderabad", "HYD"),
	("Guwahati", "GAU"),
	("Pune", "PNQ"),
	("Ahmedabad", "AMD"),
	("Jaipur", "JAI"),
	("Kochi", "COK"),
	("Lucknow", "LKO"),
]


# Each route is stored as (source airport, destination airport, distance in km).
ROUTES: List[Tuple[str, str, int]] = [
	("Delhi", "Mumbai", 1148),
	("Delhi", "Kolkata", 1305),
	("Delhi", "Chennai", 1750),
	("Delhi", "Bengaluru", 1740),
	("Delhi", "Hyderabad", 1250),
	("Delhi", "Guwahati", 1450),
	("Delhi", "Jaipur", 268),
	("Delhi", "Lucknow", 500),
	("Mumbai", "Pune", 150),
	("Mumbai", "Ahmedabad", 525),
	("Mumbai", "Kochi", 1060),
	("Mumbai", "Hyderabad", 710),
	("Kolkata", "Guwahati", 520),
	("Kolkata", "Chennai", 1660),
	("Chennai", "Bengaluru", 350),
	("Chennai", "Kochi", 690),
	("Bengaluru", "Hyderabad", 570),
	("Bengaluru", "Kochi", 550),
	("Hyderabad", "Pune", 560),
	("Hyderabad", "Lucknow", 1050),
	("Ahmedabad", "Jaipur", 650),
	("Lucknow", "Guwahati", 1100),
]


def get_airport_code(airport_name: str) -> str:
	"""Return the code for an airport name."""
	airport_codes: Dict[str, str] = dict(AIRPORTS)
	try:
		return airport_codes[airport_name]
	except KeyError as error:
		raise ValueError(f"Unknown airport: {airport_name}") from error


def build_sample_graph() -> Graph:
	"""Create and return the sample airport graph."""
	graph = Graph()

	for airport_name, _ in AIRPORTS:
		graph.add_airport(airport_name)

	for source, destination, distance in ROUTES:
		graph.add_route(source, destination, distance)

	return graph
