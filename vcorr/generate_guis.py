__author__ = 'Diego'

import os
import PyQt4.uic

if __name__ == '__main__':
    this_dir=os.path.dirname(__file__)
    qt_gui_dir=os.path.join(this_dir,'gui')

    PyQt4.uic.compileUiDir(qt_gui_dir)

