import wpilib
from networktables import NetworkTables
from wpilib.command.commandgroup import CommandGroup
from commands.driveforward import DriveForward
from commands.setforwardspeed import SetForwardSpeed
from commands.setspeeds import SetSpeeds

import subsystems

class AutonomousProgram(CommandGroup):

    def __init__(self):
        super().__init__("Autonomous Program")

        #self.addSequential()

        self.sd = NetworkTables.getTable("SmartDashboard")

        #self.addSequential(SetForwardSpeed(0.5, 1.0, False))
        #self.addSequential(SetSpeeds(0.1, 0.7, 0.2, False))
        #self.addSequential(SetForwardSpeed(0.5, 0.3, False))
        #self.addSequential(SetSpeeds(0.7, 0.1, 0.2, False))
        self.addSequential(SetForwardSpeed(0.5, 5.0, False))

        #self.addSequential(DriveForward(0.4, 3.0))