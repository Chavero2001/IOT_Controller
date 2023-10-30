import paho.mqtt.client as mqtt

import sqlite3
import json
from datatime import datetime

MQTT_BROKER = "localhost"
MQTT_CLIEN_ID = "historian-client"
MQTT_TOPIC = "#"

DB_FILE = "historian_data.db"

#MQTT Client callback for connection - the method that will be once connected to the broker 

def on_connect (clien, userdata, flags, rc):
    print("connected to MQTT")
    #subscribe to the topics
    client.subscribe(MQTT_TOPIC)

#MQTT callback
def on_message(client, userdata, msg):
   #Get value
   payload = msg.payload.()
   #get topic
   topic = msg.topic
   #get timestapm
   timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
   #save to the data base
   save_to_database(topic,payload,timestamp)

#method to save to SQLite 3 database
def  save_to_database(topic,value,timestamp)
   #connect to database
   conn = sqlite3.connect (DB_FILE)
   cursor = conn.cursor()
   #make sue the DB exists 
   SQL = "CREATE TABLE historian_data (topic TEXT, payload TEXT, timestamp TEXT)"
   cursor.execute(SQL)
   #save the message to the table
   SQL = "INSERT INTO historian_data (topic, payload, timestamp) VALUES (?,?,?)"
   data.execute(SQL, (topic, payload, timestamp))

   conn.commit()
   conn.close()

client = mqtt.Client(client_id=MQTT_CLIENT_ID)

#Setting up the obkect
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_BROKER, 1883, 60)

#Loop MQTT bu let define further logic
client.loop_start()

try:
   while True:
     pass

except KeyboardInterrupt:
   client.disconnect()

