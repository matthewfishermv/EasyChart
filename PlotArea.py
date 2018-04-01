from tkinter import *


class PlotArea():

	def __init__(self, frame, width = 400, height = 400):
		self.width = width
		self.height = height
		self.canvas = Canvas(frame, width = self.width, height = self.height, bg ='white')
		self.canvas.pack()

	def get_width(self):
		return self.width

	def get_height(self):
		return self.height

	def draw_line(self, x1, y1, x2, y2):
		self.canvas.create_line(x1, y1, x2, y2)

	def draw_rectangle(self, x1, y1, x2, y2):
		self.canvas.create_rectangle(x1, y1, x2, y2)