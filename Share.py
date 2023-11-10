#!/usr/bin/python3

import sys
from PySide2.QtWidgets import QApplication, QMainWindow,QFileDialog ,QListView,QTreeView, QAbstractItemView, QDialog
from PySide2.QtCore import QFile
from PySide2.QtGui import QStandardItem,QStandardItemModel
from MainWindow import Ui_MainWindow
from WebServer import *
from SharingDialog import *
import socket
from MessageDialog import *

def ResizeList(l, size, fill_with=None):
    l += [fill_with]*(size-len(l))


class SharingDialog(QDialog):
    def __init__(self,parent):
        super().__init__(parent)
        self.setWindowTitle("Sharing")
        self.parent=parent
        self.ui=Ui_SharingDialog()
        self.ui.setupUi(self)
        self.ui.stopSharing.clicked.connect(self.stopSharing)

    def stopSharing(self):
        if self.parent.w!=None:
            self.parent.w.stop()
        self.parent.clean()
        self.done(0)

class MessageDialog(QDialog):
    def __init__(self,parent,message):
        super().__init__(parent)
        self.parent=parent
        self.ui=Ui_MessageDialog()
        self.ui.setupUi(self)
        self.ui.message.setText(message)
        self.ui.closeButton.clicked.connect(self.closeDialog)
    def allowtoclose(self):
        self.ui.closeButton.setEnabled(True)
    def closeDialog(self):
        self.done(0)

class MainWindow(QMainWindow):

    files=[]
    folders=[]
    r=None
    w=None
    model = QStandardItemModel()

    def delduplicates(self,files,file):
        result=[1]
        if file:
            k=0
            for i in files:
                add=True
                for j in self.files:
                    if i==j:
                        add=False
                if(add):
                    ResizeList(result,k+1)
                    result[k]=i
                    k=k+1
        else:
            k=0
            for i in files:
                add=True
                for j in self.folders:
                    if i==j:
                        add=False
                if(add):
                    ResizeList(result,k+1)
                    result[k]=i
                    k=k+1
        return result

    def fileChooser(self):
        self.setStatus("Choose Files")
        dialog=QFileDialog(self)
        dialog.setOption(QFileDialog.DontUseNativeDialog, True)
        dialog.setFileMode(QFileDialog.ExistingFiles)
        #files, _ = QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "","All Files (*)",mode="DirectoryOnly")
        if dialog.exec():
            files=dialog.selectedFiles()
            i=0
            files=self.delduplicates(files,True)
            l=len(self.files)
            nl=len(files)
            ResizeList(self.files, l+nl)
            while i<nl:
                self.files[l+i]=files[i]
                item = QStandardItem(files[i])
                self.model.appendRow(item)
                i=i+1
        self.setStatus("Done")

    def clean(self):
        self.r.clean()
        self.r=WebRoot()
        self.files=[]
        self.folders=[]
        self.w=None
        self.model.removeRows( 0, self.model.rowCount() )


    def folderChooser(self):
        self.setStatus("Choose folders")
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.DirectoryOnly)
        dialog.setOption(QFileDialog.DontUseNativeDialog, True)
        file_view = dialog.findChild(QListView, 'listView')
        if file_view:
            file_view.setSelectionMode(QAbstractItemView.MultiSelection)
        f_tree_view = dialog.findChild(QTreeView)
        if f_tree_view:
            f_tree_view.setSelectionMode(QAbstractItemView.MultiSelection)
        if dialog.exec():
            files=dialog.selectedFiles()
            i=0
            files=self.delduplicates(files,False)
            l=len(self.folders)
            nl=len(files)
            ResizeList(self.folders, l+nl)
            while i<nl:
                    self.folders[l+i]=files[i]
                    item = QStandardItem(files[i])
                    self.model.appendRow(item)
                    i=i+1
        self.setStatus("Done")

    def run(self):
        self.setStatus("Creating webroot")
        i=0
        while i<len(self.files):
            self.r.add_file(self.files[i])
            i=i+1
        i=0
        while i<len(self.folders):
            self.r.add_dir(self.folders[i])
            i=i+1
        if(not len(self.files)+len(self.folders)==0):
            self.w=WebServer(8056,self.r,self.ui.ngrokCheck.checkState())
            self.setStatus("Sharing")
            self.w.start()
            dialog=SharingDialog(self)
            dialog.ui.sharingLabel.setText("Sharing : "+str(len(self.folders))+" folders and "+str(len(self.files))+" files")
            if(self.w.ngrok):
                dialog.ui.linkLabel.setText("Local : "+socket.gethostbyname(socket.getfqdn())+":8056\nPublic : "+self.w.ngrokUrls[1])
            else:
                dialog.ui.linkLabel.setText("Local : "+socket.gethostbyname(socket.getfqdn())+":8056")
            dialog.exec_()
            self.setStatus("Stopped sharing")
        else:
            self.setStatus("Done")
            dialog=MessageDialog(self,"Nothing to share")
            dialog.allowtoclose()
            dialog.exec()

    def removeItem(self):
        a=self.ui.selectedFiles.selectedIndexes()
        rows=[0]*len(a)
        i=0
        while i<len(a):
            rows[i]=a[i].row()
            try:
                self.files.remove(a[i].data())
            except:
                self.folders.remove(a[i].data())
            i=i+1
        j=0
        k=0
        while j<(len(rows)-1):
            while k<(len(rows)-1-j):
                if rows[k]<rows[k+1]:
                    tmp=rows[k]
                    rows[k]=rows[k+1]
                    rows[k+1]=tmp
                k=k+1
            j=j+1
        for i in rows:
            self.model.removeRow(i)

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.r=WebRoot()
        self.setWindowTitle("Share")
        self.ui.folderButton.clicked.connect(self.folderChooser)
        self.ui.fileButton.clicked.connect(self.fileChooser)
        self.ui.shareButton.clicked.connect(self.run)
        self.ui.selectedFiles.setModel(self.model)
        self.ui.clearButton.clicked.connect(self.clean)
        self.ui.removeButton.clicked.connect(self.removeItem)
        self.setStatus("Done")

    def setStatus(self,status):
        self.ui.status.setText("Status : "+status)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
    sys.exit()
