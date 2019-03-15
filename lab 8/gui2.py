
# -*- coding: utf-8 -*-
#!usr/bin/env python 3

# Script for ME 599 Lab 8
# Jonathan Bonebrake


from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton,\
 QVBoxLayout, QLabel, QSlider, QHBoxLayout, QGroupBox
from PyQt5.QtCore import Qt

from slider import SliderDisplay


class MultiInterface(QWidget):
    def __init__(self):
        #initialize base class
        QWidget.__init__(self)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        
        self.quit_button = QPushButton('Quit')
        self.quit_button.clicked.connect(app.exit)
        
        self.MassSlider = SliderDisplay('Mass ',0,10,100)
        self.SpringSlider = SliderDisplay('Spring ',0,10,100)
        self.DamperSlider = SliderDisplay('Damper ',0,10,100)
        self.TimeSlider = SliderDisplay('Time (s) ',0,100,100000)
        self.TimeSlider2 = SliderDisplay('Time (s) ',0,100,100000)
        self.TimeSlider3 = SliderDisplay('Time (s) ',0,100,100000)
        self.TimeSlider4 = SliderDisplay('Time (s) ',0,100,100000)
        self.TimeStepSlider = SliderDisplay('Time Step (s) ',0.001,0.1,100)
        self.SimulateButton = QPushButton('Simulate System')
        self.SimulateButton.clicked.connect(self.simulate_sys)
        
        
        # Define Top box
        
        TopBox = QGroupBox('System Parameters')
        TopBoxLayout = QVBoxLayout()
        TopBox.setLayout(TopBoxLayout)
        TopBoxLayout.addWidget(self.MassSlider)
        TopBoxLayout.addWidget(self.SpringSlider)
        TopBoxLayout.addWidget(self.DamperSlider)
        self.layout.addWidget(TopBox)
        
        # Define Middle Box
        
        MiddleBox = QGroupBox('Simulation Parameters')
        MiddleBoxLayout = QVBoxLayout()
        MiddleBox.setLayout(MiddleBoxLayout)
        MiddleBoxLayout.addWidget(self.TimeSlider)
        MiddleBoxLayout.addWidget(self.TimeSlider2)
        MiddleBoxLayout.addWidget(self.TimeSlider3)
        MiddleBoxLayout.addWidget(self.TimeSlider4)
        MiddleBoxLayout.addWidget(self.TimeStepSlider)
        MiddleBoxLayout.addWidget(self.SimulateButton)
        MiddleBoxLayout.addWidget(self.quit_button)

        
        self.layout.addWidget(MiddleBox)
      
    def simulate_sys(self):
        print('\nSimulation Values')
        print('mass: ' + str(self.MassSlider.value()))
        print('spring: ' + str(self.SpringSlider.value()))
        print('damper: ' + str(self.DamperSlider.value()))
        print('time: ' + str(self.TimeSlider.value()))
        print('timestep: ' + str(self.TimeStepSlider.value()))

if __name__ == '__main__':
    
    app = QApplication([])
    
    interface = MultiInterface()
    interface.show()
    
    app.exec_()