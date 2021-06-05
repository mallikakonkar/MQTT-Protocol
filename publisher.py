import paho.mqtt.client as mqtt
import smtplib

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully")
    else:
        print("Connect returned result code: " + str(rc))

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("Received message: " + msg.topic + " -> " + msg.payload.decode("utf-8"))

# create the client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# enable TLS
client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)

# set username and password
client.username_pw_set("Kashvi", "Kashvi123")

# connect to HiveMQ Cloud on port 8883
client.connect(host="df017b0412514241b1d6a3a7496e4318.s1.eu.hivemq.cloud", port=8883, keepalive=60)

mess=input("Enter the message you want to publish:")
mail=input("Enter your email ID to get the published messages:")



# publish "Hello" to the topic "my/test/topic"
client.publish("my/test/topic", mess)

# s = smtplib.SMTP('smtp.gmail.com', 587)
# s.starttls()
  
# # Authentication
# #s.login("greatx94@gmail.com", "shreyask")
  
# # message to be sent

# message = mess
  
# # sending the mail
# #s.sendmail("greatx94@gmail.com",mail, message)
  
# # terminating the session
# s.quit()
# Blocking call that processes network traffic, dispatches callbacks and handles reconnecting.
client.loop_forever()