import urllib3
import conf
import json
#import time
from time import sleep
from boltiot import Bolt
URL = "http://api.callmebot.com/text.php?user=anshu_2106&text=Alert! The Current Heart Rate is - "
http = urllib3.PoolManager()
minimum_limit = 57 #the minimum threshold of heart rate
maximum_limit = 100 #the maximum threshold of heart rate
mybolt = Bolt(conf.API_KEY, conf.DEVICE_ID)
#sms = Sms(conf.SID, conf.AUTH_TOKEN, conf.TO_NUMBER, conf.FROM_NUMBER)//
while True:
   response = mybolt.serialRead(0)
   data = json.loads(response)

   sensor_value = data['value']
   
   try:
       sensor_values = data['value'].split('\n')
       for sensor_value in sensor_values:
        if sensor_value != '':
        
            if float(sensor_value) > maximum_limit or float(sensor_value) < minimum_limit:
            #response = sms.send_sms("Alert! The Current Heart Rate is " +str(sensor_value))
                r = http.request('GET', URL +str(sensor_value))
                             
                sleep(10)
           #print(r) 
   except Exception as e:
       print(e)
       #r = http.request('GET', URL +str(sensor_value))
       #print(r)
   