import sys
from . import buttons
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class CreateApp:
	"""
	Create app builds and positions the buttons
	Methods:
		__init__
		createLayout
	"""
	def __init__(self):
		self.createLayout()

	def createLayout(self):
		"""
		The createLayout method builds the grid and calls the class button to 
		create the buttons themselves. It then positions the buttons in the grid
		"""

		#grid is the layout of the app
		grid = QGridLayout()

		#results is the input/text/display box at the top of the app
		results = QLineEdit()

		#the buttons themselves
		buttonLabels = ['AC', 'DEL', '√', '/',
					7, 8, 9, "*",
					4, 5, 6, "-",
					1, 2, 3, "+",
					0, ".", "="]
		row = 1
		col = 0
		grid.addWidget(results, 0, 0, 1, 4)
		for button in buttonLabels:
			if col > 3:
				col = 0
				row += 1
			buttonObject = buttons.Button(button, results)
			if button == 0:
				grid.addWidget(buttonObject.b, row, col, 1, 2)
				col+=1
			else:
				grid.addWidget(buttonObject.b, row, col, 1, 1)
			col += 1

		self.grid = grid
