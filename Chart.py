from tkinter import *
from random import *
from PlotArea import *


class Chart(object):

	def __init__(self, plot_area, type = 'column', num_values = 10, low_value = 0, high_value = 100, buffer_size = 20):
		self.DEBUG_LEVEL = 3	# 0, 1, 2, or 3

		# DEBUG
		if self.DEBUG_LEVEL >= 1:
			print("--------New Chart--------")

		# Set class variables
		self.plot_area = plot_area
		self.low_value = low_value
		self.high_value = high_value
		self.buffer_size = buffer_size
		self.plot_width = plot_area.get_width() - (self.buffer_size * 2)
		self.plot_height = plot_area.get_height() - (self.buffer_size * 2)
		self.x_width = self.plot_width / num_values

		# Create a list of random values within parameters
		values = self.get_random_values(num_values)
		self.plot_values(values)

		## DEBUG
		if (self.DEBUG_LEVEL >= 1):
			print("low and high values: ", str(self.low_value) + ", " + str(self.high_value))
			print("plot_width: " + str(self.plot_width))
			print("plot_height: " + str(self.plot_height))
			print("x_width: " + str(self.x_width))

	def get_random_values(self, num_values):
		values = []

		for x in range(num_values):
			values.append(randint(self.low_value, self.high_value))

		return values

	def plot_values(self, values):
		x_index = 0

		largest = max(values)

		# Plot values
		for value in values:
			# Set bounds of current value
			x_start = self.buffer_size + (self.x_width * x_index)
			x_end = x_start + self.x_width
			y_start = self.plot_height + self.buffer_size
			y_end = y_start - ((value / largest) * (self.plot_height))

			# Draw column and value label
			self.plot_area.draw_rectangle(x_start, y_start, x_end, y_end)
			self.plot_area.add_text(x_start + (self.x_width / 2), y_start + 10, value)

			x_index += 1

			## DEBUG
			if (self.DEBUG_LEVEL >= 3):
				print (str(value) + ": " + str([x_start, y_start, x_end, y_end]))