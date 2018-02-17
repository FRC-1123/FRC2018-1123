
class PropertySet:
    """
    Dummy class to store properties for an object.
    """
    pass

class Buttons:
	"""
	Enum for making controller bindings easier
	"""
	A, B, Y, X = range(4)
	# Note, these do not correspond to the actual button ids on the controller


## PLACEHOLDER VALUES
drivetrain = PropertySet()
drivetrain.left_front_id = 2
drivetrain.left_back_id = 4
drivetrain.right_front_id = 3
drivetrain.right_back_id = 1

lift_mech = PropertySet()
lift_mech.motor = 5

intake = PropertySet()
intake.left_motor = 6
intake.right_motor = 7

cameras = PropertySet()

joystick = PropertySet()
joystick.left_x_axis = 0
joystick.left_y_axis = 1
joystick.right_x_axis = 2
joystick.right_y_axis = 3

controller = PropertySet()
controller.port = 0
controller.joystick = joystick

controller_bindings = PropertySet()
controller_bindings.intake_in = Buttons.A
controller_bindings.intake_out = Buttons.B
controller_bindings.lift_raise = Buttons.X
controller_bindings.lift_lower = Buttons.Y
# redundant reference, but makes it a little more clear