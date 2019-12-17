import paho.mqtt.client as mqtt
import time
import random
import cmath
import numpy as np

def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic = ",message.topic)
	
broker_address="192.168.0.4"
client = mqtt.Client()
client.on_message=on_message 
client.connect(broker_address) 
client.loop_start()


while True:
	client.subscribe("/Indonesia/Jawabarat/rand")
	ran = random.randint(1, 1000)
	client.publish("/Indonesia/Jawabarat/rand",ran)
	time.sleep(2)
	
client.loop_stop()
client.disconnect()