import wpilib
from wpilib.buttons.joystickbutton import JoystickButton
import sys
sys.path.append('C:/Users/Beavertronics/Desktop/2018Workstation/2018code5970/drivingcode/robot_py_modules')

from variable_declarations import VariableDec    #Assign variables for encoders, motors, pistons etc. to use in robot.py and RobotPyModules 

class AutoMovement(VariableDec):
    '''
    Functions for autonomous movement of drivetrain (moving, turning, etc.)
    ''' 
    def drive_forward(self,distance,direction):
        self.Lcoder.reset()
        if direction =="Forward":
            while self.Lcoder.get() < distance:
                self.setDriveMotors(.5, -.5)
            self.setDriveMotors(0, 0)
        elif direction =="Backward":
            while self.Lcoder.get() > distance:
                self.setDriveMotors(-.5, .5)
            self.setDriveMotors(0, 0)
    
    def turn(self,degrees):
        self.Gyroo.reset()
        if degrees >= 0:#if it's turning left
            while self.Gyroo.getAngle()() <= degrees:
                self.setDriveMotors(-.25, -.25)#assuming it's turning left here
            self.setDriveMotors(0, 0)
            return 0
        if degrees <= 0:#if it's turning right
            while self.Gyroo.getAngle()() >= degrees:#expecting a negative value for this side
                self.setDriveMotors(.25,.25)#assuming it's turning right here
            self.setDriveMotors(0, 0) 
            
    
        