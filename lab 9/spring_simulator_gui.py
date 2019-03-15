
# -*- coding: utf-8 -*-
#!usr/bin/env python 3

# Script for ME 599 Lab 8
# Jonathan Bonebrake

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,\
 QVBoxLayout, QLabel, QHBoxLayout, QGroupBox


from slider import SliderDisplay
from msd import MassSpringDamper
from insulter import insult

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib import image as mpimg

class MultiInterface(QWidget):
    def __init__(self):
        #initialize base class
        QWidget.__init__(self)
        
        # Initialize Widgets
        self.setWindowTitle('Vibration Simulator')
        self.layout = QHBoxLayout()
        self.subLayout = QVBoxLayout()
        self.layout.addLayout(self.subLayout)
        self.setLayout(self.layout)        
        self.quit_button = QPushButton('Quit')
        self.quit_button.setMaximumHeight(32)
        self.quit_button.clicked.connect(app.exit)
        self.MiddleBoxLabel = QLabel('Type: springy')
        self.MassSlider = SliderDisplay('Mass ',0,10,100)
        self.MassSlider.slider.valueChanged.connect(self.change_sys_label)
        self.SpringSlider = SliderDisplay('Spring ',0,10,100)
        self.SpringSlider.slider.valueChanged.connect(self.change_sys_label)
        self.DamperSlider = SliderDisplay('Damper ',0,10,100)
        self.DamperSlider.slider.valueChanged.connect(self.change_sys_label)
        self.TimeSlider = SliderDisplay('Time (s) ',0,100,100000)
        self.InitialX = SliderDisplay('Initial x (m) ',-10,10,1000)
        self.InitialDX = SliderDisplay('Initial dx (m) ',0,100,100000)
        self.TimeStepSlider = SliderDisplay('Time Step (s) ',0.001,0.1,100)
        self.SimulateButton = QPushButton('Simulate System')
        self.SimulateButton.setMaximumHeight(32)
        self.SimulateButton.clicked.connect(self.simulate_sys)

        # Define Figure
        self.figure = Figure()
        self.display = FigureCanvas(self.figure)
        self.draw(data = None, text = 'Try some values!')
        self.layout.addWidget(self.display)
        
        # Define Top box        
        TopBox = QGroupBox('System Parameters')
        TopBoxLayout = QVBoxLayout()
        TopBox.setLayout(TopBoxLayout)
        TopBoxLayout.addWidget(self.MassSlider)
        TopBoxLayout.addWidget(self.SpringSlider)
        TopBoxLayout.addWidget(self.DamperSlider)
#        TopBoxLayout.addStretch()
#        TopBox.setMaximumHeight(200)
        self.subLayout.addWidget(TopBox)
        
        # Define Middle Box        
        MiddleBox = QGroupBox('System Behavior')
        MiddleBoxLayout = QVBoxLayout()        
        MiddleBoxLayout.addWidget(self.MiddleBoxLabel)
        MiddleBox.setLayout(MiddleBoxLayout)
#        MiddleBoxLayout.addStretch()
        self.subLayout.addWidget(MiddleBox)
                
        # Define Lower Box        
        LowerBox = QGroupBox('Simulation Parameters')
        LowerBoxLayout = QVBoxLayout()
        LowerBox.setLayout(LowerBoxLayout)
        LowerBoxLayout.addWidget(self.TimeSlider)
        LowerBoxLayout.addWidget(self.TimeStepSlider)
        LowerBoxLayout.addWidget(self.InitialX)
        LowerBoxLayout.addWidget(self.InitialDX)
        self.subLayout.addWidget(LowerBox)
        
        # Add simulate, quit buttons
        self.subLayout.addWidget(self.SimulateButton)
        self.subLayout.addWidget(self.quit_button)
    
      
    def simulate_sys(self):
        
        # Print settings to console
        print('\nSimulation Values')
        print('mass: ' + str(self.MassSlider.value()))
        print('spring: ' + str(self.SpringSlider.value()))
        print('damper: ' + str(self.DamperSlider.value()))
        print('time: ' + str(self.TimeSlider.value()))
        print('timestep: ' + str(self.TimeStepSlider.value()))
        
        # Simulate system
        # First check for mass and spring constant equal to zero, which will 
        # break the program
        if self.MassSlider.value() != 0 and self.SpringSlider.value() != 0:
            smd = MassSpringDamper(m=self.MassSlider.value(),k=self.SpringSlider.value(),c=self.DamperSlider.value())
            self.state,self.t = smd.simulate(self.InitialX.value(), self.InitialDX.value(), self.TimeSlider.value(),self.TimeStepSlider.value())
            self.change_sys_label()
            self.draw([self.t,self.state[:,0]],text = None)
            
        # If mass or spring constant are equal to zero, deliver a dissappointed
        # message from Dr. Smart
        else: 
            systemLabel = 'Type: ' + 'inconceivable!'
            self.MiddleBoxLabel.setText(systemLabel)
            self.draw()
        
    def change_sys_label(self):
        systemLabel = 'Type: ' + self.calc_type()
        self.MiddleBoxLabel.setText(systemLabel)
        
    def draw(self, data = None, text = None):
        # function taken from example solution
        # plots Dr. Smart's face as default
        self.figure.clear()
        
        if data:
            ax = self.figure.add_subplot(111)
            ax.plot(data[0],data[1])
            ax.set_title('simulated displacement')
            ax.set_xlabel('time (s)')
            ax.set_ylabel('amplitude (m)')
            self.display.draw()
        else:
            ax = self.figure.add_subplot(111)
            img = mpimg.imread('smart-mime_1_0.jpg')
            
            if text:
                ax.text(105,50,text,color = 'w', size = 15)
                ax = ax.imshow(img)
                self.display.draw()

            else:
                text = insult() + '\nTry different values.'
                ax.text(10,150,text,color = 'w', size = 15)
                ax = ax.imshow(img)
                self.display.draw()    
        
    
    def calc_type(self):
        # calculate damping ration (zeta) for slider settings
        # catches div/0 error and labels system as 'inconceivable'
        k = self.SpringSlider.value()
        m = self.MassSlider.value()
        c = self.DamperSlider.value()
        
        c_c = 2*(k*m)**(1/2)
        
        if c_c == 0:
            return 'inconceivable!'
        
        else:    
            zeta = c/c_c
        
            if 0 <= zeta <= 1:
                return 'underdamped'
            if zeta > 1:
                return 'overdamped'
            if zeta == 1: 
                return 'critically damped'
            if zeta == 0:
                return 'undamped'
            
        
                

if __name__ == '__main__':
    

    
    app = QApplication([])
    
    interface = MultiInterface()
    interface.show()
    
    app.exec_()