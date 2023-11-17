import RPi.GPIO as GPIO
import time

def correrServo2(servo_pin):

    #servo_pin = 17  # Pin GPIO utilizado para controlar el servo

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servo_pin, GPIO.OUT)

    pwm = GPIO.PWM(servo_pin, 50)  # Frecuencia de PWM: 50 Hz
    pwm.start(0)  # Iniciar el PWM con un ciclo de trabajo del 0%

    def set_speed(speed):
        duty_cycle = speed * 0.1 + 1.7  # Calcular el ciclo de trabajo necesario para la velocidad deseada
        pwm.ChangeDutyCycle(duty_cycle)
        print(duty_cycle)

    try:
        set_speed(1)  # Establecer la velocidad máxima en sentido horario (valor de 10)
        time.sleep(0.146)  # Mantener la velocidad máxima durante 5 segundos

        set_speed(0)   # Detener el servo

    except KeyboardInterrupt:
        pwm.stop()
        GPIO.cleanup()

#correrServo2(24)
#17 5
#27 2
#22 4
#23 6
#24 1
#25 3


