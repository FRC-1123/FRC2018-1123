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

        self.drive = subsystems.drivetrain.drive

        self.sd = NetworkTables.getTable("SmartDashboard")
		
        self.logger = logging.getLogger("robot")

        self.timer = Timer()
        self.timer.start()

    def execute(self):
        if self.timer.hasPeriodPassed(0.05):

            left_power = oi.joystick.getRawAxis(robotmap.joystick.left_y_axis) * 1.0
            right_power = oi.joystick.getRawAxis(robotmap.joystick.right_y_axis) * 1.0
			
            #self.logger.info("Joystick should be followed.")
            ## TODO: make this display live in the dashboard

            self.drive.tankDrive(left_power, right_power)

    def end(self):
        self.drive.tankDrive(0.0, 0.0)
        #subsystems.drivetrain.robot_drive.setLeftRightMotorOutputs(0, 0)
