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
        self.setWindowIcon(QtGui.QIcon("Resourses/logo.png"))
        self.main_widget = QtWidgets.QWidget(self)
        self.Stylize()

        self.InitFig()
        self.InitLineEdit()
        self.InitButton()
        self.InitLayouts()

       
        self.axes.set_title("Function Plotter")

        
        self.setCentralWidget(self.main_widget)
        self.show()

    def InitLayouts(self) :

        self.layout = QtWidgets.QGridLayout(self.main_widget)
        self.layout.addWidget(self.EquationText,0,0)
        self.layout.addWidget(self.PlotButton,0,1)
        self.EquationText.setMinimumHeight(40)
        self.PlotButton.setMinimumHeight(35)
       
        self.layout.addWidget(self.canvas,2,0,2,2)
        self.layout.setHorizontalSpacing(20)
        self.layout.setMargin(15)

    def InitLineEdit(self):
        self.EquationText= QLineEdit(self)
        self.EquationText.setStyleSheet("background-color: white;") 
        font = self.EquationText.font()      # lineedit current font
        font.setPointSize(15)               # change it's size
        self.EquationText.setFont(font)
        self.equation = str(self.EquationText.text())


    def InitFig(self):
        self.fig = Figure()
        self.axes = self.fig.add_subplot(111)
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setSizePolicy(QtWidgets.QSizePolicy.Expanding, 
                                  QtWidgets.QSizePolicy.Expanding)
        self.canvas.updateGeometry()

    def InitButton(self):
        self.PlotButton = QPushButton("Plot",self)
        self.PlotButton.clicked.connect(self.plotFunc)
        # self.PlotButton.clicked.connect(self.inputValidation)

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

        self.msg= QMessageBox()
        self.msg.setWindowTitle("INVALID INPUT")
        self.msg.setText("Please enter a valid equation")
        self.msg.setWindowIcon(QtGui.QIcon("Resourses/logo.png"))
        self.msg.setIcon(QMessageBox.Warning)
        x = self.msg.exec_()


    def plotFunc(self):
        self.axes.clear()
        self.equation = str(self.EquationText.text())
        inp = self.equation
        print(inp)
        x = np.linspace(-2, 2, 100) 
        expr = inp.replace("^","**")
        self.axes.set_title("$"+inp+"$")


        y= eval(expr)
        self.axes.plot(y)
        self.fig.canvas.draw()

















    #     grid = QGridLayout()
    #     sc = MplCanvas(self, width=5, height=4, dpi=100)
    #     sc.axes.plot([0,1,2,3,4], [10,1,20,3,40])
    #     self.setWindowTitle("Function Plotter")
    #     self.setWindowIcon(QtGui.QIcon("Resourses/logo.png"))
        
       


    # def inputValidation(self):
    #     self.msg= QMessageBox()
    #     self.msg.setWindowTitle("invalid input")
    #     self.msg.setText("please enter valid equation")
    #     self.msg.setWindowIcon(QtGui.QIcon("Resourses/logo.png"))
    #     self.msg.setIcon(QMessageBox.Warning)
    #     x = self.msg.exec_()
    # # def printEq(self):
    # #     self.EquationText

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.setStyleSheet("background-color: gray;") 
    w.show()
    app.exec_()