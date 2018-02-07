#!/usr/bin/env python3

import wpilib
from commandbased import CommandBasedRobot
from commands.respondtocontroller import RespondToController
from commands.updatenetworktables import UpdateNetworkTables
from networktables import NetworkTables

import subsystems

class Robot(CommandBasedRobot):

    def robotInit(self):
    	subsystems.init()

    def autonomousInit(self):
    	pass

    def teleopInit(self):
        RespondToController().start()
        UpdateNetworkTables().start()

if __name__ == "__main__":
	wpilib.run(Robot)