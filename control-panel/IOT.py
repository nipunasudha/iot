from Tkinter import *
from PIL import Image, ImageTk
import json

#-----------------------------------------------------------
data = [[]]
val_Broker = ""
val_API_Key = ""
val_Port = ""
val_Terminal_ID = ""

val_Analog_Port = ""
val_Select_Sensor = ""

def update():
    jsonFile = open("../Settings.json", "w+")
    jsonFile.write(json.dumps(data))
    jsonFile.close()
def read():
    jsonFile = open("../Settings.json", "r")
    data = json.load(jsonFile)
    jsonFile.close()
    return data
def getData(event):
    val_Broker = broker.get()
    val_API_Key = API_Key.get()
    val_Port = port.get()
    val_Terminal_ID = terminal_ID.get()

    val_Analog_Port = var.get()
    val_Select_Sensor = listbox.get(ACTIVE)

    print val_Broker
    print val_API_Key
    print val_Port
    print val_Terminal_ID

    print val_Analog_Port
    print val_Select_Sensor
#------------------------------------------------------------
root = Tk()

image = Image.open("Header.png")
image = image.resize((600, 72), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)

label = Label(root, image=photo)
label.grid(columnspan=4)
label.grid(rowspan=2)

#--------------------------------------------------------
frame = Frame(root,width=500, height=10)
frame.grid(row=12, columnspan=4)
#--------------------------------------------------------
label_title = Label(root, text="MQTT Network Settings")
label_title.grid(columnspan=1)
label_title.grid(row=3)
#--------------------------------------------------------
x=4
label_Broker = Label(root, text="Broker")
label_API_Key = Label(root, text="API Key")
label_Broker.grid(row=x)
label_API_Key.grid(row=x+1)

broker = Entry(root)
API_Key = Entry(root)

broker.grid(row=x, column=1)
API_Key.grid(row=x+1, column=1)
#--------------------------------------------------------
label_Port = Label(root, text="Port")
label_Terminal_ID = Label(root, text="Terminal ID")
label_Port.grid(row=x, column=2)
label_Terminal_ID.grid(row=x+1, column=2)

port = Entry(root)
terminal_ID = Entry(root)

port.grid(row=x, column=3)
terminal_ID.grid(row=x+1, column=3)
#--------------------------------------------------------
button_update = Button(root, text="Update", width=15)
button_update.bind("<Button-1>", getData)
button_update.grid(row=x+2, column=3)
#--------------------------------------------------------
label_title = Label(root, text="Sensor Settings")
label_title.grid(row=7)

add_Sensor = Button(root, text="Add Sensor", width=15)
add_Sensor.grid(row=8, column=1)

label_Analog_Port = Label(root, text="Port")
label_Analog_Port.grid(row=9, column=2)

var = StringVar(root)
var.set("1")
option = OptionMenu(root, var, "1", "2", "3")
option.grid(row=9, column=3)

calibrate_Sensor = Button(root, text="Calibrate Sensor", width=15)
calibrate_Sensor.grid(row=10, column=3)

remove_Selected = Button(root, text="Remove Selected", width=15)
remove_Selected.grid(row=11, column=3)


listbox = Listbox(root, width=20, height=10)

listbox.insert(END, "Temperature Sensor")
listbox.insert(END, "Salinity Sensor")
listbox.insert(END, "Light Sensor")
listbox.insert(END, "Wind Sensor")

listbox.grid(row=9, column=1)

#------------------------------------------------------------------------

# data=read()
# print(data['terminal']['id'])
# data['terminal']['id']="T00001"
# update()
# print(data['terminal']['id'])


#---------------------------------------------------------------------
root.mainloop()
