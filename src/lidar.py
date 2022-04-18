# API to get data from lidar sensor

import random
from common.range import *
import serial

class LIDAR:

	def __init__(self):
		self.ranging = LONG_RANGE
		self.sensor = serial.Serial(port='/dev/tty.usbmodem1413101', baudrate=115200)
		print("lidar class initialized")
	
	# Based on the Spherical Coordinate System	
	def set_position(self, r, theta, phi):
		print("position set: r = {}, theta = {}, phi = {}".format(r, theta, phi))
		
	# Read distance from lidar/time-of-flight sensor. Based on VL53L1X Time-of-Flight Distance Sensor (400 cm max sensing distance) 
	# Distance Sensor only provides a distance perpendicular to the sensor face. Knowing sensor physical position and angle is important.
	def get_distance(self):
		# return [random.randint(1, 400), random.randint(1, 400), random.randint(1, 400)];
		self.clear_sensor_buffer()
		return [0, 0, int(self.sensor.readline().decode()[:-2])/4000]
	
	def close_connection(self):
		self.sensor.close()
		print("connection to arduino successfully closed")

	def clear_sensor_buffer(self):
		while self.sensor.inWaiting() > 0:
			self.sensor.readline()
	
	# Set range distance: LONG_RANGE, MEDIUM_RANGE, SHORT_RANGE
	def set_range(self, ranging):
		self.ranging = ranging
