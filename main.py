from PySide2 import QtCore, QtWidgets , QtGui
from PySide2.QtWidgets import QWidget,QPushButton ,QLineEdit ,QMessageBox ,QHBoxLayout ,QVBoxLayout ,QGridLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import numpy as np
import sys




class MainWindow(QtWidgets.QMainWindow):


    def __init__(self):

        super(MainWindow, self).__init__()
        self.setWindowTitle("Function Plotter")
        self.setWindowIcon(QtGui.QIcon("Resources/logo.png"))
        self.msg= QMessageBox()
        self.setIconSize(QtCore.QSize(500, 500))
        self.main_widget = QtWidgets.QWidget(self)
        self.resize(900,600)

        self.Stylize()
        self.InitLineEdit()
        self.InitFig()
        self.InitButton()
        self.InitLayouts()

        self.axes.set_title("Function Plotter")

        self.setCentralWidget(self.main_widget)
        self.show()

    def InitLayouts(self) :

        self.layout = QtWidgets.QGridLayout(self.main_widget)
        self.layout.addWidget(self.EquationText,0,0)
        self.layout.addWidget(self.x1,0,1)
        self.layout.addWidget(self.x2,0,2)
        self.layout.addWidget(self.PlotButton,0,3)
        self.EquationText.setMinimumHeight(40)
        self.PlotButton.setMinimumHeight(35)
        self.x1.setMinimumHeight(30)
        self.x2.setMinimumHeight(30)
        self.x1.setMaximumWidth(130)
        self.x2.setMaximumWidth(150)    

        self.layout.addWidget(self.canvas,2,0,2,4)
        self.layout.setHorizontalSpacing(20)
        self.layout.setMargin(20)
        


     

    def InitLineEdit(self):
        self.EquationText= QLineEdit(self)
        self.EquationText.setToolTip("supported operators:+ - / * ^ \n e.g. 5*x^3 + 2*x")

        self.EquationText.setContentsMargins(10,0,0,0)
        self.EquationText.setStyleSheet("background-color: white;")
        self.x1= QLineEdit(self)
        self.x2= QLineEdit(self)
        self.x1.setStyleSheet("background-color: white;")
        self.x2.setStyleSheet("background-color: white;")

        font = self.EquationText.font()      # lineedit current font
        font.setPointSize(15)               # change it's size
        self.EquationText.setFont(font)
        self.EquationText.setPlaceholderText("  f(x) = ")
        self.x1.setPlaceholderText(" xMin= ")
        self.x2.setPlaceholderText(" xMax= ")
        self.equation = str(self.EquationText.text())


    def InitFig(self):
        self.fig = Figure()
        self.axes = self.fig.add_subplot(111)
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setStyleSheet("background-color: black;  border: 15px solid black; border-radius: 1px")
        self.canvas.setSizePolicy(QtWidgets.QSizePolicy.Expanding, 
                                  QtWidgets.QSizePolicy.Expanding)
        self.canvas.updateGeometry()

    def InitButton(self):
        self.PlotButton = QPushButton("Plot",self)
        self.PlotButton.setShortcut("Ctrl+P")
        self.PlotButton.setToolTip("CTRL+P")

        self.PlotButton.clicked.connect(self.plotFunc)
        self.PlotButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

    def Stylize(self):
        self.main_widget.setStyleSheet("QPushButton{\n"

        "    background:linear-gradient(to bottom, #ededed 5%, #bab1ba 100%);\n"
        "    background-color:#ededed;\n"
        "    border-radius:15px;\n"
        "    border:2px solid #d6bcd6;\n"
        "    color:#db2525;\n"
        "    font-family:segoe print;\n"
        "    font-size:17px;\n"
        "    padding:7px 25px;\n"
        "    text-decoration:none;\n"
        "}\n"
        "QPushButton:hover {\n"
        "        background:linear-gradient(to bottom, #e371e3 5%, #ededed 100%);\n"
        "    background-color:#bab1bf;\n"
        "}\n"
        "QPushButton:pressed{\n"
        "    position:absolute;\n"
        "    top:-5px;\n"
        "    border-style: ridge;\n"
        "}\n"
        "")

    def inputValidation(self):

        
        self.msg.setWindowTitle("INVALID INPUT")
        self.msg.setWindowIcon(QtGui.QIcon("Resources/logo.png"))
        self.msg.setIcon(QMessageBox.Warning)
        x = self.msg.exec_()


    def plotFunc(self):
        try:
            self.axes.clear()
            self.equation = str(self.EquationText.text()).lower()
            inp = self.equation
            title = inp.replace("*","")
            print(inp)
            x1= int(self.x1.text())
            x2= int(self.x2.text())
            x = np.linspace(x1, x2) 
            expr = inp.replace("^","**")
            self.axes.set_title("$"+title+"$")
            y= eval(expr)
            self.axes.plot(x,y)
            self.fig.canvas.draw()
        except :
            if not (self.x1.text().isdecimal() ) :
                self.msg.setText("Please enter integer valued X Minimum ")
            elif not ( self.x2.text().isdecimal() ) :
                self.msg.setText("Please enter integer valued X Maximum")
            else:
                self.msg.setText("Please enter a valid univariate polynomial equation\n example: 5*x^3 + 2*x ")

            
            self.inputValidation()




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.setStyleSheet("background-color: gray;") 
    w.show()
    app.exec_()