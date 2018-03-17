import wpilib
from wpilib.command import Command

from inputs import navx

import logging
import subsystems

class TurnRight90(Command):
    """
    Drives forward at the given power for a given duration.
    """

    def __init__(self, power):
        super().__init__('Turning right 90 in place at %f' % power)

        self.requires(subsystems.drivetrain)
        self.drivetrain = subsystems.drivetrain
        self.power = power
        
        self.timer = wpilib.Timer()
        self.starting_angle = 0.0
        
        self.logger = logging.getLogger("robot")

    # in range -180 to 180
    def angle_diff(self, cur, prev):
        df = cur - prev
        while df < -180.0:
            df += 360.0
        while df > 180.0:
            df -= 360.0
        return df
        
    def initialize(self):
        self.timer.start()
        self.starting_angle = navx.ahrs.getFusedHeading()

    def execute(self):
        self.drivetrain.tank_drive(-self.power, self.power, False)
        self.timer.delay(0.05)
        self.logger.info("current is " + str(self.angle_diff(navx.ahrs.getFusedHeading(), self.starting_angle)))

    def isFinished(self):
        return self.angle_diff(navx.ahrs.getFusedHeading(), self.starting_angle) > 90.0 or self.timer.hasPeriodPassed(5.0)
        ## After 5 seconds, we just give up

    def end(self):
        self.drivetrain.tank_drive(0.0, 0.0)
        # subsystems.drivetrain.drive.tankDrive(0.0, 0.0)
