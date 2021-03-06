
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
	_, X, A, B, Y, LB, RB, LT, RT = range(9)

	values = [X, A, B, Y, LB, RB, LT, RT]
	# These correspond to the actual button ID's on the Logitech Controller


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
drivetrain.left_back_multiplier = 0.95
drivetrain.right_front_multiplier = 1.0
drivetrain.right_back_multiplier = 0.9

#lift_mech = PropertySet()
#lift_mech.motor = 6
#lift_mech.power = 1.0
#lift_mech.slowable = True

autonomous = PropertySet()
autonomous.mode = 0

climb_mech = PropertySet()
climb_mech.motor_a = 5
climb_mech.motor_b = 6
climb_mech.speed = 0.5

#intake = PropertySet()
#intake.left_motor = 5
#intake.right_motor = 9

cameras = PropertySet()

joystick = PropertySet()
joystick.left_x_axis = 0
joystick.left_y_axis = 1
joystick.right_x_axis = 2
joystick.right_y_axis = 3
joystick.inverted = False

controller = PropertySet()
controller.port = 0
controller.joystick = joystick

## This was only temporarily used for running a single
## talon's motor for testing purposes
debug = PropertySet()
debug.is_set = False
debug.port = 18
debug.power = 0.5

pistons = PropertySet()

## Raising piston
pistons.piston1_forward = 1001
pistons.piston1_reverse = 1002

## Pushing things
pistons.piston2_forward = 1003
pistons.piston2_reverse = 1004
pistons.piston3_forward = 1005
pistons.piston3_reverse = 1006

## This one is used for lifting the thing
pistons.piston4_forward = 1007
pistons.piston4_reverse = 1008


controller_bindings = PropertySet()

controller_bindings.pistonlift_up = Buttons.X
controller_bindings.pistonlift_down = Buttons.Y

controller_bindings.control_lift_pan = Buttons.A # Toggle

controller_bindings.control_pushers = Buttons.B