import paho.mqtt.client as mqtt

import threading

# The callback for when the client receives a CONNACK response from the server.



class MqttClass (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self._mqttc = mqtt.Client("123")
        #self._mqttc.on_message = self.mqtt_on_message
        self._mqttc.on_connect = self.mqtt_on_connect
        self._mqttc.on_publish = self.mqtt_on_publish
        self._mqttc.on_subscribe = self.mqtt_on_subscribe
        self.clientid="123"
    def mqtt_on_connect(self, mqttc, obj, flags, rc):
        print("on connect with rc: "+str(rc))
    def mqtt_on_publish(self, mqttc, obj, mid):
        print("mid: "+str(mid))
    def mqtt_on_subscribe(self, mqttc, obj, mid, granted_qos):
        print("Subscribed: "+str(mid)+" "+str(granted_qos))
    def mqtt_on_log(self, mqttc, obj, level, string):
        print(string)
    def publish(self,topic,msg):
         self._mqttc.publish(topic,msg)
    def run(self):
        self._mqttc.on_connect = self.mqtt_on_connect
        self._mqttc.connect("trantuyen.name.vn", 1883, 60)
        self._mqttc.subscribe("+/login", 0)
        self._mqttc.subscribe("+/control", 0)
        self._mqttc.publish("111","222")
        rc = 0
        while rc == 0:
            rc = self._mqttc.loop()
        return rc
