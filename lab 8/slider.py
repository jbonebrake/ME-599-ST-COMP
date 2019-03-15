# -*- coding: utf-8 -*-
#!usr/bin/env python 3

# Script for ME 599 Lab 8
# Jonathan Bonebrake

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton,\
 QVBoxLayout, QLabel, QSlider, QHBoxLayout
from PyQt5.QtCore import Qt


class SliderDisplay(QWidget):
    def __init__(self, name, low, high, ticks = 100):
        #initialize base class
        QWidget.__init__(self)
        #will need these variables later for scaling
        self.name = name
        self.low = low
        self.high = high
        self.ticks = ticks
              
        #define interface elements        
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setTickInterval(0)
        self.slider.setMinimum(0)
        self.slider.setMaximum(ticks)
        self.slider.valueChanged.connect(self.set_label)        
        self.label = QLabel(self.name)
        self.set_label()
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.slider)        
        self.setLayout(self.layout)
        

    def set_label(self):
        self.label_value = self.slider.value()
        self.label.setText(self.name + ': {:7.3f}'.format(self.value())) 
        
    def value(self):
        self.slider_value = self.slider.value()
        self.scaled_value = self.low + \
        (self.slider_value / self.ticks)*(self.high-self.low)
        return self.scaled_value
    
#        
#if __name__ == '__main__':
#    app = QApplication([])
#
#    interface = SliderDisplay('useless slider',10,30,10)
#
#    interface.show()
#    
#    app.exec_()