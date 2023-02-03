from tkinter import *
import random
import sys
import cv2
import paho.mqtt.client as mqtt
import numpy as np
import time

win_img = cv2.imread("win.png", 1)
lose_img = cv2.imread("lose.png", 1)
draw_img = cv2.imread("draw.png", 1)
# 0. define callbacks - functions that run when events happen.
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
  print("Connection returned result: " + str(rc))
  # Subscribing in on_connect() means that if we lose the connection and
  # reconnect then subscriptions will be renewed.
  client.subscribe("ece180da_SB2/test")
# The callback of the client when it disconnects.
def on_disconnect(client, userdata, rc):
  if rc != 0:
    print('Unexpected Disconnect')
  else:
    print('Expected Disconnect')
# The default message callback.
# (won't be used if only publishing, but can still exist)
def on_message(client, userdata, message):

    result = (str(message.payload))
    print(result)
    
#    if result == 'You lose.':
#        cv2.imshow("Lose", lose_img)
#        cv2.waitKey(3000)
#        cv2.destroyAllWindows()
 #   elif result == 'You win!':

#        cv2.imshow("Win", win_img)
#        cv2.waitKey(3000)
 #       cv2.destroyAllWindows()
 #   else:
 ##       cv2.imshow("Draw", draw_img)
 #       cv2.waitKey(3000)
 #       cv2.destroyAllWindows()
        
# 1. create a client instance.
client = mqtt.Client()
# add additional client options (security, certifications, etc.)
# many default options should be good to start off.
# add callbacks to client.
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message
# 2. connect to a broker using one of the connect*() functions.
# client.connect_async("test.mosquitto.org")
client.connect_async('mqtt.eclipseprojects.io')
# 3. call one of the loop*() functions to maintain network traffic flow with the broker.
client.loop_start()
# 4. use subscribe() to subscribe to a topic and receive messages.
# 5. use publish() to publish messages to the broker.

# payload must be a string, bytearray, int, float or None.

while True:
    client.on_message = on_message
    userinput = input("Enter a choice (rock, paper, scissors): ")
    client.publish("ece180da_SB1/test", userinput, qos=1)
    print('Published!')

    client.on_message = on_message
    time.sleep(10)
    pass



client.loop_stop()
client.disconnect()



