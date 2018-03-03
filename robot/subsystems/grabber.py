import ctre
import wpilib
from networktables import NetworkTables
from wpilib.command.subsystem import Subsystem
from ctre.wpi_talonsrx import WPI_TalonSRX as Talon

import robotmap

class Grabber(Subsystem):
    """
    This subsystem will control the grabbing mechanism; it will use two Spikes,
    one for each side of the grabber and associated rollers. 
    """
    GRABBER_IN, GRABBER_OUT, GRABBER_IDLE = range(3)
    DEFAULT_SPEED = 0.6 # 60% power

    def __init__(self):
        super().__init__("Grabber")

        self.left_motor = Talon(robotmap.intake.left_motor)
        self.right_motor = Talon(robotmap.intake.right_motor)

        self.left_motor.setInverted(False)
        self.left_motor.setInverted(True)

    ## For legacy purposes; if this method is used, will just go at 60% speed
    def set_mode(self, grab_mode):
    	if grab_mode == Grabber.GRABBER_IN:
    		self.left_motor.set(Grabber.DEFAULT_SPEED)
    		self.right_motor.set(Grabber.DEFAULT_SPEED)
    	elif grab_mode == Grabber.GRABBER_OUT:
    		self.left_motor.set(-Grabber.DEFAULT_SPEED)
    		self.right_motor.set(-Grabber.DEFAULT_SPEED)
    	else:
    		self.left_motor.set(0.0)
    		self.right_motor.set(0.0)

    def set_grab_speed(self, grab_speed, inverted=False):
        if not inverted:
            self.left_motor.set(grab_speed)
            self.right_motor.set(grab_speed)
        else:
            self.left_motor.set(-grab_speed)
            self.right_motor.set(-grab_speed)