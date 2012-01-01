from PyQt4 import QtCore, QtGui
import os, sys

app = QtGui.QApplication(sys.argv)
pts = '/cesta/k/adresari/pro/synchronizaci'

MainWindow = QtGui.QMainWindow()
MainWindow.setWindowTitle('IHMS')
MainWidget=QtGui.QWidget(MainWindow)
MainWindow.setCentralWidget(MainWidget)

layout=QtGui.QGridLayout(MainWidget)


path_to_syn = QtGui.QLineEdit(MainWidget)
ftp_account = QtGui.QLineEdit(MainWidget)
ftp_passwd = QtGui.QLineEdit(MainWidget)
ftp_passwd.setEchoMode(QtGui.QLineEdit.Password)

path_to_syn_txt = QtGui.QLabel(MainWidget)
ftp_account_txt = QtGui.QLabel(MainWidget)
ftp_passwd_txt = QtGui.QLabel(MainWidget)
path_to_syn_txt.setText('Path to your directory: ')
ftp_account_txt.setText('FTP: (pr.: myftp.com)')
ftp_passwd_txt.setText('Password: ')


layout.addWidget (path_to_syn_txt,0,0,QtCore.Qt.AlignLeft)
layout.addWidget (path_to_syn,0,1,QtCore.Qt.AlignRight)
layout.addWidget (ftp_account_txt,1,0,QtCore.Qt.AlignLeft)
layout.addWidget (ftp_account,1,1,QtCore.Qt.AlignRight)
layout.addWidget (ftp_passwd_txt,2,0,QtCore.Qt.AlignLeft)
layout.addWidget (ftp_passwd,2,1,QtCore.Qt.AlignRight)

MainWindow.show()
sys.exit(app.exec_())
