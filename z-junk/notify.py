from Tkinter import *
from PIL import Image, ImageTk
import json
from time import sleep

root = Tk()

root.resizable(height=False, width=False )
root.title('Data Uploaded')
# root.iconbitmap('R2D2.ico')

image = Image.open("Header.png")
image = image.resize((500, 60), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)

label = Label(root, image=photo)
label.grid(columnspan=4)
label.grid(rowspan=2)



root.geometry('%dx%d+%d+%d' % (200, 100, 0, 0))
root.after(3000, lambda: root.destroy())
#---------------------------------------------------------------------
root.mainloop()


