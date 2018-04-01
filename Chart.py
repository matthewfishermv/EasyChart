from tkinter import *
from random import *


class Chart(object):

	DEBUG_LEVEL = 0	# 0, 1, 2, or 3

	def __init__(self, plot_area, configuration, type = 'column', num_values = 10, low_value = 0, high_value = 100):
		"""Creates a new chart object.

		Args:
			plot_area: The plot area, on which the chart will be drawn (PlotArea object).
			type: The type of chart to draw. Types: 'column'.
			num_values: The number of data points to plot.
			low_value: The lowest value in the data set (min).
			high_value: The highest value in the data set (max).
			buffer_size: The number of pixels of padding to add around the entire chart.
		"""

		# DEBUG
		if self.DEBUG_LEVEL >= 1:
			print("--------CHART--------")

		# Set class variables
		self.plot_area = plot_area
		self.configuration = configuration
		self.low_value = low_value
		self.high_value = high_value
		self.x_width = self.configuration.get_chart_width() / num_values

		## DEBUG
		if self.DEBUG_LEVEL >= 1:
			# Print vairable values
			print("low and high values: ", str(self.low_value) + ", " + str(self.high_value))
			print("chart_width: " + str(self.configuration.get_chart_width()))
			print("chart_height: " + str(self.configuration.get_chart_height()))
			print("x_width: " + str(self.x_width))
		if self.DEBUG_LEVEL >= 3:
			# Draw plot area bounding box
			bounds_x_start = self.configuration.get_buffer_size()
			bounds_y_start = self.configuration.get_buffer_size()
			bounds_x_end = bounds_x_start + self.configuration.get_chart_width()
			bounds_y_end = bounds_y_start + self.configuration.get_chart_height()

			self.plot_area.draw_rectangle(bounds_x_start, bounds_y_start, bounds_x_end, bounds_y_end,
				fill_color ='', stroke_color = 'red')

		# Create a list of random values within parameters
		values = self.get_random_values(num_values)
		self.plot_values(values)

		# Draw axes
		self.draw_axes()

		# DEBUG
		if self.DEBUG_LEVEL >= 1:
			print("----------------")

	def get_random_values(self, num_values):
		"""Produces a list a randomly-generated values that fall within the parameters of the Chart.

		Args:
			num_values: The number of random values to generate.
		Returns:
			List: The list of randomly-generated values.
		"""

		values = []

		# Add random values between low_value and high_value
		for x in range(num_values):
			values.append(randint(self.low_value, self.high_value))

		return values

	def plot_values(self, values):
		"""Plots the values graphically on the PlotArea.

		Args:
			values: The list of values to plot.

		"""

		x_index = 0

		largest = max(values)

		# Plot values
		for value in values:
			# Set bounds of current value
			x_start = self.configuration.get_buffer_size() + (self.x_width * x_index)
			x_end = x_start + self.x_width
			y_start = self.configuration.get_chart_height() + self.configuration.get_buffer_size()
			y_end = y_start - ((value / largest) * (self.configuration.get_chart_height()))

			# Draw column and value label
			self.plot_area.draw_rectangle(x_start, y_start, x_end, y_end, stroke_weight = 2)
			self.plot_area.draw_text(x_start + (self.x_width / 2), y_start + 30, value)

			x_index += 1

			## DEBUG
			if self.DEBUG_LEVEL >= 3:
				print (str(value) + ": " + str([x_start, y_start, x_end, y_end]))

	def draw_axes(self, padding = 10, stroke_weight = 2):
		"""Draws the x- and y-axis on the PlotArea.

		Args:
			padding: The number of pixels between plot area and axes.
			stroke_weight: The thickness of the axis lines.
		"""
		
		# Origin coordinates
		origin_x = self.configuration.get_buffer_size() - padding
		origin_y = self.configuration.get_chart_height() + self.configuration.get_buffer_size() + padding

		# Draw y-axis
		top_y = self.configuration.get_buffer_size() - padding
		self.plot_area.draw_line(origin_x, origin_y, origin_x, top_y, stroke_weight = stroke_weight)

		# Draw x-axis
		right_x = self.configuration.get_buffer_size() + self.configuration.get_chart_width() + padding
		self.plot_area.draw_line(origin_x, origin_y, right_x, origin_y, stroke_weight = stroke_weight)
