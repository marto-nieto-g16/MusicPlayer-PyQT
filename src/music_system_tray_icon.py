# -*- encoding:utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.phonon import Phonon

try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _toUtf8 = QString.toUtf8
except AttributeError:
    def _toUtf8(s):
        return s

class MusicSystemTray(QSystemTrayIcon):
    def __init__(self, parent=None):
        QSystemTrayIcon.__init__(self, parent)
        self._parent = parent

        menu = QMenu()
        self.showAction = QAction(u'Abre la interfaz principal', self)
        self.playAction = QAction(u'Start', self)
        self.lastAction = QAction(u'Anterior', self)
        self.nextAction = QAction(u'Siguiente', self)
        self.stopAction = QAction(u'Stop', self)
        self.stopAction.setEnabled(False)
        self.exitAction = QAction(u'Salir', self)

        menu.addAction(self.showAction)
        menu.addSeparator()
        menu.addAction(self.playAction)
        menu.addSeparator()
        menu.addAction(self.lastAction)
        menu.addSeparator()
        menu.addAction(self.nextAction)
        menu.addSeparator()
        menu.addAction(self.stopAction)
        menu.addSeparator()
        menu.addAction(self.exitAction)

        self.connect(self.showAction, SIGNAL('triggered()'), parent.showNormal)
        self.connect(self.playAction, SIGNAL('triggered()'), parent.playControl)
        self.connect(self.lastAction, SIGNAL('triggered()'), parent.lastMusic)
        self.connect(self.nextAction, SIGNAL('triggered()'), parent.nextMusic)
        self.connect(self.stopAction, SIGNAL('triggered()'), parent.stop)
        self.connect(self.exitAction, SIGNAL('triggered()'), parent.close)

        self.setContextMenu(menu)

    def updateMenu(self):
        state = self._parent.mediaObject.state()
        if state == Phonon.PlayingState:
            self.playAction.setText(u"Play")
            self.stopAction.setEnabled(True)
        elif state == Phonon.PausedState:
            self.playAction.setText(u"Play")
            self.stopAction.setEnabled(True)
        elif state == Phonon.StoppedState:
            self.playAction.setText(u"Stop")
            self.stopAction.setEnabled(False)

