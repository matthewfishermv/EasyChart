from tkinter import *


class PlotArea():

	def __init__(self, frame, width, height):
		"""Creates a new PlotArea object.

		Args:
			frame: The MainWindow, to which the PlotArea belongs.
			width: The total usable width (pixels) for drawing.
			height: The total usable height (pixels) for drawing.
		"""

		self.canvas = Canvas(frame, width = width, height = height, bg ='white')
		self.canvas.pack()

	def draw_line(self, x1, y1, x2, y2, stroke_weight = 1, stroke_color = 'black'):
		"""Draws a line on the PlotArea.

		The resultant line extends from (x1, y1) to (x2, y2) on the PlotArea.

		Args:
			x1: The x-coordinate of the first corner (x1, y1).
			y1: The y-coordinate of the first corner (x1, y1).
			x2: The x-coordinate of the second corner (x2, y2).
			y2: The y-coordinate of the second corner (x2, y2).
			stroke_weight: The thickness of the line. Default is 1.
			stroke_color: The color of the line. Can be a color name like 'light blue' or a hex string. Deafult is 'black'.
		"""

		self.canvas.create_line(x1, y1, x2, y2, width = stroke_weight, fill = stroke_color)

	def draw_rectangle(self, x1, y1, x2, y2, stroke_weight = 1, stroke_color = '#88aae0', fill_color = '#bccce5'):
		"""Draws a rectangle bounded by (x1, y1) and (x2, y2) on the PlotArea.

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

	def draw_text(self, x, y, message, font = ('Helvetica', 12)):
		"""Draw text at the coordinates (x, y).

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
		"""Forces the plot area to resize to the width w and height h.

		This method should be used to size the PlotArea to the associated PlotAreaConfiguration.

		Args:
			w: The new width (pixels).
			h: The new height (pixels).
		"""
		
		self.canvas.config(width = w, height = h)