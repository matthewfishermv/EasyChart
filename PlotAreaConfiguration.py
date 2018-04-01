from tkinter import *


class PlotAreaConfiguration(object):

	def __init__(self, plot_width, plot_height, buffer_size):
		self.plot_width = plot_width
		self.plot_height = plot_height
		self.buffer_size = buffer_size

	# Getter functions
	def get_plot_width(self): return self.plot_width
	def get_plot_height(self): return self.plot_height
	def get_buffer_size(self): return self.buffer_size
	def get_chart_width(self): return (self.plot_width - (2 * self.buffer_size))
	def get_chart_height(self): return (self.plot_height - (2 * self.buffer_size))

	# Setter functions
	def set_plot_width(self, plot_width): self.plot_width = plot_width
	def set_plot_height(self, plot_height): self.plot_height = plot_height
	def set_buffer_size(self, buffer_size): self.buffer_size = buffer_size

	def __str__(self):
		print("--------PLOT AREA CONFIGURATION--------")
		print("plot_width: " + str(self.plot_width))
		print("plot_height: " + str(self.plot_height))
		print("buffer_size: " + str(self.buffer_size))
		print("---------------------------------------")

		return ''