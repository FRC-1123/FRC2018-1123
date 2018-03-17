import wpilib
from wpilib.command import Command

import subsystems

class SleepCommand(Command):
    """
    Drives forward at the given power for a given duration.
    """

    def __init__(self, time):
        super().__init__('Driving forward at %f for %0.2fs' % (power, time))

        self.time_length = time
        self.timer = wpilib.Timer()

    def execute(self):
        pass

    def isFinished(self):
        return self.timer.hasPeriodPassed(self.time_length)
