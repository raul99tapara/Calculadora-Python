# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Calculadora.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(283, 240)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Cornmanthe3rd-Plex-Other-python.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.Pantalla = QtGui.QLineEdit(Form)
        self.Pantalla.setGeometry(QtCore.QRect(10, 10, 261, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Pantalla.setFont(font)
        self.Pantalla.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.Pantalla.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Pantalla.setObjectName(_fromUtf8("Pantalla"))
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(11, 41, 261, 180))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.btn7 = QtGui.QPushButton(self.widget)
        self.btn7.setMinimumSize(QtCore.QSize(40, 40))
        self.btn7.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn7.setFont(font)
        self.btn7.setObjectName(_fromUtf8("btn7"))
        self.gridLayout.addWidget(self.btn7, 0, 0, 1, 1)
        self.btn8 = QtGui.QPushButton(self.widget)
        self.btn8.setMinimumSize(QtCore.QSize(40, 40))
        self.btn8.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn8.setFont(font)
        self.btn8.setObjectName(_fromUtf8("btn8"))
        self.gridLayout.addWidget(self.btn8, 0, 1, 1, 1)
        self.btn9 = QtGui.QPushButton(self.widget)
        self.btn9.setMinimumSize(QtCore.QSize(40, 40))
        self.btn9.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn9.setFont(font)
        self.btn9.setObjectName(_fromUtf8("btn9"))
        self.gridLayout.addWidget(self.btn9, 0, 2, 1, 1)
        self.btnDiv = QtGui.QPushButton(self.widget)
        self.btnDiv.setMinimumSize(QtCore.QSize(40, 40))
        self.btnDiv.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnDiv.setFont(font)
        self.btnDiv.setObjectName(_fromUtf8("btnDiv"))
        self.gridLayout.addWidget(self.btnDiv, 0, 3, 1, 1)
        self.btnPar1 = QtGui.QPushButton(self.widget)
        self.btnPar1.setMinimumSize(QtCore.QSize(40, 40))
        self.btnPar1.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnPar1.setFont(font)
        self.btnPar1.setObjectName(_fromUtf8("btnPar1"))
        self.gridLayout.addWidget(self.btnPar1, 0, 4, 1, 1)
        self.btn4 = QtGui.QPushButton(self.widget)
        self.btn4.setMinimumSize(QtCore.QSize(40, 40))
        self.btn4.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn4.setFont(font)
        self.btn4.setObjectName(_fromUtf8("btn4"))
        self.gridLayout.addWidget(self.btn4, 1, 0, 1, 1)
        self.btn5 = QtGui.QPushButton(self.widget)
        self.btn5.setMinimumSize(QtCore.QSize(40, 40))
        self.btn5.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn5.setFont(font)
        self.btn5.setObjectName(_fromUtf8("btn5"))
        self.gridLayout.addWidget(self.btn5, 1, 1, 1, 1)
        self.btn6 = QtGui.QPushButton(self.widget)
        self.btn6.setMinimumSize(QtCore.QSize(40, 40))
        self.btn6.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn6.setFont(font)
        self.btn6.setObjectName(_fromUtf8("btn6"))
        self.gridLayout.addWidget(self.btn6, 1, 2, 1, 1)
        self.btnMult = QtGui.QPushButton(self.widget)
        self.btnMult.setMinimumSize(QtCore.QSize(40, 40))
        self.btnMult.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnMult.setFont(font)
        self.btnMult.setObjectName(_fromUtf8("btnMult"))
        self.gridLayout.addWidget(self.btnMult, 1, 3, 1, 1)
        self.btnPar2 = QtGui.QPushButton(self.widget)
        self.btnPar2.setMinimumSize(QtCore.QSize(40, 40))
        self.btnPar2.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnPar2.setFont(font)
        self.btnPar2.setObjectName(_fromUtf8("btnPar2"))
        self.gridLayout.addWidget(self.btnPar2, 1, 4, 1, 1)
        self.btn1 = QtGui.QPushButton(self.widget)
        self.btn1.setMinimumSize(QtCore.QSize(40, 40))
        self.btn1.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn1.setFont(font)
        self.btn1.setObjectName(_fromUtf8("btn1"))
        self.gridLayout.addWidget(self.btn1, 2, 0, 1, 1)
        self.btn2 = QtGui.QPushButton(self.widget)
        self.btn2.setMinimumSize(QtCore.QSize(40, 40))
        self.btn2.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn2.setFont(font)
        self.btn2.setObjectName(_fromUtf8("btn2"))
        self.gridLayout.addWidget(self.btn2, 2, 1, 1, 1)
        self.btn3 = QtGui.QPushButton(self.widget)
        self.btn3.setMinimumSize(QtCore.QSize(40, 40))
        self.btn3.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn3.setFont(font)
        self.btn3.setObjectName(_fromUtf8("btn3"))
        self.gridLayout.addWidget(self.btn3, 2, 2, 1, 1)
        self.btnSuma = QtGui.QPushButton(self.widget)
        self.btnSuma.setMinimumSize(QtCore.QSize(40, 40))
        self.btnSuma.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnSuma.setFont(font)
        self.btnSuma.setObjectName(_fromUtf8("btnSuma"))
        self.gridLayout.addWidget(self.btnSuma, 2, 3, 1, 1)
        self.btnIgual = QtGui.QPushButton(self.widget)
        self.btnIgual.setMinimumSize(QtCore.QSize(40, 85))
        self.btnIgual.setMaximumSize(QtCore.QSize(40, 85))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnIgual.setFont(font)
        self.btnIgual.setObjectName(_fromUtf8("btnIgual"))
        self.gridLayout.addWidget(self.btnIgual, 2, 4, 2, 1)
        self.btn0 = QtGui.QPushButton(self.widget)
        self.btn0.setMinimumSize(QtCore.QSize(40, 40))
        self.btn0.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn0.setFont(font)
        self.btn0.setObjectName(_fromUtf8("btn0"))
        self.gridLayout.addWidget(self.btn0, 3, 0, 1, 1)
        self.btnPunto = QtGui.QPushButton(self.widget)
        self.btnPunto.setMinimumSize(QtCore.QSize(40, 40))
        self.btnPunto.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnPunto.setFont(font)
        self.btnPunto.setObjectName(_fromUtf8("btnPunto"))
        self.gridLayout.addWidget(self.btnPunto, 3, 1, 1, 1)
        self.btnAC = QtGui.QPushButton(self.widget)
        self.btnAC.setMinimumSize(QtCore.QSize(40, 40))
        self.btnAC.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnAC.setFont(font)
        self.btnAC.setObjectName(_fromUtf8("btnAC"))
        self.gridLayout.addWidget(self.btnAC, 3, 2, 1, 1)
        self.btnResta = QtGui.QPushButton(self.widget)
        self.btnResta.setMinimumSize(QtCore.QSize(40, 40))
        self.btnResta.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnResta.setFont(font)
        self.btnResta.setObjectName(_fromUtf8("btnResta"))
        self.gridLayout.addWidget(self.btnResta, 3, 3, 1, 1)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.btnAC, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Pantalla.clear)
        QtCore.QObject.connect(self.btn0, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda:self.Agregar('0'))
        QtCore.QObject.connect(self.btn1, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda:self.Agregar('1'))
        QtCore.QObject.connect(self.btn2, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda:self.Agregar('2'))
        QtCore.QObject.connect(self.btn3, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda:self.Agregar('3'))
        QtCore.QObject.connect(self.btn4, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda:self.Agregar('4'))
        QtCore.QObject.connect(self.btn5, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda:self.Agregar('5'))
        QtCore.QObject.connect(self.btn6, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda:self.Agregar('6'))
        QtCore.QObject.connect(self.btn7, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda:self.Agregar('7'))
        QtCore.QObject.connect(self.btn8, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda:self.Agregar('8'))
        QtCore.QObject.connect(self.btn9, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda:self.Agregar('9'))
        QtCore.QObject.connect(self.btnSuma, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda:self.Agregar('+'))
        QtCore.QObject.connect(self.btnResta, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda:self.Agregar('-'))
        QtCore.QObject.connect(self.btnMult, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda:self.Agregar('*'))
        QtCore.QObject.connect(self.btnDiv, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda:self.Agregar('/'))
        QtCore.QObject.connect(self.btnPar1, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda:self.Agregar('('))
        QtCore.QObject.connect(self.btnPar2, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda:self.Agregar(')'))
        QtCore.QObject.connect(self.btnPunto, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda:self.Agregar('.'))
        
        QtCore.QObject.connect(self.btnIgual, QtCore.SIGNAL(_fromUtf8("clicked()")),self.Operaciones)
        
        
        QtCore.QMetaObject.connectSlotsByName(Form)

    def Agregar(self,Valor):
        ValorPantalla = self.Pantalla.text()
        self.Pantalla.setText(ValorPantalla+Valor)

    def Operaciones(self):
        expr = self.Pantalla.text()
        resultado = eval(str(expr))
        if type(resultado) in [float,int]:
            self.Pantalla.setText(str(resultado))
            

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Calculadora", None))
        self.btn7.setText(_translate("Form", "7", None))
        self.btn8.setText(_translate("Form", "8", None))
        self.btn9.setText(_translate("Form", "9", None))
        self.btnDiv.setText(_translate("Form", "/", None))
        self.btnPar1.setText(_translate("Form", "(", None))
        self.btn4.setText(_translate("Form", "4", None))
        self.btn5.setText(_translate("Form", "5", None))
        self.btn6.setText(_translate("Form", "6", None))
        self.btnMult.setText(_translate("Form", "*", None))
        self.btnPar2.setText(_translate("Form", ")", None))
        self.btn1.setText(_translate("Form", "1", None))
        self.btn2.setText(_translate("Form", "2", None))
        self.btn3.setText(_translate("Form", "3", None))
        self.btnSuma.setText(_translate("Form", "+", None))
        self.btnIgual.setText(_translate("Form", "=", None))
        self.btn0.setText(_translate("Form", "0", None))
        self.btnPunto.setText(_translate("Form", ".", None))
        self.btnAC.setText(_translate("Form", "AC", None))
        self.btnResta.setText(_translate("Form", "-", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

