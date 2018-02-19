import wpilib
from networktables import NetworkTables
from wpilib.command import Command

from inputs import navx

import logging
import subsystems

class UpdateNetworkTables(Command):

    def __init__(self):
        super().__init__("Update NetworkTables")

        self.sd = NetworkTables.getTable("SmartDashboard")
        self.nt_timer = wpilib.Timer()  # timer for updating NetworkTables
		
        self.logger = logging.getLogger("robot")

    def initialize(self):
        self.nt_timer.start()
        self.logger.info("Update Network Tables is starting!")

    def execute(self):
        if self.nt_timer.hasPeriodPassed(0.1):  # update NetworkTables every 0.1 seconds
            # dashboard forward button (for testing purposes)
            if self.sd.containsKey("forwardCommand") and self.sd.getBoolean("forwardCommand"):  # check if move forward button pressed
                self.sd.putBoolean("forwardCommand", False) # set button back 
                DriveForward(0.5, 2).start()
                #self.logger.info("Moving forward at half power for one second.")

            # update navx status
            self.sd.putBoolean('navX/isConnected', navx.ahrs.isConnected())
            self.sd.putBoolean('navX/isCalibrating', navx.ahrs.isCalibrating())
            self.sd.putNumber('navX/yaw', navx.ahrs.getFusedHeading())
            self.logger.info("NavX Yaw should be " + str(navx.ahrs.getFusedHeading()))