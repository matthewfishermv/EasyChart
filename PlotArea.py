from tkinter import *


class PlotArea():

	def __init__(self, frame, width, height):
		"""Creates a new PlotArea object.

		Args:
			frame: The main window, to which the plot area belongs.
			width: The total usable width of the plot area.
			height: The total usable height of the plot area.
		"""

		self.canvas = Canvas(frame, width = width, height = height, bg ='white')
		self.canvas.pack()

	def set_width(self, width):
		self.width = width;

	def get_width(self):
		"""Returns the width of the plot area."""

		return self.width

	def get_height(self):
		"""Returns the height of the plot area."""

		return self.height

	def draw_line(self, x1, y1, x2, y2, stroke_weight = 1, stroke_color = 'black'):
		"""Draws a line on the plot area.

		Args:
			x1: The x-coordinate for the first corner (x1, y1).
			y1: The y-coordinate for the first corner (x1, y1).
			x2: The x-coordinate for the second corner (x2, y2).
			y2: The y-coordinate for the second corner (x2, y2).
			stroke_weight: The thickness of the line. Default is 1.
			stroke_color: The color of the line. Can be a color name like 'light blue' or a hex string. Deafult is 'black'.
		"""

		self.canvas.create_line(x1, y1, x2, y2, width = stroke_weight, fill = stroke_color)

	def draw_rectangle(self, x1, y1, x2, y2, stroke_weight = 1, stroke_color = '#88aae0', fill_color = '#bccce5'):
		"""Draws a rectangle bounded by (x1, y1) and (x2, y2).

		Args:
			x1: The x-coordinate for the first corner (x1, y1).
			y1: The y-coordinate for the first corner (x1, y1).
			x2: The x-coordinate for the second corner (x2, y2).
			y2: The y-coordinate for the second corner (x2, y2).
			stroke_weight: The thickness of the ouline. Default is 1.
			stroke_color: The color of the outline. Can be a color name like 'light blue' or a hex string. Deafult is '#88aae0'.
			fill_color: The color of the inside of the rectangle. Default is '#bccce5'.
		"""

		self.canvas.create_rectangle(x1, y1, x2, y2, fill = fill_color, outline = stroke_color, width = stroke_weight)

	def draw_text(self, x, y, message, font = ("Helvetica", 12)):
		"""Draw text at the given coordinates (x,y).

		Args:
			x: The x-coordinate of the text (x, y).
			y: The y-coordinate of the text (x, y).
			message: The string of text to add at (x, y).
			font: The font, with which to draw the text, e.g. ("Helvetica", 12).
		"""

		self.canvas.create_text(x, y, text = message, font = font)

	def clear(self):
		"""Clears the plot area of all elements."""

		self.canvas.delete(ALL)

	def resize(self, w, h):
		"""Forces the plot area to resize to the current configuration."""
		
		self.canvas.config(width = w, height = h)