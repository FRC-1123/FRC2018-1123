from networktables import NetworkTables
from wpilib import GenericHID
from wpilib.command import Command
from wpilib.timer import Timer

class RespondToController(Command):
    """
    This command will respond to the controller's buttons.
    """

    def __init__(self):
        super().__init__("Respond to Controller")

        #self.sd = NetworkTables.getTable("SmartDashboard")
        #self.logger = logging.getLogger("robot")

        #oi.start_btn.whenPressed(SwitchCamera())

        self.timer = Timer()

        self.right_bumper_last = False
        self.left_bumper_last = False

    def initialize(self):
        self.timer.start()

    def execute(self):
        if self.timer.hasPeriodPassed(0.05):
            pass
