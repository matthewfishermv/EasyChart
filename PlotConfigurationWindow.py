from tkinter import *
import tkinter.messagebox
from ConfigurationWindow import *


class PlotConfigurationWindow(ConfigurationWindow):

	def __init__(self, controller):
		"""Creates a plot configuration window, where the user can change plot settings.

		Args:
			controller: The MainWindow that controls the application.
		"""

		Toplevel.__init__(self)

		self.controller = controller
		self.title("Plot Settings")

		# Display on/off toggle variables
		self.show_title = BooleanVar()
		if self.controller.plot_configuration.get_property('show_title') == True: self.show_title.set(True)
		else: self.show_title.set(False)

		# Get focus
		self.lift()
		self.focus_force()
		self.attributes("-topmost", True)
		self.grab_set()

		# Chart title
		self.title_label = Label(self, text = "Title:")
		self.title_label.grid(row = 0, column = 0)

		self.title_checkbox = Checkbutton(self, text = "Display", var = self.show_title, onvalue = True, offvalue = False)
		if self.show_title.get(): self.title_checkbox.select()
		self.title_checkbox.grid(row = 0, column = 1)

		self.title_field = Entry(self)
		self.title_field.insert(0, self.controller.plot_configuration.get_property('title'))
		self.title_field.grid(row = 0, column = 2)

		# Plot width
		self.plot_width_label = Label(self, text = "Plot Width (200 - 1000):")
		self.plot_width_label.grid(row = 1, column = 0)
		self.plot_width_field = Entry(self)
		self.plot_width_field.insert(0, self.controller.plot_configuration.get_property('plot_width'))
		self.plot_width_field.grid(row = 1, column = 2)

		# Plot height
		self.plot_height_label = Label(self, text = "Plot Height (200 - 1000):")
		self.plot_height_label.grid(row = 2, column = 0)
		self.plot_height_field = Entry(self)
		self.plot_height_field.insert(0, self.controller.plot_configuration.get_property('plot_height'))
		self.plot_height_field.grid(row = 2, column = 2)

		# Margin top
		self.margin_top_label = Label(self, text = "Top Margin (15 - 200):")
		self.margin_top_label.grid(row = 3, column = 0)
		self.margin_top_field = Entry(self)
		self.margin_top_field.insert(0, self.controller.plot_configuration.get_property('margin_top'))
		self.margin_top_field.grid(row = 3, column = 2)

		# Margin left and right
		self.margin_left_label = Label(self, text = "Left and Right Margins (15 - 200):")
		self.margin_left_label.grid(row = 4, column = 0)
		self.margin_left_field = Entry(self)
		self.margin_left_field.insert(0, self.controller.plot_configuration.get_property('margin_left'))
		self.margin_left_field.grid(row = 4, column = 1)
		self.margin_right_field = Entry(self)
		self.margin_right_field.insert(0, self.controller.plot_configuration.get_property('margin_right'))
		self.margin_right_field.grid(row = 4, column = 3)

		# Margin bottom
		self.margin_bottom_label = Label(self, text = "Bottom Margin (15 - 200):")
		self.margin_bottom_label.grid(row = 5, column = 0)
		self.margin_bottom_field = Entry(self)
		self.margin_bottom_field.insert(0, self.controller.plot_configuration.get_property('margin_bottom'))
		self.margin_bottom_field.grid(row = 5, column = 2)

		# Save and cancel buttons
		save_button = Button(self, text = "Save and Update", command = self.validate)
		save_button.grid(row = 6, column = 1)
		cancel_button = Button(self, text = "Cancel", command = self.destroy)
		cancel_button.grid(row = 6, column = 2)

	def validate(self):
		"""Validates the user-supplied data and changes settings if no errors arise.

		Returns:
			True if all entries are valid.
			False if at least one entry is invalid.
		"""

		change_messages = []
		error_messages = []
		errors = False

		# Validate title
		t = self.title_field.get()

		# Validate plot width
		try:
			pw = int(self.plot_width_field.get())

			if not (pw != None and pw >= 200 and pw <= 1000):
				error_messages.append("Invalid plot width.")
				errors = True
		except ValueError:
			errors = True
			error_messages.append("Plot width must be an integer.")

		# Validate plot height
		try:
			ph = int(self.plot_height_field.get())

			if not (ph != None and ph >= 200 and ph <= 1000):
				error_messages.append("Invalid plot height.")
				errors = True
		except ValueError:
			errors = True
			error_messages.append("Plot height must be an integer.")

		# Validate margin size
		try:
			mrgt = int(self.margin_top_field.get())
			mrgr = int(self.margin_right_field.get())
			mrgb = int(self.margin_bottom_field.get())
			mrgl = int(self.margin_left_field.get())

			# Assemble error messages, if errors exist
			if not (mrgt != None and mrgt >= 15 and mrgt <= 200):
				error_messages.append("Invalid top margin.")
				errors = True

			if not (mrgr != None and mrgr >= 15 and mrgr <= 200):
				error_messages.append("Invalid right margin.")
				errors = True

			if not (mrgb != None and mrgb >= 15 and mrgb <= 200):
				error_messages.append("Invalid bottom margin.")
				errors = True

			if not (mrgl != None and mrgl >= 15 and mrgl <= 200):
				error_messages.append("Invalid left margin.")
				errors = True
		except ValueError:
			errors = True
			error_messages.append("Margin sizes must be an integer.")

		# Handle errors
		if not errors:
			# Set all the validated settings
			if self.controller.plot_configuration.set_property('title', t):
				change_messages.append('title: ' + str(t))
			if self.controller.plot_configuration.set_property('show_title', self.show_title.get()):
				change_messages.append('show_title: ' + str(self.show_title.get()))
			if self.controller.plot_configuration.set_property('plot_width', pw):
				change_messages.append('plot_width: ' + str(pw))
			if self.controller.plot_configuration.set_property('plot_height', ph):
				change_messages.append('plot_height: ' + str(ph))
			if self.controller.plot_configuration.set_property('margin_top', mrgt):
				change_messages.append('margin_top: ' + str(mrgt))
			if self.controller.plot_configuration.set_property('margin_right', mrgr):
				change_messages.append('margin_right: ' + str(mrgr))
			if self.controller.plot_configuration.set_property('margin_bottom', mrgb):
				change_messages.append('margin_bottom: ' + str(mrgb))
			if self.controller.plot_configuration.set_property('margin_left', mrgl):
				change_messages.append('margin_left' + str(mrgl))

			self.controller.plot_area.resize(pw, ph)
			self.controller.draw_new_chart()

			# Display change messages
			base_message = 'The following property changes were made:\n\n'
			output = base_message

			for message in change_messages:
				output = output + message + "\n"

			if output != base_message: tkinter.messagebox.showinfo('Success', output)

			self.destroy()
		else:
			# Display error messages and do nothing
			output = ''

			for message in error_messages:
				output = output + message + "\n"

			tkinter.messagebox.showinfo('Error', output)