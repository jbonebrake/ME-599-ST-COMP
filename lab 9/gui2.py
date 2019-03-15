
# -*- coding: utf-8 -*-
#!usr/bin/env python 3

# Script for ME 599 Lab 8
# Jonathan Bonebrake


from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton,\
 QVBoxLayout, QLabel, QSlider, QHBoxLayout, QGroupBox
from PyQt5.QtCore import Qt

from slider import SliderDisplay

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

class MultiInterface(QWidget):
    def __init__(self):
        #initialize base class
        QWidget.__init__(self)
        
        self.setWindowTitle('title')
        self.layout = QHBoxLayout()
        self.subLayout = QVBoxLayout()
        self.layout.addLayout(self.subLayout)
        self.setLayout(self.layout)        
        self.quit_button = QPushButton('Quit')
        self.quit_button.clicked.connect(app.exit)
        self.MiddleBoxLabel = QLabel('Type: springy')
        self.MassSlider = SliderDisplay('Mass ',0,10,100)
        self.SpringSlider = SliderDisplay('Spring ',0,10,100)
        self.DamperSlider = SliderDisplay('Damper ',0,10,100)
        self.TimeSlider = SliderDisplay('Time (s) ',0,100,100000)
        self.InitialX = SliderDisplay('Initial x (m) ',-10,10,1000)
        self.InitialDX = SliderDisplay('Initial dx (m) ',0,100,100000)
        self.TimeStepSlider = SliderDisplay('Time Step (s) ',0.001,0.1,100)
        self.SimulateButton = QPushButton('Simulate System')
        self.SimulateButton.clicked.connect(self.simulate_sys)
#        self.initUI()
 
        
        # more layout stuff
        
#        widget = QWidget()
#        self.setCentralWidget(widget)
#        widget.setLayout(self.layout)
        
        # figure code
#        self.figure = Figure()
#        self.display = FigureCanvas(self.figure)
#        self.draw()
#        self.layout.addWidget(self.display)
        
        # Define Top box
        
        TopBox = QGroupBox('System Parameters')
        TopBoxLayout = QVBoxLayout()
        TopBox.setLayout(TopBoxLayout)
        TopBoxLayout.addWidget(self.MassSlider)
        TopBoxLayout.addWidget(self.SpringSlider)
        TopBoxLayout.addWidget(self.DamperSlider)
        TopBoxLayout.addStretch()
        self.subLayout.addWidget(TopBox)
        
        # Define Middle Box
        
        MiddleBox = QGroupBox('System Behavior')
        MiddleBoxLayout = QVBoxLayout()        
        MiddleBoxLayout.addWidget(self.MiddleBoxLabel)
        MiddleBox.setLayout(MiddleBoxLayout)
        MiddleBoxLayout.addStretch()
        self.subLayout.addWidget(MiddleBox)
                
        # Define Lower Box
        
        LowerBox = QGroupBox('Simulation Parameters')
        LowerBoxLayout = QVBoxLayout()
        LowerBox.setLayout(LowerBoxLayout)
        LowerBoxLayout.addWidget(self.TimeSlider)
        LowerBoxLayout.addWidget(self.TimeStepSlider)
        LowerBoxLayout.addWidget(self.InitialX)
        LowerBoxLayout.addWidget(self.InitialDX)
        LowerBoxLayout.addWidget(self.SimulateButton)
        LowerBoxLayout.addWidget(self.quit_button) 
        LowerBoxLayout.addStretch()
        self.subLayout.addWidget(LowerBox)
        
    def initUI(self):
#        self.setWindowTitle(self.title)
        self.setGeometry(20, 20, 200, 400)
#        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()
    
      
    def simulate_sys(self):
        print('\nSimulation Values')
        print('mass: ' + str(self.MassSlider.value()))
        print('spring: ' + str(self.SpringSlider.value()))
        print('damper: ' + str(self.DamperSlider.value()))
        print('time: ' + str(self.TimeSlider.value()))
        print('timestep: ' + str(self.TimeStepSlider.value()))
        systemLabel = 'Type: different spring thing'
        self.MiddleBoxLabel.setText(systemLabel)
        self.draw([(1,2,3,4,5,6),(1,2,1,2,1,2)])
        
    def set_label(self,condition):
        condition = condition
        self.setText('Type: ' + condition) 
        
    def draw(self, data = None):
        # function taken from example solution
        self.figure.clear()
        
        if data: 
            ax = self.figure.add_subplot(111)
            ax.plot(data)
            ax.set_title('plot title')
            ax.set_xlabel('time (s)')
            ax.set_ylabel('amplitude (m)')
            self.display.draw()
        
        

if __name__ == '__main__':
    
    app = QApplication([])
    
    interface = MultiInterface()
    interface.show()
    
    app.exec_()