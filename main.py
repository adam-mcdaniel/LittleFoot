#!/usr/bin/python3

'''
imports the necessary libraries
'''
import sys
import vex
# import timer


'''
Initializes the Motor, Joystick, and Sensor variables.
Each motor is connected to a port on the microcontroller.
The port # in .Motor(#) is the port number.
These variables are called / used by later methods in this class.
'''

# MOTORS
__robotName__ = 'LittleFoot'
_claw = vex.Motor(2)
_forwardLeft = vex.Motor(3, True)
_forwardRight = vex.Motor(4)
_wrist = vex.Motor(5)
_backRight = vex.Motor(6)
_backLeft = vex.Motor(7, True)

# JOYSTICK
joystick = vex.Joystick()
joystick.set_deadband(10)


def run():
    '''
    Runs the program
    '''
    drive()


def leftDrive(power):
    '''
    Controls the left motors
    Takes joystick axis as parameter
    '''
    _forwardLeft.run(power)
    _backLeft.run(power)

    # left_base_motor.run(joystick.axis3())
    # motor_7.run(joystick.axis3())


def rightDrive(power):
    '''
    Controls the right motors
    Takes joystick axis as parameter
    '''
    _forwardRight.run(power)
    _backRight.run(power)

    # right_base_motor.run(joystick.axis2())
    # motor_6.run(joystick.axis2())


def tankDrive(leftAxis, rightAxis):
    '''
    tank drive
    takes the left and right axis as prarameter
    '''
    leftDrive(leftAxis)
    rightDrive(rightAxis)


def arcadeDrive(forwardAxis, SteerAxis):
    '''
    arcade drive
    takes the forward and steer axis as prarameter
    '''
    steer = forwardAxis
    forward = - SteerAxis

    # calculate left and right power
    left = forward + steer
    right = forward - steer

    # apply power to motors
    leftDrive(left)
    rightDrive(right)


def drive():
    '''
    User defined Logic
    '''
    timer = 201
    buttonTimer = 100
    clawOpen = False

    while True:
        # base left axis 3
        # base right axis 2
        tankDrive(joystick.axis3(), joystick.axis2())

        # wrist b5
        if joystick.b5up():
            _wrist.run(-70)
        elif joystick.b5down():
            _wrist.run(70)
        else:
            _wrist.off()

        # claw b8
        if joystick.b8down() and buttonTimer > 100:
            if clawOpen:
                clawOpen = False
                timer = 0
            elif clawOpen is False:
                clawOpen = True
                timer = 0
            buttonTimer = 0

        if timer < 200:
            timer += 1
            if clawOpen:
                _claw.run(-50)
            elif clawOpen is False:
                _claw.run(50)
        elif timer >= 200:
            _claw.off()

        # applies continued closing force

        # elif timer >= 200 and clawOpen == False:
        #     claw_motor.run(-30)

        if buttonTimer <= 100:
            buttonTimer += 1
        if timer >= 250:
            timer = 0

 #########################################################
        #  # claw b8
        # if joystick.b8down() and buttonTimer > 100:
        #     if clawOpen:
        #         clawOpen = False
        #         timer = 0
        #     elif clawOpen is False:
        #         clawOpen = True
        #         timer = 0
        #     buttonTimer = 0

        # if timer < 200:
        #     timer += 1
        #     if clawOpen:
        #         _claw.run(-50)
        #     elif clawOpen is False:
        #         _claw.run(50)
        # elif timer >= 200:
        #     _claw.off()

        # # applies continued closing force

        # # elif timer >= 200 and clawOpen == False:
        # #     claw_motor.run(-30)

        # if buttonTimer <= 100:
        #     buttonTimer += 1
        # if timer >= 250:
        #     timer = 0
 #########################################################            


run()
