import VS
import debug
import sys


class MyAI(VS.PythonAI):
    def init(self,un):
        self.XMLScript ("++turntowards.xml")
        self.AddReplaceLastOrder(1)
    def Execute(self):
        VS.PythonAI.Execute(self);
        debug.info('h')
        return ''

hi1 = MyAI()
debug.info('AI creation successful')
hi1 = 0
#: 1.7; previous revision: 1.6
