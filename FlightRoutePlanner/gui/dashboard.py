"""Main dashboard window for the Flight Route Planner."""

from __future__ import annotations

import tkinter as tk
from typing import Callable, Dict


NAVY = "#0b1f3a"
CARD = "#132d4f"
ACCENT = "#2f80ed"
TEXT = "#f4f7fb"
MUTED = "#b8c7d9"


class Dashboard(tk.Frame):
	"""Dashboard containing the application's main navigation buttons."""

	def __init__(self, master: tk.Misc, on_navigate: Callable[[str], None]) -> None:
		super().__init__(master, bg=NAVY)
		self.on_navigate = on_navigate
		self._build_layout()

	def _build_layout(self) -> None:
		"""Create the dashboard title, summary, and navigation cards."""
		self.pack(fill="both", expand=True)
		self.grid_columnconfigure(0, weight=1)
		self.grid_columnconfigure(1, weight=1)

		header = tk.Frame(self, bg=NAVY)
		header.grid(row=0, column=0, columnspan=2, padx=48, pady=(42, 28), sticky="ew")

		tk.Label(
			header,
			text="FLIGHT ROUTE PLANNER",
			font=("Segoe UI", 26, "bold"),
			fg=TEXT,
			bg=NAVY,
		).pack(anchor="w")
		tk.Label(
			header,
			text="Design and Analysis of Algorithms Mini Project",
			font=("Segoe UI", 12),
			fg=MUTED,
			bg=NAVY,
		).pack(anchor="w", pady=(8, 0))

		cards: Dict[str, str] = {
			"shortest_route": "Find Shortest Route",
			"traversal": "BFS / DFS Traversal",
			"network": "View Airport Network",
			"comparison": "Algorithm Comparison",
			"about": "About Project",
		}

		for index, (page_name, label) in enumerate(cards.items()):
			row, column = divmod(index, 2)
			card = tk.Frame(self, bg=CARD, padx=20, pady=18)
			card.grid(
				row=row + 1,
				column=column,
				padx=(48 if column == 0 else 12, 48 if column == 1 else 12),
				pady=10,
				sticky="ew",
			)
			self.grid_rowconfigure(row + 1, weight=1)
			tk.Button(
				card,
				text=label,
				command=lambda page=page_name: self.on_navigate(page),
				font=("Segoe UI", 12, "bold"),
				bg=ACCENT,
				fg=TEXT,
				activebackground="#56a0ff",
				activeforeground=TEXT,
				relief="flat",
				cursor="hand2",
				padx=16,
				pady=12,
				width=22,
			).pack(fill="x")

		exit_button = tk.Button(
			self,
			text="Exit",
			command=self.master.destroy,
			font=("Segoe UI", 11, "bold"),
			bg="#263b55",
			fg=TEXT,
			activebackground="#3b5573",
			activeforeground=TEXT,
			relief="flat",
			cursor="hand2",
			padx=16,
			pady=8,
		)
		exit_button.grid(row=4, column=0, columnspan=2, pady=(24, 34))
