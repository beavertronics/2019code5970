# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Scheduler
		
from beak import Beak
from fourbar import Fourbar
from drivetrain import Drivetrain

from left_motors import Left_Motors
from right_motors import Right_Motors

from do_2_hatch_panel_auto_left import Do_2_Hatch_Panel_Auto_Left

import os
import sys
import math

sys.path.append('./subsystems')
sys.path.append('./commands')

sys.path.insert(0, '/home/lvuser/py/subsystems')
sys.path.insert(0, '/home/lvuser/py/commands')

class BeaverTronicsRobot(wpilib.TimedRobot):
	def robotInit(self):
		self.drivetrain = Drivetrain(18,self)
		self.fourbar = Fourbar(self)
		self.beak = Beak(self)
		self.left_joy = wpilib.Joystick(0)
		self.right_joy = wpilib.Joystick(1)
		self.xbox = wpilib.Joystick(2)
		self.timer = wpilib.Timer()
		self.loops = 0
		wpilib.CameraServer.launch("wision.py:main")
	def autonomousInit(self):
		Sheduler.getInstance().removeAll()
		data = wpilib.DriverStation.getInstane().getGameSpecificMessage()
		self.do_2_hatch_panel_auto_left.start()
	def autonomousPeriodic(self):
		Scheduler.getInstance().run()
	def teleopInit(self):
		self.loops = 0
		self.timer.reset()
		self.timer.start()

		Scheduler.getInstance().removeAll()
		Scheduler.getInstance().enable()
	def teleopPeriodic(self):
		Scheduler.getInstance().run()
		speed = self.right_joy.getY()
		rotation = self.left_joy.getX()
		self.drivetrain.drive.arcadeDrive(speed,rotation,True)
		self.loops += 1
		if self.timer.hasPeriodPassed(1):
			self.logger.info("%d loops / second", self.loops)
			self.loops = 0
	def disabledInit(self):
		self.drivetrain.stop()
		Scheduler.getInstance().removeAll()

		return None
	def disabledPeriodic(self):
		return None

if __name__ == "__main__":
	wpilib.run(BeaverTronicsRobot)
	
