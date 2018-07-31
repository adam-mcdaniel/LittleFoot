#!/usr/bin/python3

"""
* This file contains the code for the LittleFoot bot
* The code and this support page for the softwares 
  belongs to the South Doyle Robotics Team
* The code and this Documentation isn't open source, 
  it's intended for protected uses ```ONLY``` .
"""


"""
imports the necessary libraries
"""
import sys
import vex

__robotName__ = "LittleFoot"

class Robot:
<<<<<<< HEAD
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
        self.base_m     = vex.Motor(2)
        self.claw_m     = vex.Motor(6) 
        self.arm_m      = vex.Motor(3)
        self.wrist_m    = vex.Motor(7)
        self.joystick   = vex.Joystick()

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

            # base motor -- being controled by buttons
            
            if self.joystick.b7left() is False and self.joystick.b7right() is False:
                self.base_m.off()
            elif self.joystick.b7left():
                self.base_m.run(-35)
            elif self.joystick.b7right():
                self.base_m.run(35)

            # wrist motor -- being controled by buttons
            
            if self.joystick.b5up() is False and self.joystick.b5down() is False:
                self.wrist_m.off()
            elif self.joystick.b5down():
                self.wrist_m.run(-50)
            elif self.joystick.b5up():
                self.wrist_m.run(50)
            

            # claw motor -- being controled by buttons
            
            if self.joystick.b8up() is False and self.joystick.b8down() is False:
                self.claw_m.off()
            elif self.joystick.b8up():
                self.claw_m.run(-50)
            elif self.joystick.b8down():
                self.claw_m.run(50)
                
            # arm motor -- being controled by buttons
            
            if self.joystick.b6down() is False and self.joystick.b6up() is False:
                self.arm_m.off()
            elif self.joystick.b6down():
                self.arm_m.run(-30)
            elif self.joystick.b6up():
                self.arm_m.run(30)
            
           
LittleFoot = Robot()
LittleFoot.run()
=======
	"""
	Robot code for LittleFoot
	"""
	
	def __init__(self):
		"""
		Initializes the variables
		"""
		self.base_m     = vex.Motor(2)
		self.claw_m     = vex.Motor(6) 
		self.arm_m      = vex.Motor(3)
		self.wrist_m    = vex.Motor(7)
		self.joystick   = vex.Joystick()
	   
	def run(self):
		"""
		Runs the code
		"""
		self.drive()
		

	def drive(self):
		"""
		User defined codes
		"""
		while True:
    			
			"""
			base motor -- axis
			"""
		
			if self.joystick.axis4() != 0:
				self.base_m.run(self.joystick.axis4())
			elif self.joystick.axis4() == 0:
				self.base_m.off()
				
			"""
			wrist motor -- axis
			"""
			
			if self.joystick.axis2() != 0:
				self.wrist_m.run(self.joystick.axis2())
			elif self.joystick.axis2() == 0:
				self.wrist_m.off()
			
			"""
			claw motor -- button
			"""
			
			if self.joystick.b8up() is False and self.joystick.b8down() is False:
				self.claw_m.off()
			elif self.joystick.b8up():
				self.claw_m.run(-50)
			elif self.joystick.b8down():
				self.claw_m.run(50)
				
			"""
			arm motor -- button
			"""
			
			if self.joystick.b7up() is False and self.joystick.b7down() is False:
				self.arm_m.off()
			elif self.joystick.b7up():
				self.arm_m.run(-30)
			elif self.joystick.b7down():
				self.arm_m.run(30)


if __name__ == "main":
	LittleFoot = Robot()
	# LittleFoot.run()
