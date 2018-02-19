import wpilib
from wpilib.command import TimedCommand

import subsystems

class SetForwardSpeed(TimedCommand):
    """
    Drives forward at the given power for a given duration.
    """

    def __init__(self, power, timeout, squared=True):
        super().__init__('Going forward at %f for %0.2fs' % (power, timeout), timeout)

        self.requires(subsystems.drivetrain)

        self.drivetrain = subsystems.drivetrain
        
        self.power = power
        self.squared = squared

        self.timer = wpilib.Timer()

    def initialize(self):
        self.timer.start()

    def execute(self):
        self.drivetrain.tank_drive(self.power, self.power, self.squared)
        self.timer.delay(0.05)

    def end(self):
        self.drivetrain.tank_drive(0.0, 0.0)