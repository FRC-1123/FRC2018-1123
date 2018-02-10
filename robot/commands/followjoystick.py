from networktables import NetworkTables
from wpilib import Timer
from wpilib.command import Command

import robotmap
import subsystems
#from inputs import oi


class FollowJoystick(Command):
    """
    This command will read the joysticks' y-axes and uses tank drive.
    """

    def __init__(self):
        super().__init__('Follow Joystick')

        self.requires(subsystems.motors)

        self.drive = subsystems.motors.drive

        self.sd = NetworkTables.getTable("SmartDashboard")

        self.timer = Timer()
        self.timer.start()

    def execute(self):
        if self.timer.hasPeriodPassed(0.05):  # period of 0.05 seconds
            # tank drive
            # subsystems.motors.robot_drive.tankDrive(oi.joystick, robotmap.joystick.left_port, oi.joystick,
            #                                         robotmap.joystick.right_port, True)

            # arcade drive
            # subsystems.motors.robot_drive.arcadeDrive(oi.joystick)
 
            # rectified arcade drive

            left_power = oi.joystick.getRawAxis(robotmap.joystick.left_y_axis) * 0.75
            right_power = oi.joystick.getRawAxis(robotmap.joystick.right_y_axis) * 0.75

            ## TODO: make this display live in the dashboard

            self.drive.tankDrive(left_power, right_power)

    def end(self):
        self.drive.tankDrive(0.0, 0.0)
        #subsystems.motors.robot_drive.setLeftRightMotorOutputs(0, 0)
