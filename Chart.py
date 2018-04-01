from tkinter import *
from random import *
from PlotArea import *


class Chart(object):

	def __init__(self, plot_area, type = 'column', num_values = 10, low = 0, high = 100):
		self.low = low
		self. high = high
		self.width = (num_values / plot_area.get_width())

		values = self.get_random_values(num_values = num_values)

	def get_random_values(self, num_values):
		values = []

		for x in range(num_values):
			values.append(randint(self.low, self.high))

		return values