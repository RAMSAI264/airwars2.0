from mcp3208 import MCP3208
import time
import RPi.GPIO as GPIO
#import urllib as url
import urllib3
import sys
import dht11
myApi='BX6XQXZTWEE9D8WE'
baseURL="https://api.thingspeak.com/update?api_key=%s" %myApi

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
LED=21
GPIO.setup(LED,GPIO.OUT)
adc= MCP3208()

def Map(x,in_min,in_max,out_min,out_max):
	return (x - in_min)*(out_max - out_min)/(in_max - in_min)+out_min

while True:
	try:

		MQ2=adc.read(0)
		MQ9=adc.read(1)
		MQ135=adc.read(2)
		instance=dht11.DHT11(pin=18)
		result=instance.read()
		smoke=int(Map(MQ2,0,4095,0,100))
		carbon=int(Map(MQ9,0,4095,0,14))
		NH3=int(Map(MQ135,0,4095,10,300))
		Benzene=int(Map(MQ135,0,4095,10,1000))
		Air=int(Map(MQ135,0,4095,10,500))
		time.sleep(2)
		print("Smoke level = ",smoke)
		print("Carbon level = ",carbon)
		print("NH3 = ",NH3)
		temp=result.temperature
		if(temp==0):
			pass
		else:
			print("Temperature: %d C" % result.temperature)
		#print("Alchohol=",Alchohol)
		print("Benzene",Benzene)
		http = urllib3.PoolManager()
		#conn=http.request('GET',baseURL + '&field1=%s&field2=%s&field3=%s' %(smoke,carbon,AirQ))
		#conn.read()
		#conn.close()
	
	except KeyboardInterrupt:
		GPIO.output(LED,GPIO.LOW)
		print("Reading Stopped")
GPIO.cleanup()
