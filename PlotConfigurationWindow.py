from tkinter import *
import tkinter.messagebox


class PlotConfigurationWindow(Toplevel):

	def __init__(self, parent):

		Toplevel.__init__(self)

		self.parent = parent
		self.title("Settings")

		# Get focus
		self.lift()
		self.focus_force()
		self.attributes("-topmost", True)
		self.grab_set()

		# Plot width
		self.plot_width_label = Label(self, text = "Plot Width (200 - 1000):")
		self.plot_width_label.grid(row = 0, column = 0)
		self.plot_width_field = Entry(self)
		self.plot_width_field.insert(0, self.parent.plot_area_configuration.get_plot_width())
		self.plot_width_field.grid(row = 0, column = 1)

		# Plot height
		self.plot_height_label = Label(self, text = "Plot Height (200 - 1000):")
		self.plot_height_label.grid(row = 1, column = 0)
		self.plot_height_field = Entry(self)
		self.plot_height_field.insert(0, self.parent.plot_area_configuration.get_plot_height())
		self.plot_height_field.grid(row = 1, column = 1)

		# Buffer size
		self.buffer_size_label = Label(self, text = "Buffer Size (0 - 200):")
		self.buffer_size_label.grid(row = 2, column = 0)
		self.buffer_size_field = Entry(self)
		self.buffer_size_field.insert(0, self.parent.plot_area_configuration.get_buffer_size())
		self.buffer_size_field.grid(row = 2, column = 1)

		# Save and cancel buttons
		save_button = Button(self, text = "Save", command = self.validate)
		save_button.grid(row = 3, column = 0)
		cancel_button = Button(self, text = "Cancel", command = self.destroy)
		cancel_button.grid(row = 3, column = 1)

	def validate(self):
		change_messages = []
		error_messages = []
		errors = False

		# Validate plot width
		pw = int(self.plot_width_field.get())

		if pw != None and pw >= 200 and pw <= 1000:
			change_messages.append("Saved plot width.")
		else:
			error_messages.append("Invalid plot width.")
			errors = True

		# Validate plot height
		ph = int(self.plot_height_field.get())

		if ph != None and ph >= 200 and ph <= 1000:
			change_messages.append("Saved plot height.")
		else:
			error_messages.append("Invalid plot height.")
			errors = True

		# Validate buffer size
		bf = int(self.buffer_size_field.get())

		if bf != None and bf >= 0 and bf <= 200:
			change_messages.append("Saved buffer size.")
		else:
			error_messages.append("Invalid buffer size.")
			errors = True

		# Handle errors
		if not errors:
			self.parent.plot_area_configuration.set_plot_width(pw)
			self.parent.plot_area_configuration.set_plot_height(ph)
			self.parent.plot_area_configuration.set_buffer_size(bf)
			self.parent.plot_area.resize(pw, ph)
			self.parent.draw_new_chart()
			self.parent.set_status_label(change_messages)
			self.destroy()
		else:
			# Assemble error messages
			output = ''
			for message in error_messages:
				output = output + message + "\n"

			tkinter.messagebox.showinfo('Error', output)