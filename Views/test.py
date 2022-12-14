from tkinter import Label

import PIL
from PIL import ImageTk

load = PIL.Image.open("Output.png")
render = ImageTk.PhotoImage(load)
img = Label(self, image=render)
img.image = render
img.place(x=0, y=0)