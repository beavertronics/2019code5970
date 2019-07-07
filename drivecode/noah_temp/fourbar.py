# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Subsystem

class Fourbar(Subsystem):
	def __init__(self):
		super().__init__()
		self.solenoid = wpilib.solenoid(3)

	def extend(self):
		self.solenoid.set(True)

	def retract(self):
		self.solenoid.set(False)


