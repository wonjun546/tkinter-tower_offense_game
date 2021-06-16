from tkinter import *


class Map(Canvas):
    def __init__(self, parent, *args, **kwargs):
        Canvas.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        
