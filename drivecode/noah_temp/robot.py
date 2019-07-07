# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Scheduler
		
from beak import Beak
from fourbar import Fourbar
from drivetrain import Drivetrain

from left_motors import Left Motors
from right_motors import Right_Motors

from Do_2_Hatch_Panel_Auto_Left import do_2_hatch_panel_auto_left

class BeaverTronicsRobot(wpilib.TimedRobot):
	def robotInit(self):
		self.drivetrain = Drivetrain(self)
		self.fourbar = Fourbar(self)
		self.beak = Beak(self)
	def autonomousInit(self):
		Sheduler.getInstance().removeAll()
		data = wpilib.DriverStation.getInstane().getGameSpecificMessage()
		self.do_2_hatch_panel_auto_left.start()
	def disabledInit(self):
		self.drivetrain.stop()

if __name__ == "__main__":
	wpilib.run(BeaverTronicsRobot)
	
