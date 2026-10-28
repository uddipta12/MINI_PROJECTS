"""Shortest route GUI page."""

from __future__ import annotations

import tkinter as tk
from tkinter import ttk
from typing import Callable

from airport_data import AIRPORTS, build_sample_graph, get_airport_code
from algorithms import dijkstra


class ShortestRoutePage(tk.Frame):
	"""GUI page for finding a shortest weighted route."""

	def __init__(self, master: tk.Misc, on_back: Callable[[], None]) -> None:
		super().__init__(master, bg="#0b1f3a")
		self.on_back = on_back
		self.graph = build_sample_graph()
		self.airport_names = [name for name, _ in AIRPORTS]
		self.source_var = tk.StringVar(value=self.airport_names[0])
		self.destination_var = tk.StringVar(value=self.airport_names[1])
		self.result_text: tk.Text
		self._build_layout()

	def _build_layout(self) -> None:
		"""Create route selection controls and result area."""
		self.columnconfigure(0, weight=1)
		self.rowconfigure(3, weight=1)

		tk.Label(
			self,
			text="SHORTEST FLIGHT ROUTE",
			font=("Segoe UI", 22, "bold"),
			fg="#f4f7fb",
			bg="#0b1f3a",
		).grid(row=0, column=0, padx=42, pady=(36, 8), sticky="w")
		tk.Label(
			self,
			text="Dijkstra's algorithm on the weighted airport network",
			font=("Segoe UI", 11),
			fg="#b8c7d9",
			bg="#0b1f3a",
		).grid(row=1, column=0, padx=42, pady=(0, 24), sticky="w")

		controls = tk.Frame(self, bg="#132d4f", padx=22, pady=20)
		controls.grid(row=2, column=0, padx=42, sticky="ew")
		controls.columnconfigure(1, weight=1)
		controls.columnconfigure(3, weight=1)

		self._add_selector(controls, "Source Airport", self.source_var, 0)
		self._add_selector(controls, "Destination Airport", self.destination_var, 2)
		tk.Button(
			controls,
			text="Find Shortest Route",
			command=self.find_route,
			font=("Segoe UI", 11, "bold"),
			bg="#2f80ed",
			fg="#f4f7fb",
			activebackground="#56a0ff",
			relief="flat",
			cursor="hand2",
			padx=14,
			pady=8,
		).grid(row=1, column=0, columnspan=4, pady=(18, 0))

		self.result_text = tk.Text(
			self,
			height=12,
			bg="#f4f7fb",
			fg="#132d4f",
			font=("Consolas", 11),
			relief="flat",
			padx=18,
			pady=14,
			state="disabled",
		)
		self.result_text.grid(row=3, column=0, padx=42, pady=24, sticky="nsew")

		tk.Button(
			self,
			text="Back to Dashboard",
			command=self.on_back,
			font=("Segoe UI", 10, "bold"),
			bg="#263b55",
			fg="#f4f7fb",
			activebackground="#3b5573",
			relief="flat",
			cursor="hand2",
			padx=14,
			pady=7,
		).grid(row=4, column=0, pady=(0, 28))

	def _add_selector(
		self,
		parent: tk.Frame,
		label: str,
		variable: tk.StringVar,
		column: int,
	) -> None:
		"""Add one labeled airport combobox to the control panel."""
		tk.Label(
			parent,
			text=label,
			font=("Segoe UI", 10, "bold"),
			fg="#f4f7fb",
			bg="#132d4f",
		).grid(row=0, column=column, padx=(0, 8), sticky="w")
		combo = ttk.Combobox(
			parent,
			textvariable=variable,
			values=self.airport_names,
			state="readonly",
			width=18,
		)
		combo.grid(row=0, column=column + 1, padx=(0, 18), sticky="ew")

	def find_route(self) -> None:
		"""Run Dijkstra and display the route summary."""
		source = self.source_var.get()
		destination = self.destination_var.get()
		result = dijkstra(self.graph, source, destination)
		source_code = get_airport_code(source)
		destination_code = get_airport_code(destination)

		if result["shortest_distance"] is None:
			output = (
				"SHORTEST FLIGHT ROUTE\n\n"
				f"Source: {source} ({source_code})\n"
				f"Destination: {destination} ({destination_code})\n\n"
				"No route is available between these airports."
			)
		else:
			path = result["path"]
			output = (
				"SHORTEST FLIGHT ROUTE\n\n"
				f"Source: {source} ({source_code})\n"
				f"Destination: {destination} ({destination_code})\n\n"
				f"Route: {' -> '.join(path)}\n"
				f"Total Distance: {result['shortest_distance']} km\n"
				f"Airports in Route: {len(path)}\n"
				f"Nodes Processed: {result['nodes_processed']}\n"
				f"Execution Time: {result['execution_time']:.9f} seconds\n\n"
				"Algorithm: Dijkstra's Algorithm"
			)

		self.result_text.configure(state="normal")
		self.result_text.delete("1.0", tk.END)
		self.result_text.insert("1.0", output)
		self.result_text.configure(state="disabled")
