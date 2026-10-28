"""Application entry point for the Flight Route Planner."""

from __future__ import annotations

import tkinter as tk

from gui.about import AboutPage
from gui.comparison import ComparisonPage
from gui.dashboard import Dashboard, NAVY
from gui.shortest_route import ShortestRoutePage
from gui.traversal import TraversalPage
from airport_data import build_sample_graph
from algorithms import dijkstra
from visualization import show_network


class FlightRoutePlannerApp:
	"""Manage the main window and navigation between GUI pages."""

	def __init__(self, root: tk.Tk) -> None:
		self.root = root
		self.root.title("Flight Route Planner")
		self.root.geometry("980x700")
		self.root.minsize(820, 600)
		self.root.configure(bg=NAVY)
		self.current_page: tk.Frame | None = None
		self.show_dashboard()

	def clear_page(self) -> None:
		"""Remove the currently displayed page."""
		if self.current_page is not None:
			self.current_page.destroy()
			self.current_page = None

	def show_dashboard(self) -> None:
		"""Display the main dashboard."""
		self.clear_page()
		self.current_page = Dashboard(self.root, self.show_page)

	def show_page(self, page_name: str) -> None:
		"""Display a page selected from the dashboard."""
		if page_name == "network":
			graph = build_sample_graph()
			result = dijkstra(graph, "Delhi", "Bengaluru")
			show_network(graph, self.root, result["path"])
			return

		page_classes = {
			"shortest_route": ShortestRoutePage,
			"traversal": TraversalPage,
			"comparison": ComparisonPage,
			"about": AboutPage,
		}
		page_class = page_classes.get(page_name)
		if page_class is None:
			return

		self.clear_page()
		self.current_page = page_class(self.root, self.show_dashboard)
		self.current_page.pack(fill="both", expand=True)


def main() -> None:
	"""Start the Tkinter application."""
	root = tk.Tk()
	FlightRoutePlannerApp(root)
	root.mainloop()


if __name__ == "__main__":
	main()
