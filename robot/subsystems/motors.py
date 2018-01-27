import ctre
import wpilib
from networktables import NetworkTables
from wpilib.command.subsystem import Subsystem
from ctre.wpi_talonsrx import TalonSRX
from wpilib.drive import DifferentialDrive

import robotmap

class Motors(Subsystem):
    """
    This subsystem will control the motors
    Details TBD
    """

    def __init__(self):
        super().__init__("Motors")

        lfm = TalonSRX(robotmap.motors.left_front_id)
        #lfm.setControlMode(TalonSRX.ControlMode.Speed)
        #lfm.setFeedbackDevice(TalonSRX.FeedbackDevice.QuadEncoder)
        
        lbm = TalonSRX(robotmap.motors.left_back_id)
        #lbm.setControlMode(TalonSRX.ControlMode.Speed)
        #lbm.setFeedbackDevice(TalonSRX.FeedbackDevice.QuadEncoder)
        
        rfm = TalonSRX(robotmap.motors.right_front_id)
        #rfm.setControlMode(TalonSRX.ControlMode.Speed)
        #rfm.setFeedbackDevice(TalonSRX.FeedbackDevice.QuadEncoder)
        
        rbm = TalonSRX(robotmap.motors.right_back_id)
        #rbm.setControlMode(TalonSRX.ControlMode.Speed)
        #rbm.setFeedbackDevice(TalonSRX.FeedbackDevice.QuadEncoder)

        self.left_front_motor = lfm
        self.left_back_motor = lbm
        self.right_front_motor = rfm
        self.right_back_motor = rbm

        self.left = wpilib.SpeedControllerGroup(lfm, lbm)
        self.right = wpilib.SpeedControllerGroup(rfm, rbm)

        self.drive = DifferentialDrive(self.left, self.right)
        #self.robot_drive = wpilib.RobotDrive(
        #    frontLeftMotor = self.left_front_motor,
        #    rearLeftMotor = self.left_back_motor,
        #    frontRightMotor = self.right_front_motor,
        #    rearRightMotor = self.right_back_motor)       
