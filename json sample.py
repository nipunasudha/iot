import json
def update():
    jsonFile = open("Settings.json", "w+")
    jsonFile.write(json.dumps(data))
    jsonFile.close()
def read():
    jsonFile = open("Settings.json", "r")
    data = json.load(jsonFile)
    jsonFile.close()
    return data
#------------------------------------------------------------
data=read()
print(data['terminal']['id'])
data['terminal']['id']="T00001"
update()
print(data['terminal']['id'])
