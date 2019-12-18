import paho.mqtt.client as mqtt

import paho.mqtt.publish as publish
import time
import random
import cmath
import numpy as np

#Variable Section
broker_address="192.168.0.4"

ran = 0
# End Variable Section

def on_message(client, userdata, message):
		global ran
		print("Message Received = ",str(message.payload.decode("utf-8")))
		print("Message topic = ",message.topic)

def on_connect(client, obj, flags, rc):
		print(str(rc))
		client.subscribe("/Indonesia/Jawabarat/rand")
		client.subscribe("/Indonesia/Jawabarat/tes")

def on_publish(client, obj, mid):
		print(str(mid))

def on_subscribe(client, obj, mid, granted_qos):
		print("Subscribed: " + str(mid) + " " + str(granted_qos))

client = mqtt.Client()
client.on_message=on_message
client.on_connect = on_connect
client.on_publish = on_publish
client.on_subscribe = on_subscribe
client.connect(broker_address) 

client.loop_start()

while True:
	ran = random.randint(1, 1000)
	client.publish("/Indonesia/Jawabarat/rand",ran)
	time.sleep(2)
	
client.loop_stop()
client.disconnect()
