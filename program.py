import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout, QLabel, QLineEdit

from NewtonMethod import newton_method

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

        self.equation = []

    def keyPressEvent(self, e):
        if e.modifiers() & Qt.ControlModifier:
            self.equation.append(self.term_edit.text())
            self.term_edit.setText('')
            self.equation_label.setText(' '.join(self.equation) + " = 0")

    def clickedSolveButton(self):
        result = newton_method(self.equation, unknown_variable='x')
        self.result_label.setText(str(result[0]) + "\t" + result[1])

    def clickedRemoveButton(self):
        self.equation = []
        self.term_edit.setText('')
        self.equation_label.setText('')
        self.result_label.setText('')


    def initUI(self):

        font = QFont("font", 20)
        font.setBold(True)

        self.setWindowTitle("Equation with Newton Method")
        self.setWindowIcon(QIcon("isaac-newton.png"))
        self.move(300, 300)
        self.resize(800, 600)


        grid = QGridLayout()
        grid = QGridLayout()
        self.setLayout(grid)

        term_label = QLabel("항: ")
        term_label.setFont(font)

        grid.addWidget(term_label, 0, 0)

        self.term_edit = QLineEdit()
        self.term_edit.setFont(font)
        grid.addWidget(self.term_edit, 0, 1)

        self.equation_label = QLabel("")
        self.equation_label.setFont(font)

        equation_label_ = QLabel("식: ")
        equation_label_.setFont(font)

        grid.addWidget(equation_label_, 1, 0)
        grid.addWidget(self.equation_label, 1, 1)

        btn_font = QFont('font', 13)
        btn_font.setBold(True)

        remove_btn = QPushButton("Remove", self)
        remove_btn.setFont(btn_font)
        grid.addWidget(remove_btn, 2, 0)
        remove_btn.clicked.connect(self.clickedRemoveButton)

        solve_btn = QPushButton("Solve", self)
        solve_btn.setFont(btn_font)
        grid.addWidget(solve_btn, 2, 1)
        solve_btn.clicked.connect(self.clickedSolveButton)


        result_label_ = QLabel("해: ")
        result_label_.setFont(font)
        grid.addWidget(result_label_, 3, 0)


        self.result_label = QLabel("")
        self.result_label.setFont(font)
        grid.addWidget(self.result_label, 3, 1)

        self.show()


if __name__ == '__main__':

    
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())