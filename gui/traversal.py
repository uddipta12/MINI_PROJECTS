"""BFS and DFS traversal GUI page."""

from __future__ import annotations

import tkinter as tk
from tkinter import ttk
from typing import Callable

from airport_data import AIRPORTS, build_sample_graph
from algorithms import bfs, dfs


class TraversalPage(tk.Frame):
	"""GUI page for comparing BFS and DFS traversal order."""

	def __init__(self, master: tk.Misc, on_back: Callable[[], None]) -> None:
		super().__init__(master, bg="#0b1f3a")
		self.on_back = on_back
		self.graph = build_sample_graph()
		self.airport_names = [name for name, _ in AIRPORTS]
		self.source_var = tk.StringVar(value=self.airport_names[0])
		self.result_text: tk.Text
		self._build_layout()

	def _build_layout(self) -> None:
		"""Create the traversal selector, buttons, and output area."""
		self.columnconfigure(0, weight=1)
		self.rowconfigure(3, weight=1)

		tk.Label(
			self,
			text="GRAPH TRAVERSAL",
			font=("Segoe UI", 22, "bold"),
			fg="#f4f7fb",
			bg="#0b1f3a",
		).grid(row=0, column=0, padx=42, pady=(36, 8), sticky="w")
		tk.Label(
			self,
			text="Compare breadth-first and depth-first exploration",
			font=("Segoe UI", 11),
			fg="#b8c7d9",
			bg="#0b1f3a",
		).grid(row=1, column=0, padx=42, pady=(0, 24), sticky="w")

		controls = tk.Frame(self, bg="#132d4f", padx=22, pady=20)
		controls.grid(row=2, column=0, padx=42, sticky="ew")
		tk.Label(
			controls,
			text="Starting Airport",
			font=("Segoe UI", 10, "bold"),
			fg="#f4f7fb",
			bg="#132d4f",
		).grid(row=0, column=0, padx=(0, 10), sticky="w")
		ttk.Combobox(
			controls,
			textvariable=self.source_var,
			values=self.airport_names,
			state="readonly",
			width=20,
		).grid(row=0, column=1, padx=(0, 20))

		for column, label, command in [
			(2, "Run BFS", self.run_bfs),
			(3, "Run DFS", self.run_dfs),
		]:
			tk.Button(
				controls,
				text=label,
				command=command,
				font=("Segoe UI", 10, "bold"),
				bg="#2f80ed",
				fg="#f4f7fb",
				activebackground="#56a0ff",
				relief="flat",
				cursor="hand2",
				padx=14,
				pady=8,
			).grid(row=0, column=column, padx=5)

		self.result_text = tk.Text(
			self,
			height=13,
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

	def run_bfs(self) -> None:
		"""Run BFS from the selected starting airport."""
		self._display_result("BFS", bfs(self.graph, self.source_var.get()))

	def run_dfs(self) -> None:
		"""Run DFS from the selected starting airport."""
		self._display_result("DFS", dfs(self.graph, self.source_var.get()))

	def _display_result(self, algorithm_name: str, result: dict) -> None:
		"""Display a traversal result in the text area."""
		output = (
			f"{algorithm_name} TRAVERSAL\n\n"
			f"Starting Airport: {self.source_var.get()}\n\n"
			f"Traversal Order:\n{' -> '.join(result['traversal_order'])}\n\n"
			f"Airports Visited: {result['nodes_visited']}\n"
			f"Execution Time: {result['execution_time']:.9f} seconds\n\n"
			"BFS and DFS ignore route weights during traversal."
		)
		self.result_text.configure(state="normal")
		self.result_text.delete("1.0", tk.END)
		self.result_text.insert("1.0", output)
		self.result_text.configure(state="disabled")
