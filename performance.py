"""Performance measurement helpers for graph algorithms."""

from __future__ import annotations

import random
from time import perf_counter
from typing import Dict, List, Sequence

from algorithms import bfs, dfs, dijkstra
from graph import Graph


def create_test_graph(number_of_airports: int, seed: int = 42) -> Graph:
	"""Create a connected deterministic graph for performance experiments."""
	if number_of_airports < 1:
		raise ValueError("The graph must contain at least one airport.")

	graph = Graph()
	airport_names = [f"Airport-{index:03d}" for index in range(1, number_of_airports + 1)]
	for airport in airport_names:
		graph.add_airport(airport)

	if number_of_airports == 1:
		return graph

	random_generator = random.Random(seed + number_of_airports)
	route_pairs = set()

	# A chain guarantees every generated graph is connected.
	for index in range(number_of_airports - 1):
		source = airport_names[index]
		destination = airport_names[index + 1]
		_route_pair_key = frozenset((source, destination))
		route_pairs.add(_route_pair_key)
		graph.add_route(source, destination, random_generator.randint(100, 2000))

	target_routes = min(number_of_airports * 2, number_of_airports * (number_of_airports - 1) // 2)
	while len(route_pairs) < target_routes:
		source, destination = random_generator.sample(airport_names, 2)
		route_pair_key = frozenset((source, destination))
		if route_pair_key in route_pairs:
			continue
		route_pairs.add(route_pair_key)
		graph.add_route(source, destination, random_generator.randint(100, 2000))

	return graph


def benchmark_graph_sizes(
	sizes: Sequence[int] = (10, 20, 50, 100),
	repetitions: int = 3,
) -> List[Dict[str, object]]:
	"""Measure all algorithms for each requested graph size."""
	if repetitions < 1:
		raise ValueError("Repetitions must be at least 1.")

	results: List[Dict[str, object]] = []
	for graph_size in sizes:
		graph = create_test_graph(graph_size)
		source = "Airport-001"
		destination = f"Airport-{graph_size:03d}"
		bfs_times: List[float] = []
		dfs_times: List[float] = []
		dijkstra_times: List[float] = []
		bfs_nodes = dfs_nodes = dijkstra_nodes = 0

		for _ in range(repetitions):
			bfs_start = perf_counter()
			bfs_result = bfs(graph, source)
			bfs_times.append(perf_counter() - bfs_start)
			bfs_nodes = int(bfs_result["nodes_visited"])

			dfs_start = perf_counter()
			dfs_result = dfs(graph, source)
			dfs_times.append(perf_counter() - dfs_start)
			dfs_nodes = int(dfs_result["nodes_visited"])

			dijkstra_start = perf_counter()
			dijkstra_result = dijkstra(graph, source, destination)
			dijkstra_times.append(perf_counter() - dijkstra_start)
			dijkstra_nodes = int(dijkstra_result["nodes_processed"])

		results.append(
			{
				"graph_size": graph_size,
				"routes": sum(len(graph.get_neighbors(airport)) for airport in graph.get_airports()) // 2,
				"bfs_time": sum(bfs_times) / repetitions,
				"dfs_time": sum(dfs_times) / repetitions,
				"dijkstra_time": sum(dijkstra_times) / repetitions,
				"bfs_nodes": bfs_nodes,
				"dfs_nodes": dfs_nodes,
				"dijkstra_nodes": dijkstra_nodes,
			}
		)

	return results
