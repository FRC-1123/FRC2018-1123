from networktables import NetworkTables
from wpilib.command import Command
from wpilib.timer import Timer

from inputs import oi
import logging
import robotmap
from robotmap import Buttons
import subsystems
from subsystems.grabber import Grabber
from wpilib.interfaces import GenericHID
from wpilib import DoubleSolenoid

class RespondToController(Command):
    """
    This command will respond to the controller's buttons.
    """

    def __init__(self):
        super().__init__("Respond to Controller")

        #self.requires(subsystems.grabber)
        #self.requires(subsystems.liftmech)
        
        self.requires(subsystems.climbmech)
        self.requires(subsystems.pistons)

        if(robotmap.debug.is_set):
            self.requires(subsystems.debugsystem)
        #self.requires(subsystems.liftmech)

        #self.sd = NetworkTables.getTable("SmartDashboard")
        self.logger = logging.getLogger("robot")

        #oi.start_btn.whenPressed(SwitchCamera())

        self.timer = Timer()
        
        self.intake_state = 0

        self.lift_pan_status = True 
 
    def initialize(self):
        self.timer.start()

    def execute(self):
        if self.timer.hasPeriodPassed(0.05):

            is_pressed = {}
            for button in Buttons.values:
                is_pressed[button] = oi.controller.getRawButton(button)
            
            if oi.controller.getBackButton():
                self.logger.info("Back button is being held!")
                
            #if robotmap.debug.is_set:
            #    if oi.controller.getBackButton():
            #        self.logger.info("Running debug system...")
            #        subsystems.debugsystem.my_motor.set(robotmap.debug.power)
            #    else:
            #        subsystems.debugsystem.my_motor.set(0.0)

            if oi.controller.getRawButtonPressed(robotmap.controller_bindings.control_lift_pan):
                ## Toggle the lift pan status
                if self.lift_pan_status: #lower them
                    subsystems.pistons.piston1.set(DoubleSolenoid.Value.kReverse)
                    self.lift_pan_status = False
                else:
                    subsystems.pistons.piston1.set(DoubleSolenoid.Value.kForward)
                    self.lift_pan_status = True

            if oi.controller.getRawButtonPressed(robotmap.controller_bindings.control_pushers):
                # push out
                subsystems.pistons.piston2.set(DoubleSolenoid.Value.kForward)
                subsystems.pistons.piston3.set(DoubleSolenoid.Value.kForward)

            if oi.controller.getRawButtonReleased(robotmap.controller_bindings.control_pushers):
                # retract
                subsystems.pistons.piston2.set(DoubleSolenoid.Value.kReverse)
                subsystems.pistons.piston3.set(DoubleSolenoid.Value.kReverse)

            ## LIFTER LOGIC

            #if is_pressed[robotmap.controller_bindings.lift_raise]:
            #    # raise the lift
            #    if robotmap.lift_mech.slowable and oi.controller.getBackButton():
            #        subsystems.liftmech.set_lift_speed(robotmap.lift_mech.power/3.0)
            #    else:
            #        subsystems.liftmech.set_lift_speed(robotmap.lift_mech.power)

            #elif is_pressed[robotmap.controller_bindings.lift_lower]:
            #    # lower the lift
            #    if robotmap.lift_mech.slowable and oi.controller.getBackButton():
            #        subsystems.liftmech.set_lift_speed(-robotmap.lift_mech.power/3.0)
            #    else:
            #        subsystems.liftmech.set_lift_speed(-robotmap.lift_mech.power)
            #else:
            #    # turn off lift
            #    subsystems.liftmech.set_lift_speed(0.0)


            ## GRABBER LOGIC
            
            #if is_pressed[robotmap.controller_bindings.intake_in]:
            #    if self.intake_state != 1:
            #        self.intake_state = 1 # means IN
            #    else:
            #        self.intake_state = 0
            #elif is_pressed[robotmap.controller_bindings.intake_out]:
            #    if self.intake_state != 2:
            #        self.intake_state = 2
            #    else:
            #        self.intake_state = 0

            #if self.intake_state == 1:
            #    # make the intake come 
            #    self.logger.info("Currently Grabbing IN")
            #    subsystems.grabber.set_mode(Grabber.GRABBER_IN)

            #elif self.intake_state == 2:
            #    # make the intake go out
            #    self.logger.info("Currently Grabbing OUT")
            #    subsystems.grabber.set_mode(Grabber.GRABBER_OUT)

            #else:
            #    # turn off intake
            #    subsystems.grabber.set_mode(Grabber.GRABBER_IDLE)

                
            ## Patrick likes inverted controls, so here he goes
            if oi.controller.getStartButtonPressed():
                robotmap.joystick.inverted = not robotmap.joystick.inverted

            ## CLIMBER LOGIC

            if oi.controller.getBumper(GenericHID.Hand.kLeft):
                subsystems.climbmech.motor_a.set(robotmap.climb_mech.speed)
                subsystems.climbmech.motor_b.set(robotmap.climb_mech.speed)
            elif oi.controller.getBumper(GenericHID.Hand.kRight):
                subsystems.climbmech.motor_a.set(-robotmap.climb_mech.speed)
                subsystems.climbmech.motor_b.set(-robotmap.climb_mech.speed)
            else:
                subsystems.climbmech.motor_a.set(0.0)
                subsystems.climbmech.motor_b.set(0.0)
