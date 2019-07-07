# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Command

from pure_pursuit import Pure_Pursuit

class Do_Wall_To_Cargo_Ship(Command):
	def __init__(self, robot):
		super().__init__()

		self.drivetrain = robot.drivetrain

	def initialize(self):
		lookahead_distance = 18
		acceleration = 75
		trajectory = json.loads(open("wall_to_cargo_ship","r").read()))
		pure_pursuit = Pure_Pursuit(trajectory,lookahead_distance,acceleration)

	def execute(self):
		self.drivetrain.update_position()
		x = self.drivetrain.x
		y = self.drivetrain.y
		heading = self.drivetrain.heading
		left_speed, right_speed = pure_pursuit.controller(x,y,heading)

	def isFinished(self):
		if pure_pursuit.isFinished == True:
			return True
		else:
			return False

	def end(self):
		self.drivetrain.stop(self)
		return None

	def interrupted(self):
		return None
