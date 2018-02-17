import ctre
import wpilib
from networktables import NetworkTables
from wpilib.command.subsystem import Subsystem
from wpilib import Relay
#from ctre.wpi_talonsrx import WPI_TalonSRX as Talon

import robotmap

class Grabber(Subsystem):
    """
    This subsystem will control the grabbing mechanism; it will use two Spikes,
    one for each side of the grabber and associated rollers. 
    """
    GRABBER_IN, GRABBER_OUT, GRABBER_IDLE = range(3)

    def __init_(self):
        super().__init__("Grabber")

        self.left_motor = Relay(robotmap.intake.left_motor, Relay.Direction.kBoth) #Talon(robotmap.intake.left_motor)
        self.right_motor = Relay(robotmap.intake.right_motor, Relay.Direction.kBoth) #Talon(robotmap.intake.right_motor)

    def set_mode(self, grab_mode):
    	if grab_mode == Grabber.GRABBER_IN:
    		self.left_motor.set(Relay.Value.kForward)
    		self.right_motor.set(Relay.Value.kReverse)
    	elif grab_mode == Grabber.GRABBER_OUT:
    		self.left_motor.set(Relay.Value.kReverse)
    		self.right_motor.set(Relay.Value.kForward)
    	else:
    		self.left_motor.set(Relay.Value.kOff)
    		self.right_motor.set(Relay.Value.kOff)

        #self.left_motor.setInverted(False)
        #self.right_motor.setInverted(True)