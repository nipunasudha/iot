from Tkinter import *
from PIL import Image, ImageTk
import json
print('GUI APPLICATION MANAGER')
#-------------------FOR CHILD-----------------------------
sensor_Calibrate = ''
var_type = ''
sensor_ID = ''
sensor_Port = ''
#-----------------------------------------------------------
data = {}
selected_id = ""

val_Broker = ""
val_API_Key = ""
val_Port = ""
val_Terminal_ID = ""

val_Analog_Port = ""
val_Select_Sensor = ""
#-----------Update the json file------------
def update():
    jsonFile = open("../Settings.json", "w+")
    jsonFile.write(json.dumps(data))
    jsonFile.close()
#-----------Read the json file--------------
def read():
    jsonFile = open("../Settings.json", "r")
    data = json.load(jsonFile)
    jsonFile.close()
    return data
#-----------Display some of json values-----
def startUp():
    global data
    data = read()
    broker.delete(0, END)
    broker.insert(0, data['settings']['broker'])
    API_Key.delete(0, END)
    API_Key.insert(0, data['terminal']['apikey'])
    port.delete(0, END)
    port.insert(0, data['settings']['port'])
    terminal_ID.delete(0, END)
    terminal_ID.insert(0, data['terminal']['id'])
#-----------Popup window for adding sensors--
def popupWindow(event):
    global data
    global sensor_Calibrate
    global var_type
    global sensor_ID
    global sensor_Port

    child = Tk()
    x=0
    #------------------------------------------------
    label_type = Label(child, text="Sensor Type:")
    var_type = StringVar(child)
    var_type.set("Temperature")
    option_type = OptionMenu(child, var_type, "Temperature", "Salinity", "Light", "Wind")
    label_type.grid(row=x, sticky=E)
    option_type.config(width=10)
    option_type.grid(row=x, column=2)
    #----------------------------------------------
    label_id = Label(child, text="Sensor ID:")
    sensor_ID = Entry(child)
    sensor_ID.config(width=10)
    label_id.grid(row=x+1, sticky=E)
    sensor_ID.grid(row=x+1, column=2)
    #----------------------------------------------
    label_port = Label(child, text="Connected Port:")
    sensor_Port = Entry(child)
    sensor_Port.config(width=10)
    label_port.grid(row=x+2, sticky=E)
    sensor_Port.grid(row=x+2, column=2)
    #-----------------------------------------------
    label_calib = Label(child, text="Calibrate Value:")
    sensor_Calibrate = Entry(child)
    sensor_Calibrate.config(width=10)
    label_calib.grid(row=x+3, sticky=E)
    sensor_Calibrate.grid(row=x+3, column=2)
    #-----------------------------------------------
    add_Sensor_Submit = Button(child, text="Conform", width=15)
    add_Sensor_Submit.bind("<Button-1>", submit)
    add_Sensor_Submit.grid(row=x+4, column=2)

    child.mainloop()
#-----------Submit the added sensor details--
def submit(event):
    global data, listbox
    sensor = {}
    sensor['calib'] = sensor_Calibrate.get()
    x = var_type.get()
    id = sensor_ID.get()
    port = sensor_Port.get()

    if(x == 'Temperature'):
        x = 'TEMP'
    elif(x == 'Salinity'):
        x = 'SALI'
    elif(x == 'Light'):
        x = 'LIGH'
    elif(x == 'Wind'):
        x = 'WIND'

    sensor['type'] = x
    sensor['id'] = id
    sensor['port'] = port
    data['sensors'].append(sensor)

    update()
    startUp()
    updateCurrentSensors()
#-----------Update the current sensor panel--
def updateCurrentSensors():
    global listbox
    readed = read()

    listbox.delete(0, END)
    for i in readed['sensors']:
        x = i['type']
        y = i['id']
        if(x == 'TEMP'):
            listbox.insert(END, y+'_Temperature')
        elif(x == 'SALI'):
            listbox.insert(END, y+'_Salinity')
        elif(x == 'LIGH'):
            listbox.insert(END, y+'_Light')
        elif(x == 'WIND'):
            listbox.insert(END, y+'_Wind')
#-----------Update data we provided----------
def updateData(event):
    global data
    val_Broker = broker.get()
    val_API_Key = API_Key.get()
    val_Port = port.get()
    val_Terminal_ID = terminal_ID.get()

    data['settings']['broker'] = val_Broker
    data['terminal']['apikey'] = val_API_Key
    data['settings']['port'] = val_Port
    data['terminal']['id'] = val_Terminal_ID

    update()
    startUp()
