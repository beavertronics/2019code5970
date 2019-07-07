# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Subsystem

class Beak(Subsystem):
	def __init__(self):
		super().__init__()
		self.solenoid = wpilib.Solenoid(2)
	
	def open_beak(self):
		self.solenoid.set(True)

	def close_beak(self):
		self.solenoid.set(False)
	
