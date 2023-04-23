import numpy as np

class Robot:
    def __init__(self, index, actuator):
        self.index = index
        self.actuator = actuator
        self.x = 0
        self.y = 0
        self.angulo = 0
        self.speed = 20
        self.L = 7.5
        self.R = 3.5


    # Getters
    def get_xPosRobot(self):
        return self.xPos

    def get_yPosRobot(self):
        return self.yPos

    def get_theta(self):
        return self.theta

    def get_L(self):
        return self.L

    def get_R(self):
        return self.R
    

    # Setters
    def set_xPosRobot(self, xPos):
        self.xPos = xPos

    def set_yPosRobot(self, yPos):
        self.yPos = yPos

    def set_theta(self, theta):
        self.theta = theta

    def set_L(self, L):
        self.L = L

    def set_R(self, R):
        self.R = R

    def setPoseRobot(self, xPos, yPos, theta):
        self.set_xPosRobot(xPos)
        self.set_yPosRobot(yPos)
        self.set_theta(theta)

    def setVel(self, vL, vR):
        self.actuator.send(self.index, vL, vR)
    
    def get_index(self):
        return self.index
    




class Ball():
    def __init__(self, xPos=0, yPos=0):
        self.xPosBall = xPos
        self.yPosBall = yPos


    #Getters
    def get_xPosBall(self):
        return self.xPos

    def get_yPosBall(self):
        return self.yPos
    
    #Setters
    def set_xPosBall(self, xPos):
        self.xPos = xPos

    def set_yPosBall(self, yPos):
        self.yPos = yPos

    def setPoseBall(self, xPos, yPos):
        self.set_xPosBall(xPos)
        self.set_yPosBall(yPos)

