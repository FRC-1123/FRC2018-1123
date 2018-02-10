import ctre
import wpilib
from networktables import NetworkTables
from wpilib.command.subsystem import Subsystem
from ctre.wpi_talonsrx import WPI_TalonSRX as Talon

import robotmap


class LiftMech(Subsystem):
    """
    This subsystem will control the lift mechanism
    It will use two motors, which will be at ~half power, and in 
    opposite directions.
    """

    def __init_(self):
        super().__init__("LiftMech")

        self.motor_a = Talon(robotmap.lift_mech.motor_a)
        self.motor_a.setInverted(False)

        self.motor_b = Talon(robotmap.lift_mech.motor_b)
        self.motor_b.setInverted(True)

    def set(self, power):
    	self.motor_a.set(power)
    	self.motor_b.set(power)