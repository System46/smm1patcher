import os, tkinter
from tkinter import filedialog

home = os.path.expanduser('~')
root = tkinter.Tk()
root.withdraw()
print('Select A Super Mario Maker 1 Binary File.')
binary_path = filedialog.askopenfilename(initialdir = home + "/Desktop",title = "Select A Super Mario Maker 1 Binary File",filetypes = ([("All Files","*.*")]))
os.system('py -i smm1patcher.py ' + binary_path)
