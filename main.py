import time
from bridge import (Actuator, Replacer, Vision, Referee)


if __name__ == "__main__":

    mray = False             # Escolha o time: True para Amarelo ou False para Azul (mray = My Robots Are Yellow)

    # Initialize all clients
    actuator = Actuator(mray, "127.0.0.1", 20011)
    replacement = Replacer(mray, "224.5.23.2", 10004)
    vision = Vision(mray, "224.0.0.1", 10002)
    referee = Referee(mray, "224.5.23.2", 10003)

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

        robo0Azul = data_our_bot[0]
        xAzul0 = robo0Azul.x
        #print("Posição x: ", xAzul0)
        yAzul0 = robo0Azul.y
        #print("Posicao y: ", yAzul0)
        #print("")

        xBola = data_ball.x
        yBola = data_ball.y
        print("X bola: ", xBola)
        print("Y bola: ", yBola)
        print("")

        '''
            Para enviar uma velocidade para o simulador, utilizem o seguinte comando:
            - actuator.send(index, vL, vR)
            index: O índice do robô que você quer mover (0, 1 ou 2)
            vL: Velocidade da roda esquerda em m/s
            vR: Velocidade da roda direita em m/s
        '''

        # synchronize code execution based on runtime and the camera FPS
        t2 = time.time()
        if t2 - t1 < 1 / 60:
            time.sleep(1 / 60 - (t2 - t1))
