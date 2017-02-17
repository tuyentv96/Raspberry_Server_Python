import MQTTConnection as MQTTC
import json
import threading


class server(threading.Thread):
    def __init__(self, parent=None):
        super(server, self).__init__(parent)
        self.mqtt=MQTTC.MqttClass()
        self.mqtt.start()
        self.mqtt.publish("1122", "333333")
        self.mqtt._mqttc.on_message = self.mqtt_on_message

    def mqtt_on_message(self, mqttc, obj, msg):
        print(msg.topic+"---"+str(msg.qos)+" "+str(msg.payload.decode("utf-8")))
        handleCommandClient(msg,self.mqtt).start()


    def pushlish(self,topic,payload):
        self.mqtt.publish(topic,payload)

class handleCommandClient(threading.Thread):
    def __init__(self,msg,mqttc):
        threading.Thread.__init__(self)
        self.run()
        self.mqttc=mqttc
        #self.msg=msg
        self.loadJson(msg)


    def loadJson(self,msg):
        try:
            json_load = json.loads(msg.payload.decode("utf-8"))

            case = msg.topic[msg.topic.find('/') + 1:]
            if case == "login":
                print("Login handle")
            if case == "control":
                print("Control handle")
            self.mqttc.publish("1122", "333333")
        except:
            print("pare json fail")
            self.mqttc.publish("1122", "333333")

    def run(self):
        print("wrtf")




sev=server()
sev.start()
print("herrrr")

