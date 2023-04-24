import time
import numpy as np
from bridge import (Actuator, Replacer, Vision, Referee)
from classes import Robot, Ball


if __name__ == "__main__":

    mray = False             # Escolha o time: True para Amarelo ou False para Azul (mray = My Robots Are Yellow)

    # Initialize all clients
    actuator = Actuator(mray, "127.0.0.1", 20011)
    replacement = Replacer(mray, "224.5.23.2", 10004)
    vision = Vision(mray, "224.0.0.1", 10002)
    referee = Referee(mray, "224.5.23.2", 10003)

    #Initialize the robot
    robot = Robot(actuator=actuator, index = 0)
    ball = Ball()

    kp = 1.5



    # Main infinite loop
    while True:
        t1 = time.time()

        # Update the vision data
        vision.update()
        field = vision.get_field_data()

        data_our_bot = field["our_bots"]  # Save data from allied robots
        data_their_bots = field["their_bots"]  # Save data from enemy robots
        data_ball = field["ball"]  # Save the ball data

        '''
            A variavel data_our_bot é uma lista de 3 objetos da classe Entity, do arquivo bridge.py
            Esses objetos possuem as informações dos respectivos robôs do nosso time, seja azul ou amarelo, na seguinte ordem:
            - Posição 0 : Robô 0
            - Posição 1 : Robô 1
            - Posição 2 : Robô 2
            Para acessar as informações x, y, a (angulo) e velocidades, vejam a declaração da classe no arquivo bridge.py
            A variavel data_their_bots segue a mesma ideia, porém para os robôs do outro time
            A variavel data_ball é uma lista única que contém os dados da bola. O acesso a eles é feito da mesma forma, porém ele não possui angulo
        '''



        #atualiza posicao do robo
        robot.setPoseRobot(data_our_bot[0].x, data_our_bot[0].y, data_our_bot[0].a)

        #converte o angulo de radiano para graus
        theta_robot = np.rad2deg(data_our_bot[0].a)

        #atualiza posicao da bola
        ball.setPoseBall(data_ball.x, data_ball.y)

        #calcula angulo entre robo e bola
        theta_d = np.rad2deg(np.arctan2(data_ball.y - data_our_bot[0].y, data_ball.x - data_our_bot[0].x))

        #calcula erro angular
        theta_e = theta_d - theta_robot

        
        #trata o erro angular para garantir que ele esteja sempre entre -180 e 180
        if theta_e > 180:
            theta_e -= 360
        elif theta_e < -180:
            theta_e += 360


        #calcula velocidade angular
        w = kp * np.deg2rad(theta_e)

        #Converte velocidade angular para as rodas
        vel = robot.speed
        l = robot.get_L()
        vel_esq = vel - w * l/2
        vel_dir = vel + w * l/2
        
        #seta a velocidade de cada roda do robô
        robot.setVel(vel_esq, vel_dir)
    

        # synchronize code execution based on runtime and the camera FPS
        t2 = time.time()
        if t2 - t1 < 1 / 60:
            time.sleep(1 / 60 - (t2 - t1))