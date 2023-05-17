from threading import Thread
import time

def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        trajeto += velocidade
        time.sleep(0.5)  # import time
        print('Carro: {} km {} \n'.format( piloto, trajeto))


t_carro1 = Thread(target=carro, args=[2.5, 'Antonio'])
t_carro2 = Thread(target=carro, args=[3, 'Guilherme'])

t_carro1.start()
t_carro2.start()