#############################################################
#  ########\                                                #
#  ##  _____|                                               #
#  ## |       ######\####\   #######\                       #
#  #####\     ##  _##  _##\ ##  _____|                      #
#  ##  __|    ## / ## / ## |## /                            #
#  ## |       ## | ## | ## |## |                            #
#  ########\  ## | ## | ## |\#######\                       #
#  \________| \__| \__| \__| \_______|                      #
#    Ércio       Marcelo       Cainã                        #
#                                                           #
#  Intensidade de Luz                                       #
#  O pino 7 recebe uma tensão conforme a luz                #
#  Do ambiente é modificada.                                #
#                                                           #
#  Autores: Marcelo Josué Telles,                           #
#           Ércio Luis Dorneles Berna,                      #
#           Cainã Silva da Costa                            #
#                                                           #
#  Data: 03/06/2017                                         #
#############################################################
#Definindo a utilização da biblioteca GPIO
import RPi.GPIO as GPIO
#importação da biblioteca time para utilizar temporizadores
import time
#Aqui definimos que vamos usar o numero de ordem do pino, e
#	não o numero que refere a porta
#Para usar o numero da porta, é preciso trocar a definição 
#	"GPIO.BOARD (12)" para "GPIO.BCM (18)" 
#Definindo a pinagem real
GPIO.setmode(GPIO.BOARD)
#Definindo o pino a ser utilizado
pin_to_circuit = 7

def rc_time (pin_to_circuit):
    count = 0
    #pino será utilizado como saída
    GPIO.setup(pin_to_circuit, GPIO.OUT)
	#pino é desligado 
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)
    #pino será utilizado como entrada neste caso o pino vai receber a tensão enviada pelo 3.3v
    GPIO.setup(pin_to_circuit, GPIO.IN)
    #O contador será incrementado enquando o pino receber tensão.
	#Note que quanto mais luz o LDR receber, mais a resistência reduz e mais tensão é recebida.
	#Quanto menos luz receber, mais a resistência aumenta e menos tensão é recebida.
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count += 1
    return count
#capturando a interupção e liberando os pinos 
try:
    #Laço principal
    while True:
        print rc_time(pin_to_circuit)
except KeyboardInterrupt:
    print("Fim de programa. \n")
    pass
finally:
    GPIO.cleanup()
#Fonte: https://pimylifeup.com/raspberry-pi-light-sensor/	
