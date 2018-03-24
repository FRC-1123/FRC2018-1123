import ctre
import wpilib

from networktables import NetworkTables
from wpilib.command.subsystem import Subsystem

from wpilib import DigitalInput

import robotmap

class DigitalIn(Subsystem):
    """
    This subsystem will act as the "Piston Master", controlling all the pistons
    on the robot, through a total of 4 Double Solenoids. 
    """

    def __init__(self):
        super().__init__("DigitalIn")

        self.inp1 = DigitalInput(0);
        self.inp2 = DigitalInput(1);
        self.inp3 = DigitalInput(2);

        #subsystems.dumper.double_solenoid.set(subsystems.dumper.double_solenoid.Value.kReverse)
        #subsystems.dumper.double_solenoid.set(subsystems.dumper.double_solenoid.Value.kForward)