import wpilib
from networktables import NetworkTables
from wpilib.command.commandgroup import CommandGroup
from commands.driveforward import DriveForward
from commands.setforwardspeed import SetForwardSpeed
from commands.setspeeds import SetSpeeds
from commands.turnright90 import TurnRight90
from commands.turnleft90 import TurnLeft90

import robotmap

import subsystems

class AutonomousProgram(CommandGroup):

    def __init__(self):
        super().__init__("Autonomous Program")

        #self.addSequential()

        self.sd = NetworkTables.getTable("SmartDashboard")
        
        if robotmap.autonomous.mode == 0:
            self.addSequential(SetForwardSpeed(-0.5, 0.3, False))
            self.addSequential(SetForwardSpeed(-0.8, 2.2, False))
            self.addSequential(SetForwardSpeed(-0.5, 0.3, False))
        else:
            self.addSequential(SetForwardSpeed(-0.3, 1.0, False))
            
            self.addSequential(SetForwardSpeed(0.0, 0.2, False))
            self.addSequential(TurnRight90(0.3))
            self.addSequential(SetForwardSpeed(0.0, 0.2, False))
            
            self.addSequential(SetForwardSpeed(-0.3, 0.3, False))
            self.addSequential(SetForwardSpeed(-0.6, 1.2, False))
            self.addSequential(SetForwardSpeed(-0.3, 0.3, False))
            
            self.addSequential(SetForwardSpeed(0.0, 0.2, False))
            self.addSequential(TurnLeft90(0.3))
            self.addSequential(SetForwardSpeed(0.0, 0.2, False))
            
            self.addSequential(SetForwardSpeed(-0.3, 0.15, False))
            self.addSequential(SetForwardSpeed(-0.8, 1.4, False))
            self.addSequential(SetForwardSpeed(-0.3, 0.15, False))

        #self.addSequential(DriveForward(0.4, 3.0))