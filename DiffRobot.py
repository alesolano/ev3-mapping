#!/usr/bin/python

from ev3dev.auto import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from time import sleep
PI = 3.141592653589793

class DiffRobot(object): # do i need to inherit object?
	"""docstring for DiffRobot"""
	def __init__(self, diam, width, r_address=OUTPUT_A, l_address=OUTPUT_B):
		super(DiffRobot, self).__init__() # understand
		self.diam = diam
		self.width = width
		self.motors = [LargeMotor(address) for address in (r_address, l_address)]

	def go_forwards(self, distance=None, dc=60):
		"""docstring for go_forwards"""
		if distance != None:

			turns = distance/(self.diam * PI)

			for m in self.motors:
				m.duty_cycle_sp = dc
				m.position = turns*360
				m.run_to_abs_pos()
			while 'running' in self.motors[0].state: sleep(0.01)

		else:
			for m in self.motors:
				m.duty_cycle_sp = dc
				m.run_direct()

	def go_backwards(self, distance=None, dc=60):
		if distance != None: distance = -distance
		self.go_forwards(distance, -dc)

	def turn_left(self, angle=None, dc=60):
		"""docstring for turn_right"""
		if angle != None:

			turns_per_spin = self.width/self.diam
			turns = (angle/360) * turns_per_spin

			for m in self.motors:
				m.duty_cycle_sp = dc
				m.position = turns*360
				m.run_to_abs_pos()
				dc = -dc
				turns = -turns
			while 'running' in self.motors[0].state: sleep(0.01)

		else:
			for m in self.motors:
				m.duty_cycle_sp = dc
				m.run_direct()
				dc = -dc

	def turn_right(self, angle=None, dc=60):
		if angle != None: angle = -angle
		self.turn_left(angle, -dc)

	def stop(self):
		for m in self.motors:
			m.stop()
