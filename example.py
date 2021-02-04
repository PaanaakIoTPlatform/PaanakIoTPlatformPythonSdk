import Paanaak

device=Paanaak.PaanaakDevice(secret_key="5e1c175a-d830-42b8-8ac2-3627f5cff818")
#this method adds a sensor with name and type(float,bool,string)
device.add_sensor(name="temperature",data_type="float")
device.add_sensor(name="power",data_type="bool")
device.add_sensor(name="status",data_type="str")
#this method create and send and http request to cloud and get the 
# current state of relays as a bit array
print(device.send_sensors_and_relays(    
    {
        "temperature":12.0,
        "power":True,        
    },state="10"))

