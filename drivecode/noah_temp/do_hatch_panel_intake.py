# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Command

import time

class Do_Hatch_Panel_Intake(Command):
	def __init__(self, robot):
		super().__init__()

		self.beak = robot.beak
		self.fourbar = robot.fourbar

	def initialize(self):
		self.beak.close()
		self.fourbar.extend()
		time.sleep(1)
		self.beak.close()
		self.fourbar.retract()

	def execute(self):
		return None
	
	def isFinished(self):
		return True

	def end(self):
		return None

