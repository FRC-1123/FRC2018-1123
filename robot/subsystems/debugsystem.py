import ctre
import wpilib
from networktables import NetworkTables
from wpilib.command.subsystem import Subsystem
from ctre.wpi_talonsrx import WPI_TalonSRX as Talon

import robotmap

class DebugSystem(Subsystem):
    """
    This subsystem will control the grabbing mechanism; it will use two Spikes,
    one for each side of the grabber and associated rollers. 
    """

    def __init__(self):
        super().__init__("DebugSystem")

        self.my_motor = Talon(robotmap.debug.port)
        self.my_motor.setInverted(False)