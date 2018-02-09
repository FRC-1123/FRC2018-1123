#!/usr/bin/env python3

import wpilib
from commandbased import CommandBasedRobot
from commands.respondtocontroller import RespondToController
from commands.updatenetworktables import UpdateNetworkTables
from networktables import NetworkTables
from inputs import oi

import subsystems

class Robot(CommandBasedRobot):

    def robotInit(self):
        subsystems.init()

        self.sd = NetworkTables.getTable("SmartDashboard")
        self.ds = wpilib.DriverStation.getInstance()
        self.game_data = ""
        oi.init()

    def autonomousInit(self):
        self.game_data = self.ds.getGameSpecificMessage()


    def teleopInit(self):
        RespondToController().start()
        UpdateNetworkTables().start()

if __name__ == "__main__":
    wpilib.run(Robot)