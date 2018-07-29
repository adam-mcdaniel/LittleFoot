# This file is a replacement for the vex module  \
# because we don't have access to the vex module \
# replace this file with the actual module if    \
# the sourcecode is accessable


class Motor:
	def __init__(self, *a, **k):
		pass

	def run(self, *a, **k):
		pass

	def off(self, *a, **k):
		pass

class Joystick:
	
	def __init__(self, *a, **k):
		pass

	axis1 = laxis2 = axis3 = \
	axis4 = b5up = b5down = \
	b6up = b6down = b7up = \
	b7down = b7left = \
	b7right = b8up = \
	b8down = b8left = \
	b8right = lambda *a, **k: 0
		
		
