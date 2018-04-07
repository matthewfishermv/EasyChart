from tkinter import *
from PlotArea import *
from PlotConfiguration import *
from PlotConfigurationWindow import *
from Chart import *


class MainWindow(Tk):

	def __init__(self):
		"""Creates the MainWindow for the EasyChart application.
	
		The MainWindow controls all of its component areas (e.g. menus, plot area) and most windows that are created
		in the course of running the application.

		When needed, the MainWindow delegates control to other parts of the application.
		"""

		Tk.__init__(self)

		self.title("EasyChart")
		self.resizable(False, False)

		# Set default configuration values
		self.default_width = 600
		self.default_height = 400
		self.default_margin_size = 50

		# Initialize object variables
		#self.toolbar = self.init_toolbar()
		self.main_frame = Frame(self)
		self.main_frame.pack()
		self.plot_area = self.init_plot_area()
		self.plot_configuration = self.init_plot_config()
		self.status_bar = self.init_status_bar()
		self.status_label = self.init_status_label()
		self.chart = self.draw_new_chart()

		# Initialize menus
		self.main_menu = Menu(self)
		self.config(menu = self.main_menu)

		self.file_menu = Menu(self.main_menu)
		self.main_menu.add_cascade(label = 'File', menu = self.file_menu)
		self.file_menu.add_command(label = 'Generate Chart', command = self.draw_new_chart)
		self.file_menu.add_command(label = 'Clear Chart', command = self.clear_plot_area)
		self.file_menu.add_separator()
		self.file_menu.add_command(label = 'Exit', command = quit)		

		self.edit_menu = Menu(self.main_menu)
		self.main_menu.add_cascade(label = 'Edit', menu = self.edit_menu)
		self.edit_menu.add_command(label = 'Plot Settings', command = self.change_plot_settings)

		self.view_menu = Menu(self.main_menu)
		self.main_menu.add_cascade(label = 'View', menu = self.view_menu)
		self.view_menu.add_command(label = 'Full Screen', command = self.toggle_full_screen)

		self.mainloop()

	def init_toolbar(self):
		"""Creates a new frame at top of main window with toolbar items.

		Returns:
			tkinter.Frame: The new toolbar with tools included.
		"""

		toolbar = Frame(self, bg = '#88ade8')
		toolbar.pack(fill = X)

		# Buttons
		button_rand_column = Button(toolbar, text = "Generate Chart", command = lambda: self.draw_new_chart('column'))
		button_rand_column.pack(side = LEFT, padx = 10, pady = 10)

		button_clear = Button(toolbar, text = "Clear Chart", command = self.clear_plot_area)
		button_clear.pack(side = LEFT, padx = 10, pady = 10)

		button_clear = Button(toolbar, text = "Change Plot Settings", command = self.change_plot_settings)
		button_clear.pack(side = LEFT, padx = 10, pady = 10)

		return toolbar

	def init_plot_area(self):
		"""Creates the plot area, where charts are drawn.

		Returns:
			PlotArea: The new PlotArea.
		"""

		plot_area = PlotArea(self, width = self.default_width, height = self.default_height)

		return plot_area

	def init_plot_config(self):
		"""Initializes the plot configuration object.

		Returns:
			PlotArea: The new plot configuration object.
		"""

		plot_configuration = PlotConfiguration(plot_width = self.default_width, plot_height = self.default_height, margin_size = self.default_margin_size)

		return plot_configuration

	def init_status_bar(self):
		"""Creates the status bar at the bottom of the main window.

		Returns:
			tkinter.Frame: The new status bar.
		"""
		
		status_bar = Frame(self)
		status_bar.pack(side = BOTTOM, fill = X)

		return status_bar

	def init_status_label(self, label_text = 'The application is running.'):
		"""Creates the label, on which status bar text appears; adds the label to the status bar.

		Args:
			label_text: The text that displays in the status bar.
		Returns:
			Label: The new label.
		"""

		# Create new status label
		status_label = Label(self.status_bar, text = label_text, bd = 1, relief = SUNKEN, anchor = W)
		status_label.pack(fill = X)

		return status_label

	def set_status_label(self, label_text = 'The application is running.'):
		"""Sets the status label to label_text.

		Args:
			The message to display on the status bar.
		"""

		self.status_label['text'] = label_text

	def draw_new_chart(self, type = 'column'):
		"""Delegates drawing of a new chart to self.plot_area.

		Args:
			type: The type of chart to draw. Types: 'column'.
		"""

		self.clear_plot_area()
		chart = Chart(self.plot_area, self.plot_configuration)

		self.set_status_label('New chart drawn.')
		

	def clear_plot_area(self):
		"""Clears the plot area of all graphics."""
		
		self.plot_area.clear()
		self.set_status_label('Plot area cleared.')

	def change_plot_settings(self):
		"""Launches the plot configuration window to allow user configure plot settings."""

		PlotConfigurationWindow(self, self.plot_configuration, 'Plot Settings', 0, 0)
		self.draw_new_chart()

	def toggle_full_screen(self):
		"""Toggles between fullscreen and windowed mode."""

		self.attributes('-fullscreen', not self.attributes('-fullscreen'))