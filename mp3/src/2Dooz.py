"""
Brian T. Bailey
ITM 513 - MP3
2Dooz Main Application File
"""

from Tkinter import *
from domain.gui import AppGui


root = Tk()
myapp = AppGui(root)
root.title('2Dooz')
root.mainloop()