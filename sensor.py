import RPi.GPIO as GPIO
import time

# Pin donde está conectado el sensor MC38
sensorPin = 12      
buzzerPin = 18

GPIO.setmode(GPIO.BCM)

# Sensor pin como entrada
GPIO.setup(sensorPin, GPIO.IN)

# Sensor pin como salida
GPIO.setup(buzzerPin, GPIO.OUT)

try:
    while True:
        # Leer el estado del sensor
        sensorState = GPIO.input(sensorPin)

        # Verificar si se detectó un contacto
        if sensorState == GPIO.HIGH:
            print("Contacto detectado: ABIERTO")
            # Encender el buzzer
            GPIO.output(buzzerPin, GPIO.HIGH)
            time.sleep(0.2)
            #Apagar el buzzer
            GPIO.output(buzzerPin, GPIO.LOW)
            time.sleep(0.2)
        else:
            print("Contacto detectado: CERRADO")
            # Apagar el buzzer
            GPIO.output(buzzerPin, GPIO.LOW)

        #time.sleep(0.5)  # Esperar un segundo antes de volver a leer el sensor

except KeyboardInterrupt:
    pass

finally:
    # Limpia la configuración de GPIO
    GPIO.cleanup()
