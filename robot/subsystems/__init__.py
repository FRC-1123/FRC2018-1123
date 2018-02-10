"""
All subsystems should be imported here and instantiated inside the init method.
If you want your subsystem to be accessible to commands, you must add a variable
for it in the global scope.
"""

from wpilib.robotbase import RobotBase
from .drivetrain import DriveTrain
from .liftmech import LiftMech
#subsystemname = None

drivetrain = None
liftmech = None

def init():
    """
    Creates all subsystems. You must run this before any commands are
    instantiated. Do not run it more than once.
    """
    global motors, drivetrain

    drivetrain = DriveTrain()
    liftmech = LiftMech()

    # initialize the subsystems here
