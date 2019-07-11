import wpilib
import math

class Noah_Drive():
	def __init__(self,deadband_speed,deadband_curve,left_joy,right_joy):
		self.deadband_speed = deadband_speed
		
		self.deadband_curve = deadband_curve

		self.left_joy = left_joy

		self.right_joy = right_joy

		self.trackwidth = 24

		self.max_speed = 180

		self.max_radius = 100

	def deadband_radius(self):
		input_radius = self.left_joy.getX()

		if abs(self.input_radius) <= self.deadband_radius:
			radius = self.deadband_radius	

		return radius, input_radius

	def deadband_speed(self):
		input_speed = self.right_joy.getY()
		isQuickTurn = False
		if abs(input_speed) <= self.deadband_speed:
			speed = 0
			isQuickTurn = True
		else:
			speed = input_speed
		return speed, isQuickTurn

	def square_speed(self, speed):
		sign = lambda speed: (speed>0) - (speed<0) 
		speed = math.pow(speed,2.0)
		speed = speed * self.max_speed * sign
		return speed
	
	def convert_radius(self, input):
		sign = lambda input: (input>0) - (input<0) 
		slope = (self.trackwidth-self.max_radius)/(1-self.self.deadband_radius)
		radius = self.trackwidth - (abs(input) - 1) * slope * sign
		return radius

	def convert_data(self):
		radius, input_radius = self.deadband_radius()
		speed, isQuickTurn = self.deadband_speed()	
		speed = self.square_speed(speed)
		radius = self.convert_radius(radius)
		return radius, speed, input_radius, isQuickTurn
	
	def curved_path(self, speed, radius):
		alpha = speed/radius
		if alpha < 0:
			right_speed = speed
			left_speed = alpha * (radius - self.trackwidth)
		else:
			left_speed = speed
			right_speed = alpha * (radius - self.trackwidth)
		return left_speed, right_speed

	def controller(self, radius, speed):
		if radius == 0:
			left_speed = speed
			right_speed = speed
		else:
			left_speed, right_speed = self.curved_path(speed, radius)
		return left_speed, right_speed
		
	def QuickTurn(self, input):
		speed = self.square_speed(input)
		left_speed = speed 
		right_speed = speed * -1
		return left_speed, right_speed

	def output(self):
		radius, speed, input_radius, isQuickTurn = self.convert_data()
		if isQuickTurn == True:
			left_speed, right_speed = self.QuickTurn(input_radius)
		else:
			left_speed, right_speed = self.controller(radius, speed)
		return left_speed, right_speed
				


