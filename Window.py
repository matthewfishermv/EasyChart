from tkinter import *


class Window(Toplevel):

	def __init__(self, controller, title, width, height, force_focus = False):
		"""Creates a new window.

		Args:
			controller: The MainWindow that controls the application.
			title: The text to display in the title bar.
			width: The width (pixels) of the Window.
			height: The height (pixels) of the Window.
			force_focus: True if window must be destroyed before application continues, False otherwise. Default is False.
		"""
		
		Toplevel.__init__(self, width = width, height = height)
		self.set_title(title)
		
		# Force focus if configured to do so
		if force_focus: self.force_focus()

		self.mainloop()

	def set_title(self, new_title):
		"""Sets the window title to new_title.

		Args:
			new_title: The new title to set.
		"""

		self.title(new_title)

	def force_focus(self):
		"""Forces the focus to this window.
		Renders other windows unusable until it is closed.
		"""

		self.lift()
		self.focus_force()
		self.attributes("-topmost", True)
		self.grab_set()