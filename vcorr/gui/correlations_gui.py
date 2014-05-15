# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Diego/Documents/GitHub/correlation_viewer/vcorr\gui\correlations_gui.ui'
#
# Created: Wed May 14 20:22:30 2014
#      by: PyQt4 UI code generator 4.10.3
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

class Ui_correlation_app(object):
    def setupUi(self, correlation_app):
        correlation_app.setObjectName(_fromUtf8("correlation_app"))
        correlation_app.resize(1285, 544)
        self.centralwidget = QtGui.QWidget(correlation_app)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.list_frame = QtGui.QFrame(self.centralwidget)
        self.list_frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.list_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.list_frame.setObjectName(_fromUtf8("list_frame"))
        self.verticalLayout = QtGui.QVBoxLayout(self.list_frame)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.list_frame)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.variables_list = QtGui.QListView(self.list_frame)
        self.variables_list.setFrameShape(QtGui.QFrame.NoFrame)
        self.variables_list.setAlternatingRowColors(True)
        self.variables_list.setWordWrap(True)
        self.variables_list.setObjectName(_fromUtf8("variables_list"))
        self.verticalLayout.addWidget(self.variables_list)
        self.horizontalLayout.addWidget(self.list_frame)
        self.cor_mat_frame = QtGui.QFrame(self.centralwidget)
        self.cor_mat_frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.cor_mat_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.cor_mat_frame.setObjectName(_fromUtf8("cor_mat_frame"))
        self.horizontalLayout.addWidget(self.cor_mat_frame)
        self.reg_frame = QtGui.QFrame(self.centralwidget)
        self.reg_frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.reg_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.reg_frame.setObjectName(_fromUtf8("reg_frame"))
        self.horizontalLayout.addWidget(self.reg_frame)
        self.horizontalLayout.setStretch(1, 5)
        self.horizontalLayout.setStretch(2, 5)
        correlation_app.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(correlation_app)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1285, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        correlation_app.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(correlation_app)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        correlation_app.setStatusBar(self.statusbar)
        self.actionSave_Scenario = QtGui.QAction(correlation_app)
        self.actionSave_Scenario.setObjectName(_fromUtf8("actionSave_Scenario"))
        self.actionLoad_Scenario = QtGui.QAction(correlation_app)
        self.actionLoad_Scenario.setObjectName(_fromUtf8("actionLoad_Scenario"))
        self.actionSave_Matrix = QtGui.QAction(correlation_app)
        self.actionSave_Matrix.setObjectName(_fromUtf8("actionSave_Matrix"))
        self.actionSave_Scatter = QtGui.QAction(correlation_app)
        self.actionSave_Scatter.setObjectName(_fromUtf8("actionSave_Scatter"))
        self.menuFile.addAction(self.actionSave_Matrix)
        self.menuFile.addAction(self.actionSave_Scatter)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(correlation_app)
        QtCore.QMetaObject.connectSlotsByName(correlation_app)

    def retranslateUi(self, correlation_app):
        correlation_app.setWindowTitle(_translate("correlation_app", "Correlations", None))
        self.label.setText(_translate("correlation_app", "Select Variables:", None))
        self.menuFile.setTitle(_translate("correlation_app", "File", None))
        self.actionSave_Scenario.setText(_translate("correlation_app", "Save Scenario", None))
        self.actionLoad_Scenario.setText(_translate("correlation_app", "Load Scenario", None))
        self.actionSave_Matrix.setText(_translate("correlation_app", "Save Matrix", None))
        self.actionSave_Scatter.setText(_translate("correlation_app", "Save Scatter", None))

