"""Algorithm comparison GUI page."""

from __future__ import annotations

import tkinter as tk
from tkinter import ttk
from time import perf_counter
from typing import Callable, List, Tuple

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from airport_data import build_sample_graph
from algorithms import bfs, dfs, dijkstra
from performance import benchmark_graph_sizes


class ComparisonPage(tk.Frame):
	"""Display algorithm purposes, complexity, and measured runtimes."""

	def __init__(self, master: tk.Misc, on_back: Callable[[], None]) -> None:
		super().__init__(master, bg="#0b1f3a")
		self.on_back = on_back
		self.graph = build_sample_graph()
		self._build_layout()

	def _build_layout(self) -> None:
		"""Create the comparison table and measurement controls."""
		self.columnconfigure(0, weight=1)
		tk.Label(
			self,
			text="ALGORITHM COMPARISON",
			font=("Segoe UI", 22, "bold"),
			fg="#f4f7fb",
			bg="#0b1f3a",
		).grid(row=0, column=0, padx=42, pady=(36, 8), sticky="w")
		tk.Label(
			self,
			text="Measured on the current 12-airport graph",
			font=("Segoe UI", 11),
			fg="#b8c7d9",
			bg="#0b1f3a",
		).grid(row=1, column=0, padx=42, pady=(0, 22), sticky="w")

		columns = ("algorithm", "purpose", "time", "space", "measured")
		table = ttk.Treeview(self, columns=columns, show="headings", height=6)
		headings = {
			"algorithm": "Algorithm",
			"purpose": "Purpose",
			"time": "Time Complexity",
			"space": "Space Complexity",
			"measured": "Measured Time",
		}
		widths = {"algorithm": 120, "purpose": 220, "time": 170, "space": 150, "measured": 150}
		for column in columns:
			table.heading(column, text=headings[column])
			table.column(column, width=widths[column], anchor="center")
		table.grid(row=2, column=0, padx=42, pady=8, sticky="ew")

		results = self._measure_algorithms()
		rows: List[Tuple[str, str, str, str, str]] = [
			("BFS", "Unweighted traversal", "O(V + E)", "O(V)", f"{results[0]:.9f} sec"),
			("DFS", "Deep graph traversal", "O(V + E)", "O(V)", f"{results[1]:.9f} sec"),
			(
				"Dijkstra",
				"Weighted shortest path",
				"O((V + E) log V)",
				"O(V + E)",
				f"{results[2]:.9f} sec",
			),
		]
		for row in rows:
			table.insert("", "end", values=row)

		tk.Label(
			self,
			text="Measured values depend on the computer and current test data.",
			font=("Segoe UI", 10, "italic"),
			fg="#b8c7d9",
			bg="#0b1f3a",
		).grid(row=3, column=0, padx=42, pady=(18, 8), sticky="w")
		tk.Button(
			self,
			text="Run Performance Analysis",
			command=self.show_performance_analysis,
			font=("Segoe UI", 10, "bold"),
			bg="#2f80ed",
			fg="#f4f7fb",
			activebackground="#56a0ff",
			relief="flat",
			cursor="hand2",
			padx=14,
			pady=7,
		).grid(row=4, column=0, pady=(12, 4))
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
		).grid(row=5, column=0, pady=(8, 28))

	def _measure_algorithms(self) -> Tuple[float, float, float]:
		"""Measure each algorithm with perf_counter on the current graph."""
		start = perf_counter()
		bfs(self.graph, "Delhi")
		bfs_time = perf_counter() - start

		start = perf_counter()
		dfs(self.graph, "Delhi")
		dfs_time = perf_counter() - start

		start = perf_counter()
		dijkstra(self.graph, "Delhi", "Bengaluru")
		dijkstra_time = perf_counter() - start
		return bfs_time, dfs_time, dijkstra_time

	def show_performance_analysis(self) -> None:
		"""Open a table and line chart for increasing graph sizes."""
		results = benchmark_graph_sizes()
		window = tk.Toplevel(self)
		window.title("Performance Analysis")
		window.geometry("1120x820")
		window.configure(bg="#0b1f3a")
		window.columnconfigure(0, weight=1)
		window.rowconfigure(2, weight=1)

		tk.Label(
			window,
			text="PERFORMANCE ANALYSIS",
			font=("Segoe UI", 20, "bold"),
			foreground="#f4f7fb",
			background="#0b1f3a",
		).grid(row=0, column=0, padx=28, pady=(24, 4), sticky="w")
		tk.Label(
			window,
			text="Measured values depend on the computer and generated test data.",
			font=("Segoe UI", 10, "italic"),
			foreground="#b8c7d9",
			background="#0b1f3a",
		).grid(row=1, column=0, padx=28, pady=(0, 12), sticky="w")

		columns = (
			"size",
			"routes",
			"bfs_nodes",
			"dfs_nodes",
			"dijkstra_nodes",
		)
		table = ttk.Treeview(window, columns=columns, show="headings", height=5)
		headings = {
			"size": "Airports",
			"routes": "Routes",
			"bfs_nodes": "BFS Nodes",
			"dfs_nodes": "DFS Nodes",
			"dijkstra_nodes": "Dijkstra Nodes",
		}
		for column in columns:
			table.heading(column, text=headings[column])
			table.column(column, width=145, anchor="center")
		for result in results:
			table.insert(
				"",
				"end",
				values=(
					result["graph_size"],
					result["routes"],
					result["bfs_nodes"],
					result["dfs_nodes"],
					result["dijkstra_nodes"],
				),
			)
		table.grid(row=2, column=0, padx=28, pady=10, sticky="ew")

		figure = Figure(figsize=(10, 4.5), dpi=100, facecolor="#0b1f3a")
		axes = figure.add_subplot(111)
		axes.set_facecolor("#132d4f")
		sizes = [result["graph_size"] for result in results]
		axes.plot(sizes, [result["bfs_time"] for result in results], marker="o", label="BFS")
		axes.plot(sizes, [result["dfs_time"] for result in results], marker="o", label="DFS")
		axes.plot(
			sizes,
			[result["dijkstra_time"] for result in results],
			marker="o",
			label="Dijkstra",
		)
		axes.set_title("Graph Size vs Execution Time", color="#f4f7fb")
		axes.set_xlabel("Number of Airports", color="#f4f7fb")
		axes.set_ylabel("Execution Time (seconds)", color="#f4f7fb")
		axes.tick_params(colors="#f4f7fb")
		for spine in axes.spines.values():
			spine.set_color("#8aa4c2")
		axes.grid(color="#8aa4c2", alpha=0.25)
		legend = axes.legend(facecolor="#132d4f", edgecolor="#8aa4c2")
		for label in legend.get_texts():
			label.set_color("#f4f7fb")
		figure.tight_layout()

		canvas = FigureCanvasTkAgg(figure, master=window)
		canvas.draw()
		canvas.get_tk_widget().grid(row=3, column=0, padx=28, pady=10, sticky="nsew")
