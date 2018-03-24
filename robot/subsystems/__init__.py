"""
All subsystems should be imported here and instantiated inside the init method.
If you want your subsystem to be accessible to commands, you must add a variable
for it in the global scope.
"""

from wpilib.robotbase import RobotBase
import robotmap
from .drivetrain import DriveTrain
#from .liftmech import LiftMech
#from .grabber import Grabber
from .climbmech import ClimbMech
from .debugsystem import DebugSystem
from .pistons import Pistons
from .digitalin import DigitalIn

drivetrain = None
#liftmech = None
#grabber = None
climbmech = None
debugsystem = None
pistons = None
digitalin = None

def init():
    """
    Creates all subsystems. You must run this before any commands are
    instantiated. Do not run it more than once.
    """
    global drivetrain, liftmech, grabber, climbmech, debugsystem, pistons, digitalin

    drivetrain = DriveTrain()
    liftmech = LiftMech()
    grabber = Grabber()
    climbmech = ClimbMech()
    pistons = Pistons()
    digitalin = DigitalIn()
    if robotmap.debug.is_set:
        debugsystem = DebugSystem()

    # initialize the subsystems here
