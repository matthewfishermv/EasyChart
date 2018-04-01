from tkinter import *
from PlotArea import *
from Chart import *


class EasyChart(Frame):

	def __init__(self, master):
		"""Creates a new EasyChart application instance.

		Args:
			master: The main window (Tk object).

		"""

		Frame.__init__(self)
		self.pack()

		master.title("EasyChart 2.0")

		self.toolbar = self.init_toolbar()
		self.main_frame = Frame(self)
		self.main_frame.pack()
		self.plot_area = self.init_plot_area()
		self.status_bar = self.init_status_bar()
		self.status_label = self.init_status_label()

		# Initialize menus
		self.main_menu = Menu(master)
		master.config(menu = self.main_menu)

		self.file_menu = Menu(self.main_menu)
		self.main_menu.add_cascade(label = 'File', menu = self.file_menu)
		self.file_menu.add_command(label = 'Generate Chart', command = self.draw_chart)
		self.file_menu.add_separator()
		self.file_menu.add_command(label = 'Exit', command = quit)

		# Create chart
		self.current_chart = self.plot_area.add_chart()

	def init_menu(self):
		"""Creates a new menu with all sub-menus."""

		# Create a new menu in the main window
		new_menu = Menu(master)

		# File menu
		file_menu = Menu(new_menu)
		new_menu.add_cascasde(label = "File", menu = file_menu)
		file_menu.add_command(label = "New")

		return new_menu

	def init_toolbar(self):
		"""Creates a new frame at top of main window with toolbar items.

		Returns:
			Frame: The new toolbar with tools included.
		"""

		toolbar = Frame(self, bg = '#88ade8')
		toolbar.pack(fill = X)

		# Buttons
		button_rand_column = Button(toolbar, text = "Generate Chart", command = lambda: self.draw_chart('column'))
		button_rand_column.pack(side = LEFT, padx = 10, pady = 10)

		button_clear = Button(toolbar, text = "Clear", command = self.clear)
		button_clear.pack(side = LEFT, padx = 10, pady = 10)

		return toolbar

	def init_plot_area(self):
		"""Creates the plot area, where charts are plotted.

		Returns:
			PlotArea: The new PlotArea.
		"""

		# Create plot area
		plot_area = PlotArea(self, width = 500, height = 300)

		return plot_area

	def init_status_bar(self):
		"""Creates the status bar at the bottom of the main window.

		Returns:
			Frame: The new status bar.
		"""

		# Create a new frame at bottom of main window for status
		status_bar = Frame(self)
		status_bar.pack(side = BOTTOM, fill = X)

		return status_bar

	def init_status_label(self, label_text = 'The application is running.'):
		"""Creates and adds the label, on which status bar text appears.

		Args:
			label_text: The text that displays in the status bar.
		Returns:
			Label: The new label.
		"""

		# Create new status label
		status_label = Label(self.status_bar, text = label_text, bd = 1, relief = SUNKEN, anchor = W)
		status_label.pack(fill = X)

		return status_label

	def draw_chart(self, type = 'column'):
		"""Creates a new chart on the plot area.

		Args:
			type: The type of chart to draw. Types: 'column'.
		"""

		self.plot_area.clear()
		self.current_chart = Chart(self.plot_area)

	def clear(self):
		"""Clears the plot area of any graphics."""
		
		self.plot_area.clear()


if __name__ == "__main__":
	root = Tk()
	app = EasyChart(root)
	root.mainloop()