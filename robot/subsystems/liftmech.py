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

    def __init__(self):
        super().__init__("LiftMech")

        self.motor = Talon(robotmap.lift_mech.motor)
        #self.motor_b = Talon(robotmap.lift_mech.motor_b)
        
        self.motor.setInverted(False)
        #self.motor_b.setInverted(False)


    def set_lift_speed(self, lift_speed):
        self.motor.set(lift_speed)
        #self.motor_b.set(grab_speed)