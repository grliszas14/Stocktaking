#! /usr/bin/python3
# -*- coding: utf-8 -*-

'''
© 2018 Grzegorz Wojciechowski All right reserved

Icons from:
https://freeiconshop.com/
https://www.shareicon.net
'''

import sys
from PyQt5.QtWidgets import (QApplication, QDesktopWidget, QWidget,
	QMainWindow, QAction, qApp, QToolTip, QTableWidget, QTableWidgetItem,
	QGridLayout)
from PyQt5.QtGui import QIcon, QFont
from PyQt5 import QtCore

class MainWindow(QMainWindow):

	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		self.resize(655,400)
		self.center()
		self.setWindowTitle('Stocktaking')
		self.setWindowIcon(QIcon('images/book.png'))

		searchAction = QAction(QIcon('images/search.png'), 'Search', self)
		addAction = QAction(QIcon('images/add.png'), 'Add', self)
		editAction = QAction(QIcon('images/edit.png'), 'Edit', self)
		deleteAction = QAction(QIcon('images/trash.png'), 'Delete', self)
		printAction = QAction(QIcon('images/print.png'), 'Print', self)
		optionsAction = QAction(QIcon('images/options.png'), 'Options', self)

		exitAction = QAction(QIcon('images/exit.png'), 'Exit', self)
		exitAction.setShortcut('Ctrl+Q')
		exitAction.triggered.connect(qApp.quit)

		toolbar = self.addToolBar('MainToolbar')
		toolbar.setIconSize(QtCore.QSize(40,40))
		toolbar.addAction(searchAction)
		toolbar.addAction(addAction)
		toolbar.addAction(editAction)
		toolbar.addAction(deleteAction)
		toolbar.addAction(printAction)
		toolbar.addAction(optionsAction)
		toolbar.addAction(exitAction)

		centralWidget = QWidget(self)
		self.setCentralWidget(centralWidget)

		gridLayout = QGridLayout()
		centralWidget.setLayout(gridLayout)
		self.createTable()
		gridLayout.addWidget(self.tableWidget, 0, 0)

		self.show()

	def center(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def createTable(self):
		self.tableWidget = QTableWidget()
		self.tableWidget.setRowCount(20) #get how many scores in database
		self.tableWidget.setColumnCount(6)
		self.tableWidget.setHorizontalHeaderLabels(['Barcode', 'Index', 'Name', 'Catalogue number', 'State', 'Description'])
		self.tableWidget.resizeColumnsToContents()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = MainWindow()
	sys.exit(app.exec_())
