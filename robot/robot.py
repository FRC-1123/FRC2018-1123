#!/usr/bin/env python3
import logging

import wpilib
from commandbased import CommandBasedRobot
from commands.respondtocontroller import RespondToController
from commands.updatenetworktables import UpdateNetworkTables
from commands.followjoystick import FollowJoystick
from commands.autonomousprogram import AutonomousProgram
from networktables import NetworkTables
from inputs import oi, navx

import subsystems

class Robot(CommandBasedRobot):

    def robotInit(self):
        subsystems.init()

        self.logger = logging.getLogger("robot")	
        self.sd = NetworkTables.getTable("SmartDashboard")
        self.sd.putBoolean("testerino", True)
        self.ds = wpilib.DriverStation.getInstance()
        self.game_data = ""
        
        oi.init()
        navx.init()

    def autonomousInit(self):
        self.game_data = self.ds.getGameSpecificMessage()
        self.logger.info("Starting autonomous, game data is " + str(self.game_data))
        AutonomousProgram().start()

    def teleopInit(self):
        self.logger.info("Teleop starting here!")
        RespondToController().start()
        UpdateNetworkTables().start()
        FollowJoystick().start()
        self.logger.info("Okay I think it started")

if __name__ == "__main__":
    wpilib.run(Robot)