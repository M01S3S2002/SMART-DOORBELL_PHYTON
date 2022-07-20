import subprocess
import os
from time import sleep # Función sleep del módulo time					 
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    if GPIO.input(10) == GPIO.HIGH:
        print("BOTON PULSADO.")
        p1 = subprocess.Popen(['python3','correo_4.py'])
        sleep(7)
        os.system("pkill -f 'python3 correo_4.py' ")