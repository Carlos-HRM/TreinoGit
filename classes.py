class Robot:
    def __init__(self, index, actuator, speed=10):
        self.index = index
        self.actuator = actuator
        self.x = 0
        self.y = 0
        self.angulo = 0
        self.speed = speed


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
    
    def move_forward(self, speed):
        self.setVel(speed, speed)

    def move_backward(self, speed):
        self.setVel(-speed, -speed)

    def turn_left(self, speed):
        self.actuator.send(self.index, -self.speed, self.speed)

    def turn_right(self, speed):
        self.actuator.send(self.index, self.speed, -self.speed)




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

