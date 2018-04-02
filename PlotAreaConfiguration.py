from tkinter import *


class PlotAreaConfiguration(object):

	def __init__(self, plot_width, plot_height, buffer_size):
		"""Creates a new set of configurations for the plot area."""
		
		self.title = 'New Chart'
		self.plot_width = plot_width
		self.plot_height = plot_height
		self.buffer_top = buffer_size
		self.buffer_right = buffer_size
		self.buffer_bottom = buffer_size
		self.buffer_left = buffer_size

	# Getter functions
	def get_title(self): return self.title
	def get_plot_width(self): return self.plot_width
	def get_plot_height(self): return self.plot_height
	def get_buffer_top(self): return self.buffer_top
	def get_buffer_right(self): return self.buffer_right
	def get_buffer_bottom(self): return self.buffer_bottom
	def get_buffer_left(self): return self.buffer_left
	def get_chart_width(self): return (self.plot_width - (self.buffer_left + self.buffer_right))
	def get_chart_height(self): return (self.plot_height - (self.buffer_top + self.buffer_bottom))

	# Setter functions
	def set_title(self, title): self.title = title
	def set_plot_width(self, plot_width): self.plot_width = plot_width
	def set_plot_height(self, plot_height): self.plot_height = plot_height
	def set_buffer_top(self, size): self.buffer_top = size
	def set_buffer_right(self, size): self.buffer_right = size
	def set_buffer_bottom(self, size): self.buffer_bottom = size
	def set_buffer_left(self, size): self.buffer_left = size

	def set_buffer_size(self, buffer_size):
		"""Sets the buffer size on all sides to buffer_size."""

		self.buffer_top = buffer_size
		self.buffer_right = buffer_size
		self.buffer_bottom = buffer_size
		self.buffer_left = buffer_size

	def __str__(self):
		print("--------PLOT AREA CONFIGURATION--------")
		print("plot_width: " + str(self.plot_width))
		print("plot_height: " + str(self.plot_height))
		print("buffer_size: " + str(self.buffer_size))
		print("---------------------------------------")

		return ''