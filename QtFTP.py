from qt import *
import os, sys

class FTPOkno(QMainWindow):
  
  def __init__(self, *args):
    apply(QMainWindow.__init__, (self,) + args)
    self.hlavniWidget=QWidget(self)
    self.vlayout=QVBoxLayout(self.hlavniWidget, 10, 5)
    
    self.lsv=QListView(self.hlavniWidget)
    self.lsv.addColumn('Prvni sloupec')
    self.lsv.setSelectionMode(QListView.Multi)
    self.lsv.insertItem(QListViewItem(self.lsv, 'Jeden'))
    self.lsv.insertItem(QListViewItem(self.lsv, 'Dva'))
    self.lsv.insertItem(QListViewItem(self.lsv, 'Tri'))
    
    self.tlac=QPushButton('Stiskni', self.hlavniWidget)
    
    self.vlayout.addWidget(self.lsv)
    self.vlayout.addWidget(self.tlac)
    
    QObject.connect(self.tlac, SIGNAL('clicked()'), self.lsv, SLOT('invertSelection()'))
    self.setCentralWidget(self.hlavniWidget)
    
def main(args):
  app=QApplication(args)
  hl_okno=FTPOkno()
  hl_okno.setWindowTitle('FTP prenos')
  hl_okno.show()
  app.connect(app, SIGNAL('lastWindowClosed()'), app, SLOT('quit()'))
  app.exec_loop()
if __name__=='__main__':
  main(sys.argv)