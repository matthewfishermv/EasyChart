from tkinter import *
from PlotArea import *
from Chart import *


class EasyChart(Frame):

	def __init__(self, master):

		Frame.__init__(self)
		self.pack()

		master.title("EasyChart 2.0")

		self.toolbar = self.init_toolbar()
		self.main_frame = Frame(self)
		self.main_frame.pack()
		self.plot_area = self.init_plot_area()
		self.status_bar = self.init_status_bar()
		self.status_label = self.init_status_label()

		# Initialize menus
		self.main_menu = Menu(master)
		master.config(menu = self.main_menu)

		self.file_menu = Menu(self.main_menu)
		self.main_menu.add_cascade(label = 'File', menu = self.file_menu)
		self.file_menu.add_command(label = 'New')

		Chart(self.plot_area)

	def init_menu(self):

		# Create a new menu in the main window
		new_menu = Menu(master)

		# File menu
		file_menu = Menu(new_menu)
		new_menu.add_cascasde(label = "File", menu = file_menu)
		file_menu.add_command(label = "New")

		return new_menu

	def init_toolbar(self):

		# Create a new frame at top of main window for toolbar items
		toolbar = Frame(self, bg = '#88ade8')
		toolbar.pack(fill = X)

		button_rand_column = Button(toolbar, text = "Random column chart", command = lambda: draw_chart('column'))
		button_rand_column.pack(side = LEFT, padx = 10, pady = 10)

		button_rand_column = Button(toolbar, text = "Random scatter plot", command = lambda: draw_chart('scatter'))
		button_rand_column.pack(side = LEFT, padx = 10, pady = 10)

		return toolbar

	def init_plot_area(self):

		# Create plot area
		plot_area = PlotArea(self, width = 600, height = 400)

		return plot_area

	def init_status_bar(self):

		# Create a new frame at bottom of main window for status
		status_bar = Frame(self)
		status_bar.pack(side = BOTTOM, fill = X)

		return status_bar

	def init_status_label(self, label_text = 'The application is running.'):

		# Create new status label
		status_label = Label(self.status_bar, text = label_text, bd = 1, relief = SUNKEN, anchor = W)
		status_label.pack(fill = X)

		return status_label


if __name__ == "__main__":
	root = Tk()
	app = EasyChart(root)
	root.mainloop()