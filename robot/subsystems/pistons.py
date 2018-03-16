import ctre
import wpilib
from networktables import NetworkTables
from wpilib.command.subsystem import Subsystem
from ctre.wpi_talonsrx import WPI_TalonSRX as Talon
from wpilib.drive import DifferentialDrive
from wpilib import DoubleSolenoid

import robotmap

class Pistons(Subsystem):
    """
    This subsystem will act as the "Piston Master", controlling all the pistons
    on the robot, through a total of 4 Double Solenoids. 
    """

    def __init__(self):
        super().__init__("Pistons")

        self.piston1 = DoubleSolenoid(robotmap.pistons.piston1_forward, robotmap.pistons.piston1_reverse)
        self.piston2 = DoubleSolenoid(robotmap.pistons.piston2_forward, robotmap.pistons.piston2_reverse)
        self.piston3 = DoubleSolenoid(robotmap.pistons.piston3_forward, robotmap.pistons.piston3_reverse)
        self.piston4 = DoubleSolenoid(robotmap.pistons.piston4_forward, robotmap.pistons.piston4_reverse)

        #subsystems.dumper.double_solenoid.set(subsystems.dumper.double_solenoid.Value.kReverse)
        #subsystems.dumper.double_solenoid.set(subsystems.dumper.double_solenoid.Value.kForward)