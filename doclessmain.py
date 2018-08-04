#!/usr/bin/python3

'''
imports the necessary libraries
'''
import sys
import vex
import timer


# MOTORS

_claw = vex.Motor(2)
_forwardLeft = vex.Motor(3, True)
_forwardRight = vex.Motor(4)
_wrist = vex.Motor(5)
_backRight = vex.Motor(6)
_backLeft = vex.Motor(7, True)

# JOYSTICK
joystick = vex.Joystick()
joystick.set_deadband(10)


tickTimer = timer.Timer()
tickTimer_max = 1.3
tickTimer.start()
buttonTimer = timer.Timer()
buttonTimer_max = 1.3
buttonTimer.start()
# timer_stopping_point = 10
clawIsOpen = False

while True:
    #########################################################
    if joystick.b5up():
        _wrist.run(-50)
    elif joystick.b5down():
        _wrist.run(50)
    else:
        _wrist.off()
    
    ########################################################
    # claw b8 ++ timer module

    if joystick.b8down() and buttonTimer.elapsed_time() > buttonTimer_max:
        if clawIsOpen:
            clawIsOpen = False
            tickTimer.reset()
            tickTimer.start()
        elif clawIsOpen is False:
            clawIsOpen = True
            tickTimer.reset()
            tickTimer.start()
        buttonTimer.reset()
        buttonTimer.start()
    
    if tickTimer.elapsed_time() < tickTimer_max:
        if clawIsOpen:
            _claw.run(50)
        elif clawIsOpen is False:
            _claw.run(-50)

    else:
        if clawIsOpen:
            _claw.run(100)
        else:
            _claw.off()

    #####################################################
    forward = - joystick.axis3()
    steer = joystick.axis4()

    # calculate left and right power
    left = -(forward + steer)
    right = -(forward - steer)

    
    _forwardLeft.run(left)
    _backLeft.run(left)
    _forwardRight.run(right)
    _backRight.run(right)
    


