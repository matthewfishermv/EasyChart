from tkinter import *
from PlotArea import *
from PlotAreaConfiguration import *
from PlotConfigurationWindow import *
from Chart import *


class MainWindow(Tk):

	def __init__(self):
		"""Creates a new EasyChart application instance."""

		Tk.__init__(self)

		self.title("EasyChart")

		# Set default configuration values
		self.default_width = 800
		self.default_height = 400
		self.default_buffer_size = 50

		# Initialize object variables
		self.toolbar = self.init_toolbar()
		self.main_frame = Frame(self)
		self.main_frame.pack()
		self.plot_area = self.init_plot_area()
		self.plot_area_configuration = self.init_plot_area_config()
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
		self.edit_menu.add_command(label = 'Settings', command = self.change_settings)

		self.mainloop()

	def init_menu(self):
		"""Creates a new menu with all sub-menus."""

		# Create a new menu in the main window
		new_menu = Menu(self)

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
		button_rand_column = Button(toolbar, text = "Generate Chart", command = lambda: self.draw_new_chart('column'))
		button_rand_column.pack(side = LEFT, padx = 10, pady = 10)

		button_clear = Button(toolbar, text = "Clear Chart", command = self.clear_plot_area)
		button_clear.pack(side = LEFT, padx = 10, pady = 10)

		button_clear = Button(toolbar, text = "Change Settings", command = self.change_settings)
		button_clear.pack(side = LEFT, padx = 10, pady = 10)

		return toolbar

	def init_plot_area(self):
		"""Creates the plot area, where charts are plotted.

		Returns:
			PlotArea: The new PlotArea.
		"""

		# Create plot area
		plot_area = PlotArea(self, width = self.default_width, height = self.default_height)

		return plot_area

	def init_plot_area_config(self):
		"""Initializes the plot area configuration object."""

		plot_area_configuration = PlotAreaConfiguration(plot_width = self.default_width, plot_height = self.default_height, buffer_size = self.default_buffer_size)

		return plot_area_configuration

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
		#self.plot_area.draw_chart()

		self.clear_plot_area()
		chart = Chart(self.plot_area, self.plot_area_configuration)

		self.set_status_label('New chart drawn.')
		

	def clear_plot_area(self):
		"""Clears the plot area of any graphics."""
		
		self.plot_area.clear()
		self.set_status_label('Plot area cleared.')

	def change_settings(self):
		PlotConfigurationWindow(self)
		self.draw_new_chart()