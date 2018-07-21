#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
CODE FOR CRAWL BOT ___ IN PYTHON !!!
"""

# imports
import sys
import vex

__robotName__ = "LittleFoot"

class Robot:
    """
    Robot code for LittleFoot
    """
    
    def __init__(self):
        self.base_m     = vex.Motor(2)
        self.claw_m     = vex.Motor(6) 
        self.arm_m      = vex.Motor(3)
        self.wrist_m    = vex.Motor(7)
        self.joystick   = vex.Joystick()
        
    def run(self):
        self.drive()
        
#     def motor_to_button(self, _motor, li_button, li_power=[-50,50]):
#         if self.joystick.li_button[0]() is False and self.joystick.li_button[1]() \
#                 is False:
#             self._motor.off()
#         elif self.joystick.li_button[0]():
#             self.shoulder_m.run(li_power[0])
#         elif self.joystick.li_button[1]():
#             self.shoulder_m.run(li_power[1])
                
#     def motor_to_axis(self, _motor, _axis)
#         if self.joystick._axis() != 0:
#             self._motor.run(self.joystick._axis())
#         elif self.joystick._axis() == 0:
#             self._motor.off()

    def drive(self):
        """
        User defined codes
        """
        
        while True:

            # base motor -- axis
            
            if self.joystick.axis4() != 0:
                self.base_m.run(self.joystick.axis4())
            elif self.joystick.axis4() == 0:
                self.base_m.off()
#             self.motor_to_axis(base_m, axis4)
                
            # wrist motor -- axis
            
            if self.joystick.axis2() != 0:
                self.wrist_m.run(self.joystick.axis2())
            elif self.joystick.axis2() == 0:
                self.wrist_m.off()
#             self.motor_to_axis(wrist_m, axis2)
            
            # claw motor -- button
            
            if self.joystick.b8up() is False and self.joystick.b8down() is False:
                self.claw_m.off()
            elif self.joystick.b8up():
                self.claw_m.run(-50)
            elif self.joystick.b8down():
                self.claw_m.run(50)
                
            # arm motor -- button
            
            if self.joystick.b7up() is False and self.joystick.b7down() is False:
                self.arm_m.off()
            elif self.joystick.b7up():
                self.arm_m.run(-30)
            elif self.joystick.b7down():
                self.arm_m.run(30)
            
           
LittleFoot = Robot()
LittleFoot.run()
