# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Command
from wpilib.command.WaitCommand import WaitCommand

class Do_Hatch_Panel_Intake(Command):
	def __init__(self, robot):
		super().__init__()

		self.beak = robot.beak
		self.fourbar = robot.fourbar

	def initialize(self):
		self.beak.close()
		self.fourbar.extend()
		WaitCommand(1)
		self.beak.close()
		self.fourbar.retract()

	def execute(self):
		return None
	
	def isFinished(self):
		return True

	def end(self):
		return None

