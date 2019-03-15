#!/usr/bin/env python3


from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QLabel, QHBoxLayout
from PyQt5.QtCore import Qt


class SliderDisplay(QWidget):
    def __init__(self, name, low, high, ticks=1000):
        QWidget.__init__(self)
        layout = QHBoxLayout()
        self.setLayout(layout)

        self.name = name
        self.low = low
        self.range = high - low
        self.ticks = ticks

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(ticks)
        self.slider.valueChanged.connect(self.change_value)

        self.display = QLabel()
        self.change_value()

        layout.addWidget(self.display)
        layout.addWidget(self.slider)

    def value(self):
        """Return the current value of the slider"""
        return (self.slider.value() / self.ticks) * self.range + self.low

    def change_value(self):
        self.display.setText('{0}: {1:.3f}'.format(self.name, self.value()))


if __name__ == '__main__':
    app = QApplication([])

    slider = SliderDisplay('foo', 0, 1)

    slider.show()

    app.exec_()

