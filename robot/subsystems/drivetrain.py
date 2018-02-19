import ctre
import wpilib
from networktables import NetworkTables
from wpilib.command.subsystem import Subsystem
from ctre.wpi_talonsrx import WPI_TalonSRX as Talon
from wpilib.drive import DifferentialDrive

import math
import robotmap

class DriveTrain(Subsystem):
    """
    This subsystem will control the drive train.
    The robot uses a tank drive setup, with 4 Independent CIMs, although the two right motors and two left motors
    will always be moving together.
    """

    def __init__(self):
        super().__init__("DriveTrain")

        self.left_front_motor = Talon(robotmap.drivetrain.left_front_id)
        self.left_back_motor = Talon(robotmap.drivetrain.left_back_id)
        self.right_front_motor = Talon(robotmap.drivetrain.right_front_id)
        self.right_back_motor = Talon(robotmap.drivetrain.right_back_id)

        self.left_front_motor.setInverted(True)
        self.left_back_motor.setInverted(True)
        self.right_front_motor.setInverted(True)
        self.right_back_motor.setInverted(True)

        #self.left_controller_group = wpilib.SpeedControllerGroup(self.left_front_motor, self.left_back_motor)
        #self.right_controller_group = wpilib.SpeedControllerGroup(self.right_front_motor, self.right_back_motor)

        self.drive = DifferentialDrive(self.left_controller_group, self.right_controller_group)

    ## This is, to some degree, recreating the method from DifferentialDrive; except that we want to be able
    ## to apply the manual multipliers from robotmap, which "fix" the front and back motors on a given side
    ## not going at the same speed.
    def tank_drive(self, left_speed, right_speed, squared=True):
        left_speed = apply_deadband(limit(left_speed))
        right_speed = apply_deadband(limit(right_speed))

        if squared:
            left_speed = math.copysign(left_speed ** 2, left_speed)
            right_speed = math.copysign(right_speed ** 2, right_speed)

        self.left_front_motor.set(left_speed * robotmap.drivetrain.left_front_multiplier)
        self.left_back_motor.set(left_speed * robotmap.drivetrain.left_back_multiplier)

        self.right_front_motor.set(right_speed * robotmap.drivetrain.right_front_multiplier)
        self.right_back_motor.set(right_speed * robotmap.drivetrain.right_back_multiplier)


    ## Basically straight from RobotDriveBase, just for recreating locally with custom multipliers
    def apply_deadband(value, deadband=0.05):
        if abs(value) > deadband:
            if value < 0.0:
                return (value - deadband) / (1.0 - deadband)
            else:
                return (value + deadband) / (1.0 - deadband)
        else:
            return 0.0

    def limit(value):
        if value > 1.0:
            return 1.0
        elif value < -1.0:
            return -1.0
        return value