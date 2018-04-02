from tkinter import *
import tkinter.messagebox


class PlotConfigurationWindow(Toplevel):

	def __init__(self, parent):
		"""Creates a plot configuration window, where the user can change plot settings."""

		Toplevel.__init__(self)

		self.parent = parent
		self.title("Settings")

		# Get focus
		self.lift()
		self.focus_force()
		self.attributes("-topmost", True)
		self.grab_set()

		# Chart title
		self.title_label = Label(self, text = "Title:")
		self.title_label.grid(row = 0, column = 0)
		self.title_field = Entry(self)
		self.title_field.insert(0, self.parent.plot_area_configuration.get_title())
		self.title_field.grid(row = 0, column = 2)

		# Plot width
		self.plot_width_label = Label(self, text = "Plot Width (200 - 1000):")
		self.plot_width_label.grid(row = 1, column = 0)
		self.plot_width_field = Entry(self)
		self.plot_width_field.insert(0, self.parent.plot_area_configuration.get_plot_width())
		self.plot_width_field.grid(row = 1, column = 2)

		# Plot height
		self.plot_height_label = Label(self, text = "Plot Height (200 - 1000):")
		self.plot_height_label.grid(row = 2, column = 0)
		self.plot_height_field = Entry(self)
		self.plot_height_field.insert(0, self.parent.plot_area_configuration.get_plot_height())
		self.plot_height_field.grid(row = 2, column = 2)

		# Buffer top
		self.buffer_top_label = Label(self, text = "Buffer Top (0 - 200):")
		self.buffer_top_label.grid(row = 3, column = 0)
		self.buffer_top_field = Entry(self)
		self.buffer_top_field.insert(0, self.parent.plot_area_configuration.get_buffer_top())
		self.buffer_top_field.grid(row = 3, column = 2)

		# Buffer left and right
		self.buffer_left_label = Label(self, text = "Buffer Left and Right (0 - 200):")
		self.buffer_left_label.grid(row = 4, column = 0)
		self.buffer_left_field = Entry(self)
		self.buffer_left_field.insert(0, self.parent.plot_area_configuration.get_buffer_left())
		self.buffer_left_field.grid(row = 4, column = 1)
		self.buffer_right_field = Entry(self)
		self.buffer_right_field.insert(0, self.parent.plot_area_configuration.get_buffer_right())
		self.buffer_right_field.grid(row = 4, column = 3)

		# Buffer bottom
		self.buffer_bottom_label = Label(self, text = "Buffer Bottom (0 - 200):")
		self.buffer_bottom_label.grid(row = 5, column = 0)
		self.buffer_bottom_field = Entry(self)
		self.buffer_bottom_field.insert(0, self.parent.plot_area_configuration.get_buffer_bottom())
		self.buffer_bottom_field.grid(row = 5, column = 2)

		# Save and cancel buttons
		save_button = Button(self, text = "Save and Update", command = self.validate)
		save_button.grid(row = 6, column = 1)
		cancel_button = Button(self, text = "Cancel", command = self.destroy)
		cancel_button.grid(row = 6, column = 2)

	def validate(self):
		"""Validates user input and changes settings if *all* settings are valid.
		
		If at least one setting is invalid, an error message describing the issue will display.
		"""

		change_messages = []
		error_messages = []
		errors = False

		# Validate title
		t = self.title_field.get()

		# Validate plot width
		try:
			pw = int(self.plot_width_field.get())

			if pw != None and pw >= 200 and pw <= 1000:
				change_messages.append("Saved plot width.")
			else:
				error_messages.append("Invalid plot width.")
				errors = True
		except ValueError:
			errors = True
			error_messages.append("Plot width must be numeric.")

		# Validate plot height
		try:
			ph = int(self.plot_height_field.get())

			if ph != None and ph >= 200 and ph <= 1000:
				change_messages.append("Saved plot height.")
			else:
				error_messages.append("Invalid plot height.")
				errors = True
		except ValueError:
			errors = True
			error_messages.append("Plot height must be numeric.")

		# Validate buffer size
		try:
			bft = int(self.buffer_top_field.get())
			bfr = int(self.buffer_right_field.get())
			bfb = int(self.buffer_bottom_field.get())
			bfl = int(self.buffer_left_field.get())

			# Assemble success and failure messages
			if bft != None and bft >= 0 and bft <= 200:
				change_messages.append("Saved buffer top.")
			else:
				error_messages.append("Invalid buffer top.")
				errors = True

			if bfr != None and bfr >= 0 and bfr <= 200:
				change_messages.append("Saved buffer right.")
			else:
				error_messages.append("Invalid buffer right.")
				errors = True

			if bfb != None and bfb >= 0 and bfb <= 200:
				change_messages.append("Saved buffer bottom.")
			else:
				error_messages.append("Invalid buffer bottom.")
				errors = True

			if bfl != None and bfl >= 0 and bfl <= 200:
				change_messages.append("Saved buffer left.")
			else:
				error_messages.append("Invalid buffer left.")
				errors = True
		except ValueError:
			errors = True
			error_messages.append("Buffer sizes must be numeric.")

		# Handle errors
		if not errors:
			# Set all the validated settings
			self.parent.plot_area_configuration.set_title(t)
			self.parent.plot_area_configuration.set_plot_width(pw)
			self.parent.plot_area_configuration.set_plot_height(ph)
			self.parent.plot_area_configuration.set_buffer_top(bft)
			self.parent.plot_area_configuration.set_buffer_right(bfr)
			self.parent.plot_area_configuration.set_buffer_bottom(bfb)
			self.parent.plot_area_configuration.set_buffer_left(bfl)
			self.parent.plot_area.resize(pw, ph)
			self.parent.draw_new_chart()
			self.parent.set_status_label(change_messages)
			self.destroy()
		else:
			# Display error messages and do nothing
			output = ''

			for message in error_messages:
				output = output + message + "\n"

			tkinter.messagebox.showinfo('Error', output)