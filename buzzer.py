import RPi.GPIO as GPIO
import time

# Configuración de la biblioteca RPi.GPIO
GPIO.setmode(GPIO.BCM)

def recordatorio_alarma(pin=18, repeticiones=5, duracion=0.5, descanso=0.5):
    GPIO.setup(pin, GPIO.OUT)

    try:
        for _ in range(repeticiones):
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(duracion)
            GPIO.output(pin, GPIO.LOW)
            time.sleep(descanso)

    except KeyboardInterrupt:
        pass

    finally:
        GPIO.cleanup()

def entrega_pastilla(pin_buzzer=18, duracion=0.6):
    GPIO.setup(pin_buzzer, GPIO.OUT)

    try:
        GPIO.output(pin_buzzer, GPIO.HIGH)
        time.sleep(duracion)
        GPIO.output(pin_buzzer, GPIO.LOW)

    except KeyboardInterrupt:
        pass

    finally:
        GPIO.cleanup()

