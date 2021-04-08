from time import sleep
import RPi.GPIO as GPIO



MOTOR1_EN = 14
MOTOR1_A = 18
MOTOR1_B = 15

MOTOR2_EN = 25
MOTOR2_A = 8
MOTOR2_B = 7

def stop():
    GPIO.output(MOTOR1_EN, GPIO.LOW)
    GPIO.output(MOTOR2_EN, GPIO.LOW)

def go_recule(duree):
    GPIO.output(MOTOR1_EN, GPIO.HIGH)
    GPIO.output(MOTOR1_A, GPIO.LOW)
    GPIO.output(MOTOR1_B, GPIO.HIGH)

    GPIO.output(MOTOR2_EN, GPIO.HIGH)
    GPIO.output(MOTOR2_B, GPIO.LOW)
    GPIO.output(MOTOR2_A, GPIO.HIGH)
    sleep(duree)
    stop()
    
def go_avance(duree):
    GPIO.output(MOTOR1_EN, GPIO.HIGH)
    GPIO.output(MOTOR1_A, GPIO.HIGH)
    GPIO.output(MOTOR1_B, GPIO.LOW)

    GPIO.output(MOTOR2_EN, GPIO.HIGH)
    GPIO.output(MOTOR2_B, GPIO.HIGH)
    GPIO.output(MOTOR2_A, GPIO.LOW)
    sleep(duree)
    stop()

   
def go_gauche(duree):
    GPIO.output(MOTOR1_EN, GPIO.HIGH)
    GPIO.output(MOTOR1_A, GPIO.LOW)
    GPIO.output(MOTOR1_B, GPIO.HIGH)

    GPIO.output(MOTOR2_EN, GPIO.HIGH)
    GPIO.output(MOTOR2_B, GPIO.HIGH)
    GPIO.output(MOTOR2_A, GPIO.LOW)
    sleep(duree)
    stop()
    
def go_droite(duree):
    GPIO.output(MOTOR1_EN, GPIO.HIGH)
    GPIO.output(MOTOR1_A, GPIO.HIGH)
    GPIO.output(MOTOR1_B, GPIO.LOW)

    GPIO.output(MOTOR2_EN, GPIO.HIGH)
    GPIO.output(MOTOR2_B, GPIO.LOW)
    GPIO.output(MOTOR2_A, GPIO.HIGH)
    sleep(duree)
    stop()


try:

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(MOTOR1_EN, GPIO.OUT)
    GPIO.setup(MOTOR1_A, GPIO.OUT)
    GPIO.setup(MOTOR1_B, GPIO.OUT)

    GPIO.setup(MOTOR2_EN, GPIO.OUT)
    GPIO.setup(MOTOR2_A, GPIO.OUT)
    GPIO.setup(MOTOR2_B, GPIO.OUT)


    while True:
        x = input("Press w")
        if x=="z":
            go_avance(1)
           
        elif x=="s":
            go_recule(1)
           
        elif x=="q":
            go_gauche(0.25)
            
        elif x=="d":
            go_droite(0.25)
            
        else:
            break
            
    stop()

 

except KeyboardInterrupt:
    pass
except:
    GPIO.cleanup()
    raise

GPIO.cleanup()


