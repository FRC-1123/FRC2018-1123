
class PropertySet:
    """
    Dummy class to store properties for an object.
    """
    pass

class Buttons:
	"""
	Enum for making controller bindings easier.
	This simply makes the bindings for various actions easier to change, by putting
	them in this file.
	"""
	A, B, Y, X = range(4)
	# Note, these do not correspond to the actual button ids on the controller


drivetrain = PropertySet()
## These are CAN ports, PDP is usually 0
drivetrain.left_front_id = 1
drivetrain.left_back_id = 2
drivetrain.right_front_id = 3
drivetrain.right_back_id = 4

## These values are multiplied by the power values before the motors get set to those
## speeds. This is used to "manually" fix wheels moving at different speeds; these values
## were found empirically by running the wheels for one revolution and counting the difference.

## This does not handle when left/right are the same and the robot curves; that will be 
## handled by the PID system.

## These values should always be LESS THAN 1.0
drivetrain.left_front_multiplier = 1.0
drivetrain.left_back_multiplier = 1.0
drivetrain.right_front_multiplier = 1.0
drivetrain.right_back_multiplier = 1.0

lift_mech = PropertySet()
lift_mech.motor = 5

intake = PropertySet()
intake.left_motor = 0
intake.right_motor = 1

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