from networktables import NetworkTables
from wpilib.command import Command
from wpilib.timer import Timer

from inputs import oi
import logging
import robotmap
import subsystems
from subsystems.grabber import Grabber
from wpilib.interfaces import GenericHID

class RespondToController(Command):
    """
    This command will respond to the controller's buttons.
    """

    def __init__(self):
        super().__init__("Respond to Controller")

        self.requires(subsystems.grabber)
        self.requires(subsystems.debugsystem)
        #self.requires(subsystems.liftmech)

        #self.sd = NetworkTables.getTable("SmartDashboard")
        self.logger = logging.getLogger("robot")

        #oi.start_btn.whenPressed(SwitchCamera())

        self.timer = Timer()
 
    def initialize(self):
        self.timer.start()

    def execute(self):
        if self.timer.hasPeriodPassed(0.05):
            is_pressed = {}
            is_pressed[robotmap.Buttons.A] = oi.controller.getAButton()
            is_pressed[robotmap.Buttons.B] = oi.controller.getBButton()
            is_pressed[robotmap.Buttons.X] = oi.controller.getXButton()
            is_pressed[robotmap.Buttons.Y] = oi.controller.getYButton()

            if robotmap.debug.is_set:
                if oi.controller.getBumper(GenericHID.Hand.kLeft) and robotmap.debug.is_set:
                    self.logger.info("Running debug system...")
                    subsystems.debugsystem.my_motor.set(robotmap.debug.power)
                else:
                    subsystems.debugsystem.my_motor.set(0.0)

            ## LIFTER LOGIC

            if is_pressed[robotmap.controller_bindings.lift_raise]:
                # raise the lift
                subsystems.liftmech.set_lift_speed(robotmap.lift_mech.power)
                pass
            elif is_pressed[robotmap.controller_bindings.lift_lower]:
                # lower the lift
                subsystems.liftmech.set_lift_speed(-robotmap.lift_mech.power)
                pass
            else:
                # turn off lift
                subsystems.liftmech.set_lift_speed(0.0)

            ## GRABBER LOGIC

            if is_pressed[robotmap.controller_bindings.intake_in]:
                # make the intake come 
                self.logger.info("Currently Grabbing IN")
                subsystems.grabber.set_mode(Grabber.GRABBER_IN)

            elif is_pressed[robotmap.controller_bindings.intake_out]:
                # make the intake go out
                self.logger.info("Currently Grabbing OUT")
                subsystems.grabber.set_mode(Grabber.GRABBER_OUT)

            else:
                # turn off intake
                subsystems.grabber.set_mode(Grabber.GRABBER_IDLE)