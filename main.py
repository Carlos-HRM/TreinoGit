import time
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
        robot.setPoseRobot(data_our_bot[0].x, data_our_bot[0].y, data_our_bot[0].a)
        
        print("Posição x: ", robot.get_xPosRobot())
        print("Posicao y: ", robot.get_yPosRobot())
        print("")

        ball.setPoseBall(data_ball.x ,data_ball.y)
        print("X bola: ", ball.get_xPosBall())
        print("Y bola: ", ball.get_yPosBall())
        print("")
        
      
        # synchronize code execution based on runtime and the camera FPS
        t2 = time.time()
        if t2 - t1 < 1 / 60:
            time.sleep(1 / 60 - (t2 - t1))
