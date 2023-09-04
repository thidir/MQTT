import paho.mqtt.client as mqtt
import time

name = input("name")
Connected = False  # global variable for the state of the connection

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected  # Use global variable
        Connected = True  # Signal connection

    else:
        print("Connection failed")
      
      
client = mqtt.Client()
client.on_connect = on_connect
client.connect("2.tcp.eu.ngrok.io", 17913, 60)
client.loop_start()  # start the loop

while Connected != True:  # Wait for connection
    time.sleep(0.1)

client.publish(name + " just joined")
try:
    while True:
        message = input('Your message: ')
        client.publish("glblcd","HTU/" + name + ":" +message)
       

except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()