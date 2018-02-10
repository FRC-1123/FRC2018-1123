
class PropertySet():
    """
    Dummy class to store properties for an object.
    """
    pass

## PLACEHOLDER VALUES
drivetrain = PropertySet()
drivetrain.left_front_id = 0
drivetrain.left_back_id = 1
drivetrain.right_front_id = 2
drivetrain.right_back_id = 3

lift_mech = PropertySet()
lift_mech.motor_a = 4
lift_mech.motor_b = 5

cameras = PropertySet()

joystick = PropertySet()
joystick.left_x_axis = 0
joystick.left_y_axis = 1
joystick.right_x_axis = 4
joystick.right_y_axis = 5

controller = PropertySet()
controller.port = 0
controller.joystick = joystick
# redundant reference, but makes it a little more clear