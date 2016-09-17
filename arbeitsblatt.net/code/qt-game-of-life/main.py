#!/usr/bin/python3

from PyQt5.QtWidgets import QMainWindow, QApplication # Import the PyQt4 module we'll need
import sys  # We need sys so that we can pass argv to QApplication

import design  # This file holds our MainWindow and all design related things
            # it also keeps events etc that we defined in Qt Designer



class ExampleApp(QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Explaining super is out of the scope of this article
        # So please google it if you're not familar with it
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the design.py file
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
        # It sets up layout and widgets that are defined
        self.pushButton_2.clicked.connect(self.print_hallo)  # When the button is pressed
                                                            # Execute browse_folder function

        self.v = 10
        self.frame.setValue(self.v)
        self.pushButton.clicked.connect(self.increase_v)

    def print_hallo(self):
        print("Hallo")
        self.v = 0
        self.frame.setValue(self.v)

    def increase_v(self):
        self.v = self.v + 20
        self.frame.setValue(self.v)

def main():
    app = QApplication(sys.argv)  # A new instance of QApplication
    form = ExampleApp()  # We set the form to be our ExampleApp (design)
    form.show()  # Show the form
    app.exec_()  # and execute the app


if __name__ == '__main__':  # if we're running file directly and not importing it
    main()  # run the main function
