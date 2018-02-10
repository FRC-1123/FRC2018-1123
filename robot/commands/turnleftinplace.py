import wpilib
from wpilib.command import Command

import subsystems

class TurnLeftInPlace(Command):
    """
    Drives forward at the given power for a given duration.
    """

    def __init__(self, power, time):
        super().__init__('Turning left in place at %f for %0.2fs' % (power, time))

        self.requires(subsystems.drivetrain)
        self.power = power
        self.time_length = time
        self.timer = wpilib.Timer()

    def initialize(self):
        self.timer.start()

    def execute(self):
        subsystems.drivetrain.drive.tankDrive(-self.power, self.power)
        self.timer.delay(0.05)

    def isFinished(self):
        return self.timer.hasPeriodPassed(self.time_length)

    def end(self):
        subsystems.drivetrain.drive.tankDrive(0.0, 0.0)
