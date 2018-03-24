import wpilib
from wpilib.command import InstantCommand

from inputs import navx

import logging
import subsystems

class DumpBlock(InstantCommand):
    """
    Drives forward at the given power for a given duration.
    """

    def __init__(self, power):
        super().__init__('Dump Block')
        self.requires(subsystems.pistons)
        self.timer = wpilib.Timer()
        self.logger = logging.getLogger("robot")
        
    def initialize(self):
        self.logger.info("Pushing block out!")
        subsystems.pistons.piston2.set(DoubleSolenoid.Value.kForward)
        subsystems.pistons.piston3.set(DoubleSolenoid.Value.kForward)
        self.timer.delay(0.2)
        self.logger.info("Retracting pistons!")
        subsystems.pistons.piston2.set(DoubleSolenoid.Value.kReverse)
        subsystems.pistons.piston3.set(DoubleSolenoid.Value.kReverse)
