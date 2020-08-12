import requests
import json
from PIL import Image, ImageTk
import os
from tkinter import Tk, Button, Canvas, PhotoImage

imageSoleil = 'Desktop/weather/openImagePython/test/SOLEIL2.png'

fenetre = Tk()
fenetre.attributes('-fullscreen', True)

w, h = fenetre.winfo_screenwidth(),fenetre.winfo_screenheight()

image = Image.open(imageSoleil)
image = image.resize((w, h))

photo = ImageTk.PhotoImage(image)

can = Canvas(fenetre, highlightthickness=0)
can.create_image(0, 0, anchor='nw', image=photo)
can.pack(fill='both', expand=1)

Button(can,text='Quitter', command=fenetre.destroy).pack()

fenetre.mainloop()


