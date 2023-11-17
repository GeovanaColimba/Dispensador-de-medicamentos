import RPi.GPIO as GPIO
import time

def correrServo1(servo_pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servo_pin, GPIO.OUT)

    pwm = GPIO.PWM(servo_pin, 50)  # Frecuencia de PWM: 50 Hz
    pwm.start(0)  # Iniciar el PWM con un ciclo de trabajo del 0%

    def set_angle(angle):
        duty_cycle = angle / 18 + 2
        pwm.ChangeDutyCycle(duty_cycle)
        print("Ángulo:", angle, "Duty Cycle:", duty_cycle)
        time.sleep(0.114)  # Esperar para que el servo alcance el ángulo

    try:
        set_angle(45)  # Girar a grados
        
    except KeyboardInterrupt:
        pwm.stop()
        GPIO.cleanup()

#correrServo1(27)
