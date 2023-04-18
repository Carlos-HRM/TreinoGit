import time
import pygame
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

    #Configurando teclas do robô
    keys = {
        pygame.K_UP: 'move_forward',
        pygame.K_DOWN: 'move_backward',
        pygame.K_LEFT: 'turn_left',
        pygame.K_RIGHT: 'turn_right',
    }

    # Rastreie o estado atual de cada tecla
    key_state = {
        pygame.K_UP: False,
        pygame.K_DOWN: False,
        pygame.K_LEFT: False,
        pygame.K_RIGHT: False,
}

    # Create a window (optional)
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("FIRASim Control")
    pygame.key.set_repeat()


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

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key in keys:
                    # Marque a tecla correspondente como pressionada
                    key_state[event.key] = True
            elif event.type == pygame.KEYUP:
                if event.key in keys:
                    # Marque a tecla correspondente como liberada e defina a velocidade do robô para 0
                    key_state[event.key] = False
                    robot.setVel(0, 0)


        # Atualize a velocidade do robô com base nas teclas pressionadas
        if key_state[pygame.K_UP]:
            robot.move_forward(10)
        elif key_state[pygame.K_DOWN]:
            robot.move_backward(10)


        if key_state[pygame.K_LEFT]:
            robot.turn_left(10)
        elif key_state[pygame.K_RIGHT]:
            robot.turn_right(10)

      
        # synchronize code execution based on runtime and the camera FPS
        t2 = time.time()
        if t2 - t1 < 1 / 60:
            time.sleep(1 / 60 - (t2 - t1))
