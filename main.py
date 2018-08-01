#!/usr/bin/python3

"""
imports the necessary libraries
"""
import sys
import vex


__robotName__ = "LittleFoot"

class Robot:
    """
    Robot code for LittleFoot
    """
    
    def __init__(self):
        """
        Initializes the Motor, Joystick, and Sensor variables.
        Each motor is connected to a port on the microcontroller.
        The port # in .Motor(#) is the port number.
        These variables are called / used by later methods in this class.
        """
        self.mclaw  = vex.Motor(2)
        self.mbleft  = vex.Motor(3, True)
        self.mbright  = vex.Motor(4)
        self.mwrist  = vex.Motor(5)
        self.joystick = vex.Joystick()
        self.joystick.set_deadband(10)

    def run(self):
        """
        Runs the program
        """
        self.drive()

    def drive(self):
        """
        User defined Logic
        """
        
        while True:

            # base left axis 3
            
            if self.joystick.axis3() != 0:
                self.mbleft.run(self.joystick.axis3())
            else:
                self.mbleft.off()
                

            # base right axis 2
            
            if self.joystick.axis2() != 0:
                self.mbright.run(self.joystick.axis2())
            else:
                self.mbright.off()
            

            # wrist b5
            
            if self.joystick.b5up() is False and self.joystick.b5down() is False:
                self.mwrist.off()
            elif self.joystick.b5up():
                self.mwrist.run(-50)
            elif self.joystick.b5down():
                self.mwrist.run(40)
                
            # claw b8
            
            if self.joystick.b8down() is False and self.joystick.b8left() is False:
                self.mclaw.off()
            elif self.joystick.b8down():
                self.mclaw.run(-30)
            elif self.joystick.b8left():
                self.mclaw.run(30)
            
           
LittleFoot = Robot()
LittleFoot.run()
