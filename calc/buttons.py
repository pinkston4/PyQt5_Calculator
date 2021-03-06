import math
from PyQt5.QtWidgets import *


class Button:
    """
    The Button class builds the button and handles the events
    Arguments:
        text = the text displayed on the button
        results = what is or will be in the text box at the top of the app
    Methods:
        __init__
        handle_input
    """
    def __init__(self, text, results):
        """
        self.b.clicked is the attribute that acts as an event listener
        when QPushButton b is clicked it takes the value of that button,
        the text argument, and passes text to handle_input
        """
        self.b = QPushButton(str(text))
        self.text = text
        self.results = results
        self.b.clicked.connect(lambda: self.handle_input(self.text))

    def handle_input(self, v):
        """
        The method handle_input determines the course of action when a
        button is pressed. It has one argument, v.
        Arguments:
            v = the value/meaning of the button
        """
        if v == "=":
            # "=" takes what is in the box and runs it through the eval function
            res = eval(self.results.text())
            self.results.setText(str(res))
        elif v == "AC":
            self.results.setText(None)
        elif v == "√":
            # the square root of a number
            value = float(self.results.text())
            self.results.setText(str(math.sqrt(value)))
        elif v == "DEL":
            # "DEL" acts as backspace and deletes the last character in result
            current_value = self.results.text()
            self.results.setText(current_value[:-1])
        else:
            current_value = self.results.text()
            new_value = current_value + str(v)
            self.results.setText(new_value)
