import ctre
import wpilib
from networktables import NetworkTables
from wpilib.command.subsystem import Subsystem
from ctre.wpi_talonsrx import WPI_TalonSRX as Talon

import robotmaphh

class Grabber(Subsystem):
    """
    This subsystem will control the grabbing mechanism
    Details TBD
    """

    def __init_(self):
        super().__init__("Grabber")

        self.left_motor = Talon(robotmap.intake.left_motor)
        self.right_motor = Talon(robotmap.intake.right_motor)

        self.left_motor.setInverted(False)
        self.right_motor.setInverted(True)