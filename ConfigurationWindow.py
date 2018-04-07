from Window import *


class ConfigurationWindow(Window):

	def __init__(self, controller, target_configuration, title, width, height, force_focus = True):
		"""Creates a new ConfigurationWindow.

		Args:
			controller: The MainWindow that controls the application.
			target_configuration: The Configuration that is changed by changing settings in this ConfigurationWindow.
			title: The text to display in the title bar.
			width: The width of the ConfigurationWindow.
			height: The height (pixels) of the ConfigurationWindow.
			force_focus: True if window must be destroyed before application continues, False otherwise. Default is False.
		"""

		Window.__init__(self, controller, title, width, height, force_focus)

	def validate(self):
		"""Validates the user-supplied data.

		Returns:
			True if all entries are valid.
			False if at least one entry is invalid.
		"""
		pass