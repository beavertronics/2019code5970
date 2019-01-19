#!/usr/bin/env python3
# vim: set sw=4 noet ts=4 fileencoding=utf-8:

# Robotics specifc libraries
import wpilib
from wpilib.buttons.joystickbutton import JoystickButton
import time
from networktables import NetworkTables

# Non robot specific libraries
import os
import sys
import math

#Linux path
sys.path.append('./robot_py_modules') 
sys.path.append('./robot_logic') 

#Windows RobotPyModules path
sys.path.append('C:/Users/Beavertronics/Desktop/2019code5970/drivingcode/\
robot_py_modules') 
sys.path.append('C:/Users/Beavertronics/Desktop/2019code5970/drivingcode/\
robot_logic') 

# Subsidiary objects on the robot. Ex: Cube Intake from 2017/18 season
from pneumatics import Pneuma              
from encoders import Encoders
from left_motors import Left_Motors
from right_motors import Right_Motors
import set_drive
import joysticks

class BeaverTronicsRobot(wpilib.IterativeRobot): 

    def robotInit(self):

        # TeleOP instances of classes
        self.pn = Pneuma()
        self.encoders = Encoders()
        self.left_motors = Left_Motors.left_motor_group
        self.right_motors = Right_Motors.right_motor_group
        
        # Autonomous modules

		# Tank Drive mode
		self.lj = joysticks.lj
		self.rj = joysticks.rj
		self.drive = drive.set_tank_drive(self.left_motors, self.right_motors)

		# Joystick buttons, when pressed do some function in other files
		cargo_eject_butt = joysticks.set_button(self.lj, xxx)
		ramp_deploy_butt = joysticks.set_button(self.lj, xxx)
		ramp_up_butt = joysticks.set_button(self.lj, xxx)

		hp_eject_butt = joysticks.set_button(self.rj, xxx)
		lineup_butt = joysticks.set_button(self.rj, xxx)
		highgear_butt = joysticks.set_button(self.rj, xxx)
		
		
		
            
    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
	# Set up encoders

	# Loop counter to stop/start auto?

	# Reset encoders (zero them) upon init
		
	# Get Driverstation data from field
        data = wpilib.DriverStation.getInstance().getGameSpecificMessage()
		self.error = 0
		self.total_error = 0
        
    def autonomousPeriodic(self):
   
	# Begin auto loop counter for controlling auto? Loop if less than x val
        if self.auto_loop_counter < 300:
            self.setDriveMotors(-.25, .25)
			
	    # Get inputs for PID
            
	    # PID loop for target velocity on each side of drivetrain in auto
	    # Input: target pathway (Noah code)
	    pid = Pid_Loop()	
	    previous_error = self.error 
	    self.error = pid.get_error()
	    self.total_error = pid.set_total_error(self.error, self.total_error)
		proportion = pid.set_proportion()
	    max_error = pid.set_max_error()
	    integral = pid.set_integral()
		derivative = pid.set_derivative(self.error, self.kd, previous_error)
	    ###right_velocity = pid.get_velocity()
                
	    # Outputs for PID
	
            # set motor speed to PID outputs 

            time.sleep(0.2)
          
        else:
	    ### now diff file set_drive_motors()
	    # set drive motors to zero if auto counter is done

        self.auto_loop_counter +=1
		# Why is this necessary?
        data = wpilib.DriverStation.getInstance().getGameSpecificMessage()

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""

		# Set speed of motors based on joysticks
		set_tank_speed(self.lj, self.rj, self.drive)

		# Executing button functions
		joysticks.execute_button(cargo_eject_butt, arm.cargo_eject(), xxx)
		joysticks.execute_button(ramp_deploy_butt, arm.ramp_deploy(), xxx)
		### etc

		#intake/outakes

		#shifters

	# any lineup code used for teleop 
    
    def testPeriodic(self):
        """This function is called periodically during test mode."""
    
if __name__ == "__main__":
    wpilib.run(BeaverTronicsRobot)
