import paho.mqtt.client as mqtt
import json
from data import Data


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("#")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    try:
        json_payload = json.loads(msg.payload)
        if msg.topic == "/feeds/battery":
            Data.instance().battery = json_payload["percentage"]
        elif msg.topic == "/feeds/temp":
            Data.instance().drum_temp = json_payload["env"]
            Data.instance().bean_temp = json_payload["bean"]
    except:
        print("MQTT - non json message, ignoring")


def setup():
    client = mqtt.Client()
    client.username_pw_set("roaster", "roastervole")
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("localhost", 1883, 60)
    client.loop_start()
