# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command.subsystem import Subsystem
from wpilib.drive import DifferentialDrive

from left_motors import Left_Motors
from right_motors import Right_Motors

import math

class Drivetrain(Subsystem):
	def __init__(self, distance_per_pulse, robot):
		super().__init__()

		left_motors_instance = Left_Motors()
		right_motors_instance = Right_Motors()
		self.left_motors = left_motors_instance.left_motor_group
		self.right_motors = right_motors_instance.right_motor_group

		self.left_encoder = wpilib.Encoder(2,3)
		self.right_encoder = wpilib.Encoder(4,5)
		self.left_encoder.setDistancePerPulse(distance_per_pulse)
		self.right_encoder.setDistancePerPulse(distance_per_pulse)

		self.gyro = wpilib.ADXRS450_Gyro()

		self.robot_instance = robot

		self.drive = DifferentialDrive(self.left_motors,
									self.right_motors)
		self.gyro.reset()

		self.x = 0
		self.y = 0
		self.heading = math.pi/2

		self.last_left_encoder_distance = 0
		self.last_right_encoder_distance = 0

	def set_tank_speed(self, left_speed, right_speed):
		self.left_motors.set(left_speed)
		self.right_motors.set(right_speed)

	def stop(self):
		self.left_motors.set(0)
		self.right_motors.set(0)
	
	def reset_encoders(self):
		self.right_encoder.reset()
		self.left_encoder.reset()

	def find_displacement(self):
		left_distance = self.left_encoder.getDistance()
		right_distance = self.right_encoder.getDistance()
		left_displacement = left_distance - self.last_left_distance
		right_displacement = right_distance - self.last_right_distance
		return left_displacement, right_displacement

	def update_position(self):
		left_displacement, right_displacement = self.find_displacement()
		center_displacement = (left_displacement + right_displacement)/2
		self.heading = math.radians(self.gyro.getAngle()) + math.pi/2
		self.x += math.cos(heading) * center_displacement
		self.y += math.sin(heading) * center_displacement
