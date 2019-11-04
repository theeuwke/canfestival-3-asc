# this could probably done more efficient, but I'm just a python beginner, be gentle ;-)

import os
import os.path
import shutil

lib_path = os.path.join('lib', 'canfestival-3-asc')

shutil.rmtree(lib_path, ignore_errors=True)
os.mkdir(lib_path)

for root, dirs, files in os.walk('canfestival-3-asc/src'):
	for file in files:
		if file.endswith('.c') or file.endswith('.h'):
			if file.find("symbols.c") is -1:
				print("copy: " + file)
				shutil.copy2(os.path.join(root, file), lib_path)
#
# skip this, these aren't compatible with Stm32CubeMX
#
# for root, dirs, files in os.walk('canfestival-3-asc/drivers/cm3'):
#	for file in files:
#		if file.endswith('.c') or file.endswith('.h'):
#			print "copy: " + file
#			shutil.copy2(os.path.join(root, file), lib_path)

for file in os.listdir("canfestival-3-asc/include"):
	if file.endswith('.h'):
		print("copy: " + file)
		shutil.copy2(os.path.join("canfestival-3-asc/include", file), lib_path)

for file in os.listdir("canfestival-3-asc/include/cm4"):
	if file.endswith('.h'):
		print("copy: " + file)
		shutil.copy2(os.path.join("canfestival-3-asc/include/cm4", file), lib_path)

for file in os.listdir("canfestival-3-asc/include/default"):
	if file.endswith('.h'):
		print("copy: " + file)
		shutil.copy2(os.path.join("canfestival-3-asc/include/default", file), lib_path)
