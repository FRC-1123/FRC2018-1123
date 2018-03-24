import wpilib
from networktables import NetworkTables
from wpilib.command.commandgroup import CommandGroup
from commands.driveforward import DriveForward
from commands.setforwardspeed import SetForwardSpeed
from commands.setspeeds import SetSpeeds
from commands.turnright90 import TurnRight90
from commands.turnleft90 import TurnLeft90
from commands.dumpblock import DumpBlock

import robotmap
import logging

import subsystems

class AutonomousProgram(CommandGroup):

    def __init__(self, game_data):
        super().__init__("Autonomous Program")

        self.sd = NetworkTables.getTable("SmartDashboard")

        self.requires(subsystems.digitalin)

        self.logger = logging.getLogger("robot")

        if len(game_data) < 3:
            self.logger.info("Game Data not read correctly!")
            game_data = "CCC"

        game_data = game_data.upper()
        self.logger.info("Game Data parsed as " + str(game_data))

        ## Active Low for these pins
        if not subsystems.digitalin.inp1.get():
            self.logger.info("Autonomous #0 Selected: Just Move Straight")
            self.addSequential(SetForwardSpeed(-0.5, 0.3, False))
            self.addSequential(SetForwardSpeed(-0.8, 2.2, False))
            self.addSequential(SetForwardSpeed(-0.5, 0.3, False))

        elif not subsystems.digitalin.inp2.get(): # Autonomous #1: Left Side
            self.logger.info("Autonomous #1 Selected: Left Side")
            self.addSequential(SetForwardSpeed(-0.5, 0.3, False))
            self.addSequential(SetForwardSpeed(-0.8, 2.2, False))
            self.addSequential(SetForwardSpeed(-0.5, 0.3, False))
            if game_data[0] == "L":
                self.logger.info("Our Switch is also Left Side! Will try to dump block")
                self.addSequential(TurnRight90(0.2))
                self.addSequential(DumpBlock())

        elif not subsystems.digitalin.inp3.get(): # Autonomous #2: Right Side
            self.logger.info("Autonomous #2 Selected: Right Side")
            self.addSequential(SetForwardSpeed(-0.5, 0.3, False))
            self.addSequential(SetForwardSpeed(-0.8, 2.2, False))
            self.addSequential(SetForwardSpeed(-0.5, 0.3, False))
            if game_data[0] == "R":
                self.logger.info("Our Switch is also Right Side! Will try to dump block")
                self.addSequential(TurnLeft90(0.2))
                self.addSequential(DumpBlock())

        else:
            self.logger.info("DEFAULT: Autonomous #0 Selected: Just Move Straight")
            self.addSequential(SetForwardSpeed(-0.5, 0.3, False))
            self.addSequential(SetForwardSpeed(-0.8, 2.2, False))
            self.addSequential(SetForwardSpeed(-0.5, 0.3, False))

        
        # if robotmap.autonomous.mode == 0:
        #     self.addSequential(SetForwardSpeed(-0.5, 0.3, False))
        #     self.addSequential(SetForwardSpeed(-0.8, 2.2, False))
        #     self.addSequential(SetForwardSpeed(-0.5, 0.3, False))
        # else:
        #     self.addSequential(SetForwardSpeed(-0.3, 1.0, False))
            
        #     self.addSequential(SetForwardSpeed(0.0, 0.2, False))
        #     self.addSequential(TurnRight90(0.3))
        #     self.addSequential(SetForwardSpeed(0.0, 0.2, False))
            
        #     self.addSequential(SetForwardSpeed(-0.3, 0.3, False))
        #     self.addSequential(SetForwardSpeed(-0.6, 1.2, False))
        #     self.addSequential(SetForwardSpeed(-0.3, 0.3, False))
            
        #     self.addSequential(SetForwardSpeed(0.0, 0.2, False))
        #     self.addSequential(TurnLeft90(0.3))
        #     self.addSequential(SetForwardSpeed(0.0, 0.2, False))
            
        #     self.addSequential(SetForwardSpeed(-0.3, 0.15, False))
        #     self.addSequential(SetForwardSpeed(-0.8, 1.4, False))
        #     self.addSequential(SetForwardSpeed(-0.3, 0.15, False))

        #self.addSequential(DriveForward(0.4, 3.0))