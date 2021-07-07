import math
import sys
from PyQt5.QtWidgets import *


class Button:
    def __init__(self, text, results):
        self.b = QPushButton(text)
        self.text = text
        self.results = results
        self.b.clicked.connect(lambda: self.HandleInput(self.text))

    def HandleInput(self,v):
        if v == "=":
            res = eval(self.results.text())
            self.results.setText(str(res))

        elif v == "RS":
            self.results.setText("")

        elif v == "√":
            value = float(self.results.text())
            self.results.setText(math.sqrt(value))

        else:
            current_value = self.results.text()
            new_value = current_value + str(v)
            self.results.setText(new_value)

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setFixedSize(500,400)
        self.CreateApp()

    def CreateApp(self):

        #Creating our grid
        grid = QGridLayout()

        #result
        result = QLineEdit()

        buttons = ["RS", "%", "√", "/",
                    '7', '8', '9',"*",
                    '4', '5', '6', "-",
                    '1', '2', '3', "+",
                    '0', ".", "="]
        grid.addWidget(result, 0, 0, 1, 4)

        rows = 1
        cols = 0



        for button in buttons:
            if cols > 3:
                cols = 0
                rows += 1

            buttonObject = Button(button, result)
            if button == 0:
                grid.addWidget(buttonObject.b, rows, cols, 2, 2)
                cols += 1

            else:
                grid.addWidget(buttonObject.b, rows, cols, 2, 1)
            cols += 1

        self.setLayout(grid)
        self.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()

    with open("style.css", "r") as style:
        app.setStyleSheet(style.read())

    sys.exit(app.exec())
