"""Airport network visualization helpers."""

from __future__ import annotations

import tkinter as tk
from math import cos, pi, sin
from typing import List, Optional, Tuple

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from graph import Graph


BACKGROUND = "#0b1f3a"
NODE_COLOR = "#2f80ed"
EDGE_COLOR = "#8aa4c2"
PATH_COLOR = "#f2c94c"
TEXT_COLOR = "#f4f7fb"


def show_network(
	graph: Graph,
	parent: tk.Misc,
	highlighted_path: Optional[List[str]] = None,
) -> tk.Toplevel:
	"""Open a Tkinter window containing the airport network graph."""
	window = tk.Toplevel(parent)
	window.title("Airport Network")
	window.geometry("1050x760")
	window.configure(bg=BACKGROUND)

	figure = Figure(figsize=(10, 7), dpi=100, facecolor=BACKGROUND)
	axes = figure.add_subplot(111)
	axes.set_facecolor(BACKGROUND)
	_draw_network(axes, graph, highlighted_path or [])

	canvas = FigureCanvasTkAgg(figure, master=window)
	canvas.draw()
	canvas.get_tk_widget().pack(fill="both", expand=True, padx=12, pady=12)
	return window


def _draw_network(axes, graph: Graph, highlighted_path: List[str]) -> None:
	"""Draw airport nodes, routes, labels, and an optional highlighted path."""
	airports = graph.get_airports()
	positions = _get_positions(airports)
	highlighted_edges = {
		frozenset((source, destination))
		for source, destination in zip(highlighted_path, highlighted_path[1:])
	}
	drawn_edges = set()

	for source in airports:
		for destination, distance in graph.get_neighbors(source):
			edge_key = frozenset((source, destination))
			if edge_key in drawn_edges:
				continue
			drawn_edges.add(edge_key)
			source_x, source_y = positions[source]
			destination_x, destination_y = positions[destination]
			edge_color = PATH_COLOR if edge_key in highlighted_edges else EDGE_COLOR
			line_width = 3.2 if edge_key in highlighted_edges else 1.2
			axes.plot(
				[source_x, destination_x],
				[source_y, destination_y],
				color=edge_color,
				linewidth=line_width,
				alpha=0.9,
				zorder=1,
			)
			label_x = (source_x + destination_x) / 2
			label_y = (source_y + destination_y) / 2
			axes.text(
				label_x,
				label_y,
				f"{distance} km",
				color=TEXT_COLOR,
				fontsize=7,
				ha="center",
				va="center",
				bbox={"facecolor": BACKGROUND, "edgecolor": "none", "pad": 1.5},
				zorder=3,
			)

	axes.scatter(
		[positions[airport][0] for airport in airports],
		[positions[airport][1] for airport in airports],
		s=950,
		color=NODE_COLOR,
		edgecolors=TEXT_COLOR,
		linewidths=1.2,
		zorder=2,
	)
	for airport in airports:
		x_position, y_position = positions[airport]
		axes.text(
			x_position,
			y_position,
			airport,
			color=TEXT_COLOR,
			fontsize=8,
			fontweight="bold",
			ha="center",
			va="center",
			zorder=4,
		)

	title = "Airport Network"
	if highlighted_path:
		title += " | Highlighted shortest path: " + " -> ".join(highlighted_path)
	axes.set_title(title, color=TEXT_COLOR, fontsize=13, pad=16)
	axes.set_xlim(-1.35, 1.35)
	axes.set_ylim(-1.25, 1.25)
	axes.axis("off")
	figure = axes.get_figure()
	figure.tight_layout()


def _get_positions(airports: List[str]) -> dict[str, Tuple[float, float]]:
	"""Return a readable circular layout for any number of airports."""
	positions = {}
	count = max(len(airports), 1)
	for index, airport in enumerate(airports):
		angle = (2 * pi * index / count) + pi / 2
		positions[airport] = (cos(angle), sin(angle))
	return positions
