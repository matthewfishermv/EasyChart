from tkinter import *
from Configuration import *


class PlotConfiguration(Configuration):

	def __init__(self, plot_width, plot_height, margin_size):
		"""Creates a new set of configuration properties for the plot area.

		Args:
			plot_width: The width (pixels) of the plot area.
			plot_height: The height (pixels) of the plot area.
			margin_size: The margin size (pixels) to add between chart boundaries and plot area boundaries on all sides.
		"""

		self.properties = {'title': 'Sample Chart',
								'plot_width': plot_width,
								'plot_height': plot_height,
								'chart_height': (plot_height - (margin_size * 2)),
								'chart_width': (plot_width - (margin_size * 2)),
								'margin_top': margin_size,
								'margin_right': margin_size,
								'margin_bottom': margin_size,
								'margin_left': margin_size,
								'show_title': True
							}

	def set_property(self, property, value, override = False):
		"""Sets property to value.

		Assumes property name references a valid property.
		Assumes every property has a unique property name.

		Returns:
			True if property has been changed.
			False if no change was made or an error was encountered.
		"""

		# Forbidden cases
		if property in ['chart_width', 'chart_height'] and not override:
			return None

		# Special cases
		if property == 'plot_width':
			new_chart_width = self.calculate_chart_width(value, self.properties['margin_left'], self.properties['margin_right'])
			self.set_property('chart_width', new_chart_width, override = True)

		if property == 'plot_height':
			new_chart_height = self.calculate_chart_height(value, self.properties['margin_top'], self.properties['margin_bottom'])
			self.set_property('chart_height', new_chart_height, override = True)

		if property == 'margin_top':
			new_chart_height = self.calculate_chart_height(self.properties['plot_height'], value, self.properties['margin_bottom'])
			self.set_property('chart_height', new_chart_height, override = True)

		if property == 'margin_right':
			new_chart_width = self.calculate_chart_width(self.properties['plot_width'], self.properties['margin_left'], value)
			self.set_property('chart_width', new_chart_width, override = True)

		if property == 'margin_bottom':
			new_chart_height = self.calculate_chart_height(self.properties['plot_height'], self.properties['margin_top'], value)
			self.set_property('chart_height', new_chart_height, override = True)

		if property == 'margin_left':
			new_chart_width = self.calculate_chart_width(self.properties['plot_width'], value, self.properties['margin_right'])
			self.set_property('chart_width', new_chart_width, override = True)

		# Allowed cases (including special cases)
		return Configuration.set_property(self, property, value)

	# Helper functions
	def calculate_chart_width(self, plot_width, margin_left, margin_right):
		"""Calculates the chart width, taking plot width and margins into account.

		Returns:
			Integer: The chart width (pixels).
		"""

		return plot_width - (margin_left + margin_right)

	def calculate_chart_height(self, plot_height, margin_top, margin_bottom):
		"""Calculates the chart height, taking plot height and margins into account.

		Returns:
			Integer: The chart height (pixels).
		"""

		return plot_height - (margin_top + margin_bottom)