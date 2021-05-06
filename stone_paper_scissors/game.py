from PyQt5 import QtCore, QtGui, QtWidgets
import random
option=['Stone','Paper','Scissor']
computer_choice=random.choice(option)
#print(computer_choice)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("PyGame")
        MainWindow.resize(821, 603)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.photo_label = QtWidgets.QLabel(self.centralwidget)
        self.photo_label.setGeometry(QtCore.QRect(440, 410, 281, 171))
        self.photo_label.setText("")
        self.photo_label.setPixmap(QtGui.QPixmap("sps.jpg"))
        self.photo_label.setObjectName("photo_label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(100, 10, 551, 41))
        self.textEdit.setObjectName("textEdit")
        self.stone_button = QtWidgets.QPushButton(self.centralwidget)
        self.stone_button.setGeometry(QtCore.QRect(560, 230, 171, 41))
        self.stone_button.setObjectName("stone_button")
        self.paper_button = QtWidgets.QPushButton(self.centralwidget)
        self.paper_button.setGeometry(QtCore.QRect(560, 170, 171, 41))
        self.paper_button.setObjectName("paper_button")
        self.scissor_button = QtWidgets.QPushButton(self.centralwidget)
        self.scissor_button.setGeometry(QtCore.QRect(560, 110, 171, 41))
        self.scissor_button.setObjectName("scissor_button")
        self.img1_label = QtWidgets.QLabel(self.centralwidget)
        self.img1_label.setGeometry(QtCore.QRect(-10, 70, 481, 471))
        self.img1_label.setText("")
        self.img1_label.setPixmap(QtGui.QPixmap("img2.png"))
        self.img1_label.setObjectName("img1_label")
        self.winner_label = QtWidgets.QLabel(self.centralwidget)
        self.winner_label.setGeometry(QtCore.QRect(530, 300, 231, 61))
        self.winner_label.setAcceptDrops(False)
        self.winner_label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.winner_label.setTextFormat(QtCore.Qt.RichText)
        self.winner_label.setScaledContents(False)
        self.winner_label.setObjectName("winner_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.stone_button.clicked.connect(self.stone)
        self.paper_button.clicked.connect(self.paper)
        self.scissor_button.clicked.connect(self.scissor)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("PyGame", "PyGame"))
        self.textEdit.setHtml(_translate("PyGame", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600; color:#aaaaff;\">Welcome to Stone Paper Scissor Game </span></p></body></html>"))
        self.stone_button.setText(_translate("MainWindow", "Stone"))
        self.paper_button.setText(_translate("MainWindow", "Paper"))
        self.scissor_button.setText(_translate("MainWindow", "Scissor"))
        self.winner_label.setText(_translate("MainWindow", "Let\'s See who wins !!"))

    def stone(self):
        if computer_choice=='Stone':
            self.winner_label.setText("Computer's choice is Stone : It's a Tie ! Nobody won")
        elif computer_choice=='Paper':
            self.winner_label.setText("Computer's choice is Paper : Computer Won !!")
        else:
            self.winner_label.setText("Computer's choice is Scissor : You Won wohoo!!")


    def paper(self):
        if computer_choice=='Stone':
            self.winner_label.setText("Computer's choice is Stone : You Won wohoo!!")
        elif computer_choice=='Paper':
            self.winner_label.setText("Computer's choice is Paper : It's a Tie ! Nobody won")
        else:
            self.winner_label.setText("Computer's choice is Scissor : Computer Won!")


    def scissor(self):
        if computer_choice=='Stone':
            self.winner_label.setText("Computer's choice is Stone : Computer Won!")
        elif computer_choice=='Paper':
            self.winner_label.setText("Computer's choice is Paper : You Won wohoo!!")
        else:
            self.winner_label.setText("Computer's choice is Scissor : It's a Tie ! Nobody won")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
