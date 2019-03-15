#!/usr/bin/env python3


from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton,\
 QVBoxLayout, QLabel, QSlider
from PyQt5.QtCore import Qt

class Interface(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        
        widget = QWidget()
                
        self.setWindowTitle('I am an example window')
        self.setCentralWidget(widget)
        
        self.slider_label = QLabel()
        self.set_label
        
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setTickPosition(QSlider.TicksBothSides)
        self.slider.setTickInterval(1)
        self.slider.setMinimum(1)
        self.slider.setMaximum(10)
   
        self.quit_button = QPushButton('Quit')
        self.quit_button.clicked.connect(app.exit)     
        
    def set_label(self):
        self.label_value = self.slider.value()
        self.slider_label.setText(str(self.label_value()))
        
        # A widget to hold everything


        # A layout
        layout = QVBoxLayout()
        widget.setLayout(layout)

        # A button


        # You probably want to add in other interface elements here
        # Label
#        label_text = 0
#        label_zero = QLabel(str(label_text))            
        

        #slider_label.valueChanged.connect(label_text)
        
        # Add things to the layout
        layout.addWidget(self.label_zero)
        layout.addWidget(self.quit_button)
        layout.addWidget(self.slider)


        # Add other widgets to the layout here.  Possibly other layouts.


if __name__ == '__main__':
    app = QApplication([])

    interface = Interface()

    interface.show()

    app.exec_()

