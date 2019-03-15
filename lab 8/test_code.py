
# -*- coding: utf-8 -*-
#!usr/bin/env python 3

# Script for ME 599 Lab 8
# Jonathan Bonebrake

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton,\
 QVBoxLayout, QLabel, QSlider, QHBoxLayout
from PyQt5.QtCore import Qt

from time import sleep

class Interface(QWidget):
    def __init__(self, name ,low,high,ticks = 100):
        #initialize base class
        QWidget.__init__(self)
        
        #define interface elements
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setTickPosition(QSlider.TicksBothSides)
        self.slider.setTickInterval(1)
        self.slider.setMinimum(low)
        self.slider.setMaximum(high)
        self.slider.valueChanged.connect(self.set_label)
        
        self.label = QLabel(name)
        self.set_label()
        
        self.quit_button = QPushButton('Quit')
        self.quit_button.clicked.connect(app.exit)   
        
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.slider)
        self.layout.addWidget(self.quit_button)
        self.setLayout(self.layout)
        
    def set_label(self):
        #self.label_value = self.slider.value()
        self.label.setText(str(self.slider.value()))


if __name__ == '__main__':

    app = QApplication([])

    interface = Interface('test',4,44)

    interface.show()

    app.exec_()

        