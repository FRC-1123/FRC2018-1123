from networktables import NetworkTables
from wpilib import Timer
from wpilib.command import Command

import logging

import robotmap
import subsystems
from inputs import oi


class FollowJoystick(Command):
    """
    This command will read the joysticks' y-axes and uses tank drive.
    """

    def __init__(self):
        super().__init__('Follow Joystick')

        self.requires(subsystems.drivetrain)

        self.drivetrain = subsystems.drivetrain
        #self.drive = subsystems.drivetrain.drive

        self.sd = NetworkTables.getTable("SmartDashboard")
		
        self.logger = logging.getLogger("robot")

        self.timer = Timer()
        self.timer.start()
		
        self.tolerance = 0.15

    def execute(self):
        if self.timer.hasPeriodPassed(0.05):

            left_power = oi.joystick.getRawAxis(robotmap.joystick.left_y_axis) * 1.0
            right_power = oi.joystick.getRawAxis(robotmap.joystick.right_y_axis) * 1.0
			
            ## If we're within the tolerance, we assume driver means to straight, and
            ## correct to whichever has the largest magnitudes
            if abs(left_power - right_power) < self.tolerance:
                if abs(left_power) > abs(right_power):
                    right_power = left_power
                elif abs(right_power) > abs(left_power):
                    left_power = right_power

            self.sd.putNumber("controller/leftPower", left_power)
            self.sd.putNumber("controller/rightPower", right_power)
            
            if robotmap.joystick.inverted:
                left_power *= -1.0
                right_power *= -1.0
            
            self.drivetrain.tank_drive(left_power, right_power)
            #self.drive.tankDrive(left_power, right_power)

    def end(self):
        self.drivetrain.tank_drive(0.0, 0.0)
        #self.drive.tankDrive(0.0, 0.0)
        #subsystems.drivetrain.robot_drive.setLeftRightMotorOutputs(0, 0)