#--------------------Show data of selected sensor------------
def showMyDetails(event):
    global listbox, data, selected_id
    widget = event.widget
    selection = widget.curselection()
    value = widget.get(selection[0])

    temp = value.split('_')

    selected_id = temp[0]

    for i in data['sensors']:
        if(i['id'] == selected_id):

            type = i['port'][0]
            number = i['port'][1:]

            if(type == 'D'):
                value = 'Digital Port '+number
                var.set(value)
            elif(type == "A"):
                value = 'Analog Port '+number
                var.set(value)

            calibrate.delete(0, END)
            calibrate.insert(END, i['calib'])

#------------------------------------------------------------
def modifySelected(event):
    global selected_id, data
    print 'I am in'
    for i in data['sensors']:
        if(i['id'] == selected_id):
            new_port = (var.get().split(" "))[0][0]+(var.get().split(" "))[2]
            i['port'] = new_port
            cali = calibrate.get()
            i['calib'] = cali

    update()
    updateCurrentSensors()
    autoReset()

def removeSelected(event):
    global selected_id, data
    for i in data['sensors']:
        if(i['id'] == selected_id):
            del data['sensors'][data['sensors'].index(i)]
    update()
    updateCurrentSensors()
    autoReset()

def autoReset():
    var.set("None")
    calibrate.delete(0, END)
    calibrate.insert(END, "None")

root = Tk()

root.title('Terminal Config')


image = Image.open("Header.png")
image = image.resize((500, 60), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)

label = Label(root, image=photo)
label.grid(columnspan=4)
label.grid(rowspan=2)
#--------------------------------------------------------
label_title = Label(root, text="MQTT Network Settings")
label_title.grid(row=3, sticky=W)
label_title.grid(columnspan=2, sticky=W)
#--------------------------------------------------------
x=4
label_Broker = Label(root, text="Broker")
label_API_Key = Label(root, text="API Key")
label_Broker.grid(row=x, sticky=E)
label_API_Key.grid(row=x+1, sticky=E)

broker = Entry(root)
API_Key = Entry(root)

broker.grid(row=x, column=1)
API_Key.grid(row=x+1, column=1)
#--------------------------------------------------------
label_Port = Label(root, text="Port")
label_Terminal_ID = Label(root, text="Terminal ID")
label_Port.grid(row=x, column=2, sticky=E)
label_Terminal_ID.grid(row=x+1, column=2, sticky=E)

port = Entry(root)
terminal_ID = Entry(root)

port.grid(row=x, column=3)
terminal_ID.grid(row=x+1, column=3)
#--------------------------------------------------------
button_update = Button(root, text="Update", width=15)
button_update.bind("<Button-1>", updateData)
button_update.grid(row=x+2, column=3)
#--------------------------------------------------------
label_title = Label(root, text="Sensor Settings")
label_title.grid(row=7, sticky=W)
label_title.grid(columnspan=2, sticky=W)

add_Sensor = Button(root, text="Add Sensor", width=15)
add_Sensor.bind("<Button-1>",popupWindow)
add_Sensor.grid(row=8, column=1)
#--------------------------------------------------------
t = 9
listbox = Listbox(root, height=4,width=1, bg="white")
scroll = Scrollbar(root, orient=VERTICAL)
listbox.config(yscrollcommand=scroll.set)
scroll.config(command=listbox.yview)

listbox.grid(row=t, column=1, rowspan=4, columnspan=1, sticky=N+E+W+S)
listbox.bind("<Double-Button-1>",showMyDetails)
listbox.columnconfigure(t,weight=1)

scroll.grid(row=t, column=1, rowspan=4, sticky=N+E+S)

#--------------------------------------------------------
label_Digital_Port = Label(root, text="Analog/Digital Port")
label_Digital_Port.grid(row=9, column=2, sticky=E)

var = StringVar(root)
var.set("None")
option_1 = OptionMenu(root, var, "None", "Analog Pin 01", "Analog Pin 02", "Analog Pin 03", "Digital Pin 01", "Digital Pin 02", "Digital Pin 03")
option_1.config(width=14)
option_1.grid(row=9, column=3)
#---------------------------------------------------------
label_Calibrate = Label(root, text="Calibrate Value")
label_Calibrate.grid(row=10, column=2, sticky=E)
calibrate = Entry(root)
calibrate.grid(row=10, column=3)
calibrate.insert(0, "None")
#----------------------------------------------------------
modify_Selected = Button(root, text="Modify Selected", width=15)
modify_Selected.bind("<Button-1>",modifySelected)
modify_Selected.grid(row=11, column=2)
#----------------------------------------------------------
remove_Selected = Button(root, text="Remove Selected", width=15)
remove_Selected.bind("<Button-1>",removeSelected)
remove_Selected.grid(row=11, column=3)
#------------------------------------------------------------------------
last = Label(root, text="",height=1)
last.grid(row=13, columnspan=4, sticky=E)

startUp()
updateCurrentSensors()

#---------------------------------------------------------------------
root.mainloop()
