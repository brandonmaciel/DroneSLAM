# API to get data from lidar sensor

import random
from common.range import *

class LIDAR:

	def __init__(self):
		self.range = LONG_RANGE
		print("lidar class initialized")
	
	# Read distance from lidar/time-of-flight sensor. Based on VL53L1X Time-of-Flight Distance Sensor (400 cm max sensing distance) 
	def get_distance(self):
		return [random.randint(1, 400), random.randint(1, 400), random.randint(1, 400)];
	
	# Set range distance: LONG_RANGE, MEDIUM_RANGE, SHORT_RANGE
	def set_range(self, range):
		self.range = range

