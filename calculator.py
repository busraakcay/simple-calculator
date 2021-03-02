import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip, QPushButton
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()

        self.setWindowTitle("Calculator")
        self.setGeometry(700,300,260,350)
        self.setToolTip("Calculator")
        self.setWindowIcon(QIcon('icon.png'))
        self.initUI()
    
    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(5,5,240,70)
        self.label.setStyleSheet("QLabel { border : 1px ridge gray; background : white; }")
        self.label.setAlignment(Qt.AlignRight) 
        self.label.move(10, 10)
        self.label.setFont(QFont('Sans-Serif', 20))

        clear = QPushButton("Clear", self)
        clear.setGeometry(10, 290, 120, 50)

        dlt = QPushButton("Delete", self)
        dlt.setGeometry(130, 290, 120, 50)

        one = QPushButton("1",self)
        one.setGeometry(10, 85, 60, 50)

        two = QPushButton("2", self)
        two.setGeometry(70, 85, 60, 50)

        three = QPushButton("3",self)
        three.setGeometry(130, 85, 60, 50)

        four = QPushButton("4", self)
        four.setGeometry(10, 135, 60, 50)

        five = QPushButton("5",self)
        five.setGeometry(70, 135, 60, 50)

        six = QPushButton("6", self)
        six.setGeometry(130, 135, 60, 50)

        seven = QPushButton("7",self)
        seven.setGeometry(10, 185, 60, 50)

        eight = QPushButton("8", self)
        eight.setGeometry(70, 185, 60, 50)

        nine = QPushButton("9",self)
        nine.setGeometry(130, 185, 60, 50)

        dot = QPushButton(".", self)
        dot.setGeometry(10, 235, 60, 50)

        zero = QPushButton("0", self)
        zero.setGeometry(70, 235, 60, 50)

        eq = QPushButton("=",self)
        eq.setGeometry(130, 235, 60, 50)

        summ = QPushButton("+",self)
        summ.setGeometry(190, 85, 60, 50)

        sub = QPushButton("-",self)
        sub.setGeometry(190, 135, 60, 50)

        mult = QPushButton("*", self)
        mult.setGeometry(190, 185, 60, 50)

        div = QPushButton("/", self)
        div.setGeometry(190, 235, 60, 50)

        one.clicked.connect(self.act_one)
        two.clicked.connect(self.act_two)
        three.clicked.connect(self.act_three)
        four.clicked.connect(self.act_four)
        five.clicked.connect(self.act_five)
        six.clicked.connect(self.act_six)
        seven.clicked.connect(self.act_seven)
        eight.clicked.connect(self.act_eight)
        nine.clicked.connect(self.act_nine)
        zero.clicked.connect(self.act_zero)
        dot.clicked.connect(self.act_dot)
        summ.clicked.connect(self.act_summ)
        sub.clicked.connect(self.act_sub)
        mult.clicked.connect(self.act_mult)
        div.clicked.connect(self.act_div)
        eq.clicked.connect(self.act_eq)
        clear.clicked.connect(self.act_clr)
        dlt.clicked.connect(self.act_dlt)   

    def act_eq(self):
        result = self.label.text() 
  
        try: 
            answer = eval(result) 
            self.label.setText(str(answer)) 
  
        except: 
            self.label.setText("Try Again")
    
    def act_clr(self):
        self.label.setText("")

    def act_dlt(self):
        text = self.label.text()
        self.label.setText(text[:len(text)-1])

    def act_one(self):
        text = self.label.text() 
        self.label.setText(text + "1")

    def act_two(self):
        text = self.label.text() 
        self.label.setText(text + "2") 

    def act_three(self):
        text = self.label.text() 
        self.label.setText(text + "3")

    def act_four(self):
        text = self.label.text() 
        self.label.setText(text + "4")

    def act_five(self):
        text = self.label.text() 
        self.label.setText(text + "5")

    def act_six(self):
        text = self.label.text() 
        self.label.setText(text + "6")

    def act_seven(self):
        text = self.label.text() 
        self.label.setText(text + "7") 

    def act_eight(self):
        text = self.label.text() 
        self.label.setText(text + "8") 

    def act_nine(self):
        text = self.label.text() 
        self.label.setText(text + "9") 

    def act_zero(self):
        text = self.label.text() 
        self.label.setText(text + "0") 

    def act_dot(self):
        text = self.label.text() 
        self.label.setText(text + ".")

    def act_summ(self):
        text = self.label.text() 
        self.label.setText(text + "+") 

    def act_sub(self):
        text = self.label.text() 
        self.label.setText(text + "-") 

    def act_mult(self):
        text = self.label.text() 
        self.label.setText(text + "*") 

    def act_div(self):
        text = self.label.text() 
        self.label.setText(text + "/")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter:
            self.act_eq()
        
        if event.key() == Qt.Key_Delete:
            self.act_dlt()
        
        if event.key() == Qt.Key_Space:
            self.act_clr()

        text = self.label.text()
        self.label.setText(text + event.text())

def CalculatorWindow():
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec_())

CalculatorWindow()

