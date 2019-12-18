import paho.mqtt.client as mqtt

import paho.mqtt.publish as publish
import time
import random
import cmath
import numpy as np

#Variable Section
broker_address="192.168.0.4"

run = 0
i = 0 
hasil = 0
rata = 0 
pangkat = 0
hsp = 0
hasilp = 0
hasilr = 0
pangkathr = 0
kuadrat = 0
distribusi = 0
standevkuadrat = 0
standev = 0

flagrun = False
# End Variable Section

def on_message(client, userdata, message):
		global run, pangkat, hsp, hasil, hasilp, i, rata, hasilr, pangkathr, standev, flagrun, distribusi, standevkuadrat
		#print("Message Received = ",str(message.payload.decode("utf-8")))
		run = float(str((message.payload.decode("utf-8"))))
		#print("Message topic = ",message.topic)

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
	pangkat = run*run
	hsp = hsp+pangkat
	hasilr = hasilr+run
	pangkathr = hasilr*hasilr
	i=i+1
	rata = hasil/i
	standevkuadratA = (i*hsp)-pangkathr
	standevkuadratB = i*(i-1)
	try:
		s = standevkuadratA/standevkuadratB
	except ZeroDivisionError:
		s = 0
	standev = np.sqrt(s)
	distribusi = (run-rata)/standev
	client.publish("/Indonesia/Jawabarat/tes",distribusi)
	time.sleep(2)
	
client.loop_stop()
client.disconnect()
