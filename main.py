"""
CODE FOR CRAWL BOT ___ IN PYTHON !!!
"""
import sys
import vex

#region config

#endregion config
class Robot():
    def __init__(self):
        self.base_m     = vex.Motor(2)
        self.claw_m     = vex.Motor(6) 
        self.shoulder_m = vex.Motor(3)
        self.arm_m      = vex.Motor(7)
        self.joystick   = vex.Joystick()
        
        
    def run(self):
        self.exam_fun()
        
    def exam_fun(self):
        """
        test test test
        """
        while True:
            # Driver control code here, setting motors based on joystick movements
            # if self.joystick.b5down() is False and self.joystick.b5up() is False:
            #     self.base_m.off()
            # elif self.joystick.b5down():
            #     self.base_m.run(50)
            # elif self.joystick.b5up():
            #     self.base_m.run(-50)
            
            #base
            if self.joystick.axis4() != 0:
                self.base_m.run(self.joystick.axis4())
            elif self.joystick.axis4() == 0:
                self.base_m.off()
            
            #shoulder
            if self.joystick.b7up() is False and self.joystick.b7down() is False:
                self.shoulder_m.off()
            elif self.joystick.b7up():
                self.shoulder_m.run(-30)
            elif self.joystick.b7down():
                self.shoulder_m.run(30)
                
            #arm
            if self.joystick.axis2() != 0:
                self.arm_m.run(self.joystick.axis2())
            elif self.joystick.axis2() == 0:
                self.arm_m.off()
                
            #claw
            if self.joystick.b8up() is False and self.joystick.b8down() is False:
                self.claw_m.off()
            elif self.joystick.b8up():
                self.claw_m.run(-50)
            elif self.joystick.b8down():
                self.claw_m.run(50)
            
           
    
bot = Robot()
bot.run()
