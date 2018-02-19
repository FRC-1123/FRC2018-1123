import wpilib
from wpilib.command import TimedCommand

import subsystems

class SetSpeeds(TimedCommand):
    """
    Drives forward at the given power for a given duration.
    """

    def __init__(self, left_power, right_power, timeout, squared=True):
        super().__init__('Left: %f, Right: %f, for %0.2fs' % (left_power, right_power, timeout), timeout)

        self.requires(subsystems.drivetrain)

        self.drivetrain = subsystems.drivetrain

        self.left_power = left_power
        self.right_power = right_power
        self.squared = squared

        self.timer = wpilib.Timer()

    def initialize(self):
        self.timer.start()

    def execute(self):
        self.drivetrain.tank_drive(self.left_power, self.right_power, self.squared)
        self.timer.delay(0.05)

    def end(self):
        self.drivetrain.tank_drive(0.0, 0.0)