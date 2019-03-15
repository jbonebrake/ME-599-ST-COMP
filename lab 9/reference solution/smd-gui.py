#!/usr/bin/env python3


from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QSlider, QLabel, QGroupBox
from PyQt5.QtCore import Qt

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


class SpringMassDamperGUI(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.setWindowTitle('Spring-Mass-Damper Playgound')

		# Control buttons for the interface
		quit_button = QPushButton('Quit')
		quit_button.clicked.connect(app.exit)

		simulate_button = QPushButton('Simulate\nSystem')
		simulate_button.clicked.connect(self.simulate)

		# The display for the graph
		self.figure = Figure()
		self.display = FigureCanvas(self.figure)
		self.draw()

		# The parameters of the system we're simulating
		parameters = QGroupBox('System parameters')
		parameter_layout = QVBoxLayout()
		self.m = SliderDisplay('Mass', 0, 10)
		self.k = SliderDisplay('Spring', 0, 10)
		self.c = SliderDisplay('Damper', 0, 10)
		parameter_layout.addWidget(self.m)
		parameter_layout.addWidget(self.k)
		parameter_layout.addWidget(self.c)
		parameters.setLayout(parameter_layout)

		# The parameters of the simulation themselves
		system = QGroupBox('Simulation parameters')
		system_layout = QVBoxLayout()
		self.t = SliderDisplay('Time (s)', 0, 100)
		self.dt = SliderDisplay('Time step (s)', 0.001, 0.1)
		system_layout.addWidget(self.t)
		system_layout.addWidget(self.dt)
		system.setLayout(system_layout)

		# The layout of the interface
		widget = QWidget()
		self.setCentralWidget(widget)

		top_level_layout = QHBoxLayout()
		widget.setLayout(top_level_layout)
		left_side_layout = QVBoxLayout()

		left_side_layout.addWidget(parameters)
		left_side_layout.addWidget(system)
		left_side_layout.addWidget(simulate_button)
		left_side_layout.addStretch()
		left_side_layout.addWidget(quit_button)
		
		top_level_layout.addLayout(left_side_layout)
		top_level_layout.addWidget(self.display)

	def simulate(self):
		from random import random	
		self.draw([random() for i in range(25)])

	def draw(self, data=None):
		self.figure.clear()

		if data:
			ax = self.figure.add_subplot(111)
			ax.plot(data)
			ax.set_title('Spring-Mass-Damper System Behavior\nk = {0:.3f}, m = {1:.3f}, c = {2:.3f}, dt = {3:.3f}'.format(self.k.value(), self.m.value(), self.c.value(), self.dt.value()))
			ax.set_xlabel('Time (s)')
			ax.set_ylabel('Amplitude')
			self.display.draw()


class SliderDisplay(QWidget):
	def __init__(self, name, low, high, ticks=1000):
		QWidget.__init__(self)

		self.name = name
		self.low = low
		self.range = high - low
		self.ticks = ticks

		# Horizontal layout
		layout = QHBoxLayout()
		self.setLayout(layout)

		self.slider = QSlider(Qt.Horizontal)
		self.slider.setMinimum(0)
		self.slider.setMaximum(ticks)
		self.slider.valueChanged.connect(self.set_value)

		self.display = QLabel()
		self.set_value()

		layout.addWidget(self.display)
		layout.addWidget(self.slider)

	def value(self):
		return (self.slider.value() / self.ticks) * self.range + self.low

	def set_value(self):
		self.display.setText('{0}: {1:.3f}'.format(self.name, self.value()))


class GraphingDisplay(FigureCanvas):
	def __init__(self):
		self.figure = Figure()
		FigureCanvas.__init__(self, self.figure)

	def clear(self):
		self.figure.clear()

	def figure(self):
		return self.add_subplot(111)


if __name__ == '__main__':
	app = QApplication([])

	gui = SpringMassDamperGUI()

	gui.show()

	app.exec_()