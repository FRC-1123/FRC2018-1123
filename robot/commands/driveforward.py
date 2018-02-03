import wpilib
from wpilib.command import Command

import subsystems

class DriveForward(Command):
    """
    Drives forward at the given power for a given duration.
    """

    def __init__(self, power, time):
        super().__init__('Driving forward at %f for %0.2fs' % (power, time))

        self.requires(subsystems.motors)
        self.power = power
        self.time_length = time
        self.timer = wpilib.Timer()

    def initialize(self):
        self.timer.start()

    def execute(self):
        subsystems.motors.drive.tankDrive(self.power, self.power)
        self.timer.delay(0.05)

    def isFinished(self):
        return self.timer.hasPeriodPassed(self.time_length)

    def end(self):
        subsystems.motors.drive.tankDrive(0.0, 0.0)
