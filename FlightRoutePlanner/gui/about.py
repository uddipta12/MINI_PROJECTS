"""About project GUI page."""

from __future__ import annotations

import tkinter as tk
from typing import Callable


class AboutPage(tk.Frame):
	"""Display project purpose and the DAA concepts demonstrated."""

	def __init__(self, master: tk.Misc, on_back: Callable[[], None]) -> None:
		super().__init__(master, bg="#0b1f3a")
		self.on_back = on_back
		self._build_layout()

	def _build_layout(self) -> None:
		"""Create the project information view."""
		tk.Label(
			self,
			text="ABOUT THE PROJECT",
			font=("Segoe UI", 22, "bold"),
			fg="#f4f7fb",
			bg="#0b1f3a",
		).pack(anchor="w", padx=42, pady=(42, 8))
		tk.Label(
			self,
			text="Flight Route Planner",
			font=("Segoe UI", 16, "bold"),
			fg="#56a0ff",
			bg="#0b1f3a",
		).pack(anchor="w", padx=42, pady=(18, 4))

		details = (
			"Subject: Design and Analysis of Algorithms\n\n"
			"Purpose:\n"
			"To demonstrate how graph algorithms can be applied to flight route planning.\n\n"
			"Main Concepts:\n"
			"Graph representation\n"
			"Breadth-First Search (BFS)\n"
			"Depth-First Search (DFS)\n"
			"Dijkstra's shortest-path algorithm\n"
			"Priority queues\n"
			"Time and space complexity\n"
			"Empirical performance analysis\n\n"
			"Algorithm Analysis:\n"
			"BFS: Time O(V + E), Space O(V)\n"
			"DFS: Time O(V + E), Space O(V)\n"
			"Dijkstra: Time O((V + E) log V), Space O(V + E)\n\n"
			"Best, average, and worst cases depend on graph connectivity and\n"
			"whether the destination is reached before the full graph is explored."
		)
		tk.Label(
			self,
			text=details,
			justify="left",
			anchor="nw",
			font=("Segoe UI", 12),
			fg="#f4f7fb",
			bg="#132d4f",
			padx=24,
			pady=24,
		).pack(fill="x", padx=42, pady=24)
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
		).pack(pady=(8, 28))
