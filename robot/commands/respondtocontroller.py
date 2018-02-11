from networktables import NetworkTables
from wpilib import GenericHID
from wpilib.command import Command
from wpilib.timer import Timer

from inputs import oi
import robotmap

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

    def initialize(self):
        self.timer.start()

    def execute(self):
        if self.timer.hasPeriodPassed(0.05):
            is_pressed = {}
            is_pressed[robotmap.Buttons.A] = oi.getAButton()
            is_pressed[robotmap.Buttons.B] = oi.getBButton()
            is_pressed[robotmap.Buttons.X] = oi.getXButton()
            is_pressed[robotmap.Buttons.Y] = oi.getYButton()

            if is_pressed[robotmap.controller_bindings.lift_raise]:
                # raise the lift
                pass
            elif is_pressed[robotmap.controller_bindings.lift_lower]:
                # lower the lift
                pass

            if is_pressed[robotmap.controller_bindings.intake_in]:
                # make the intake come in
                pass
            elif is_pressed[robotmap.controller_bindings.intake_out]:
                # make the intake go out
                pass