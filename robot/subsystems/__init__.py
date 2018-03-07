"""
All subsystems should be imported here and instantiated inside the init method.
If you want your subsystem to be accessible to commands, you must add a variable
for it in the global scope.
"""

from wpilib.robotbase import RobotBase
from .drivetrain import DriveTrain
from .liftmech import LiftMech
from .grabber import Grabber
from .climbmech import ClimbMech
from .debugsystem import DebugSystem

drivetrain = None
liftmech = None
grabber = None
climbmech = None
debugsystem = None

def init():
    """
    Creates all subsystems. You must run this before any commands are
    instantiated. Do not run it more than once.
    """
    global drivetrain, liftmech, grabber, climbmech, debugsystem

    drivetrain = DriveTrain()
    liftmech = LiftMech()
    grabber = Grabber()
    climbmech = ClimbMech()
    debugsystem = DebugSystem()

    # initialize the subsystems here
