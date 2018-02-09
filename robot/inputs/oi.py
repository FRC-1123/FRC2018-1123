from wpilib import Joystick, XboxController

import robotmap

left_joystick = None
right_joystick = None
controller = None


def init():
    """
    Initialize operator input (OI) objects.
    """
    global left_joystick, right_joystick, controller

    left_joystick = Joystick(robotmap.left_joystick.port)
    right_joystick = Joystick(robotmap.right_joystick.port)
    controller = XboxController(robotmap.xbox_controller.port)
