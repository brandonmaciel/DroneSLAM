import pptk
import numpy as np
import pandas as pd
from common.range import *
import lidar
import time

# def get_camera_view():
	# example usage:
	#	# assume viewer has been initialized as v
	#	cview = get_camera_view()
	#	v.set(lookat=cview['lookat'], phi=cview['phi'], r=cview['r'], theta=cview['theta'])
#	return {"lookat": v.get('lookat'), "phi": v.get('phi'), "r": v.get('r'), "theta": v.get('theta')}

def main():
	print("Starting slam")

	v = pptk.viewer([[0, 0, 0]])
	v.clear()
	v.set(point_size=0.0005)
	sns = lidar.LIDAR()
	
#	points = [[0, 0, 0]]
	x = 0.15
	points = [[x, x, 0], [-x, x, 0], [-x, -x, 0], [x, -x, 0]]

	for _ in range(20):
		v.clear()
		sns.clear_sensor_buffer()
		points.extend([sns.get_distance()])
		v.load(points, [i[2] for i in points])	
	

	v.wait()
	v.close()
	sns.close_connection()

if __name__ == "__main__":
	main()
