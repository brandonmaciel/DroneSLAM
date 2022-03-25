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
	
	points = [[0, 0, 0]]
	for x in range(10):
		v.clear()
		points = np.concatenate((points, np.random.rand(100, 3)))
		cview = get_camera_view()
		v.load(points, points[:, 2])
		v.set(lookat=cview['lookat'], phi=cview['phi'], r=cview['r'], theta=cview['theta'])
		time.sleep(1)
	
	


if __name__ == "__main__":
	main()
