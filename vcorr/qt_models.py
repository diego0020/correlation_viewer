__author__ = 'Diego'

import PyQt4.QtCore as QtCore
from PyQt4.QtCore import QAbstractListModel
from PyQt4.QtCore import QAbstractTableModel, QAbstractItemModel
import pandas as pd

class VarListModel(QAbstractListModel):
    CheckedChanged = QtCore.pyqtSignal(list)
    def __init__(self, outcome_var=None, parent=None, checkeable=False):
        QAbstractListModel.__init__(self, parent)
        self.variables_list = []
        self.header = "Variable"
        self.outcome = outcome_var
        self.checkeable = checkeable
        self.checked_set = None
        if checkeable:
            self.checked_set = set()


    def set_variables(self,vars_list):
        self.variables_list = vars_list
        self.modelReset.emit()


    def rowCount(self, QModelIndex_parent=None, *args, **kwargs):
        return len(self.variables_list)

    def data(self, QModelIndex, int_role=None):
        idx = QModelIndex.row()
        if 0 <= idx < len(self.variables_list):
            if int_role == QtCore.Qt.DisplayRole:
                return self.variables_list[idx]
            elif (self.checkeable is True) and (int_role == QtCore.Qt.CheckStateRole):
                if self.variables_list[idx] in self.checked_set:
                    return QtCore.Qt.Checked
                else:
                    return QtCore.Qt.Unchecked
        else:
            return QtCore.QVariant()

    def headerData(self, p_int, Qt_Orientation, int_role=None):
        if int_role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()
        if Qt_Orientation == QtCore.Qt.Horizontal and p_int == 0:
            return self.header
        else:
            return QtCore.QVariant()

    def sort(self, p_int, Qt_SortOrder_order=None):
        reverse = True
        if Qt_SortOrder_order == QtCore.Qt.DescendingOrder:
            reverse = False
        self.variables_list.sort(reverse=reverse)
        self.modelReset.emit()

    def flags(self, QModelIndex):
        idx = QModelIndex.row()
        if (QModelIndex.column() == 0) and (0 <= idx < len(self.variables_list)):
            flag = QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
            if self.checkeable is True:
                flag |= QtCore.Qt.ItemIsUserCheckable
            return flag

        else:
            return QtCore.Qt.NoItemFlags

    def setData(self, QModelIndex, QVariant, int_role=None):
        if not int_role == QtCore.Qt.CheckStateRole:
            return False
        else:
            idx = QModelIndex.row()
            if QVariant.toBool() is True:
                self.checked_set.add(self.variables_list[idx])
            else:
                self.checked_set.remove(self.variables_list[idx])
            self.CheckedChanged.emit(sorted(self.checked_set))
            return True


    def select_items_by_name(self, items_list):
        for i in items_list:
            self.checked_set.add(i)


