import ctre
import wpilib
from networktables import NetworkTables
from wpilib.command.subsystem import Subsystem
from ctre.wpi_talonsrx import WPI_TalonSRX as Talon
from wpilib.drive import DifferentialDrive

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
    #def tank_drive(self):
