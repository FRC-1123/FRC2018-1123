from wpilib import Joystick, XboxController

import robotmap

joystick = None
controller = None


def init():
    """
    Initialize operator input (OI) objects.
    """
    global joystick, controller

    joystick = Joystick(robotmap.controller.port)
    controller = XboxController(robotmap.controller.port)