import tkinter as tk
from tkinter import messagebox, Entry
import os
import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np
import pickle
from PIL import Image, ImageTk
import sys

sys.path.append("/local/lib/python3.9/site-packages")
print(sys.executable)

camera = None  # Variable global para la cámara


def mostrar_mensaje_top(mensaje, top):
    mensaje_label = tk.Label(top, text=mensaje, fg="red")
    mensaje_label.pack(pady=5)


def cerrar_top(top):
    top.destroy()


def guardar_usuario(top):
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    baseDir = os.path.dirname(os.path.abspath(__file__))
    imageDir = os.path.join(baseDir, "images")

    currentId = 1
    labelIds = {}
    yLabels = []
    xTrain = []

    for root, dirs, files in os.walk(imageDir):
        print(root, dirs, files)
        for file in files:
            print(file)
            if file.endswith("png") or file.endswith("jpg"):
                path = os.path.join(root, file)
                label = os.path.basename(root)
                print(label)

                if not label in labelIds:
                    labelIds[label] = currentId
                    print(labelIds)
                    currentId += 1

                id_ = labelIds[label]
                pilImage = Image.open(path).convert("L")
                imageArray = np.array(pilImage, "uint8")
                faces = faceCascade.detectMultiScale(imageArray, scaleFactor=1.1, minNeighbors=5)

                for (x, y, w, h) in faces:
                    roi = imageArray[y:y + h, x:x + w]
                    xTrain.append(roi)
                    yLabels.append(id_)

    with open("labels", "wb") as f:
        pickle.dump(labelIds, f)
        f.close()

    recognizer.train(xTrain, np.array(yLabels))
    recognizer.save("entrenamiento.yml")
    print(labelIds)
    top.destroy()


def registrar_usuario():
    def capture_images(top):
        global camera  # Acceder a la variable global de la cámara
        if camera is not None:
            camera.close()  # Cerrar la cámara si está en uso

        try:
            camera = PiCamera()
            camera.resolution = (640, 480)
            camera.framerate = 30
            rawCapture = PiRGBArray(camera, size=(640, 480))

            faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

            name = name_entry.get()
            dirName = "/home/pi/Documents/proyectoPastillero/images/" + name

            if not os.path.exists(dirName):
                os.makedirs(dirName)
                mostrar_mensaje_top("Se ha creado el directorio con éxito.", top)
            else:
                mostrar_mensaje_top("Esta persona ya se encuentra registrada.", top)
                return

            count = 1
            for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
                if count > 100:
                    break
                frame = frame.array
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = faceCascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
                for (x, y, w, h) in faces:
                    roiGray = gray[y:y + h, x:x + w]
                    fileName = dirName + "/" + name + str(count) + ".jpg"
                    cv2.imwrite(fileName, roiGray)
                    cv2.imshow("face", roiGray)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    count += 1

                cv2.imshow('frame', frame)
                key = cv2.waitKey(1)
                rawCapture.truncate(0)

                if key == 27:
                    break
            cv2.destroyAllWindows()
            name_entry.delete(0, tk.END)  # Limpiar el campo de entrada

        except picamera.exc.PiCameraMMALError as e:
            print(f"Error de la cámara: {e}")

    top = tk.Toplevel()
    top.title("Captura de Rostros")
    top.geometry("250x185+180+250")

    name_label = tk.Label(top, text="Ingrese el nombre de la persona:")
    name_label.pack(pady=5)

    name_entry = Entry(top)
    name_entry.pack(pady=5)

    # Función para abrir el teclado virtual
    def abrir_teclado_virtual(event):
        os.system("matchbox-keyboard &")

    # Enlazar la función al evento FocusIn
    name_entry.bind("<FocusIn>", abrir_teclado_virtual)

    capture_button = tk.Button(top, text="Iniciar Captura", command=lambda: capture_images(top))
    capture_button.pack(pady=10)

    guardar_button = tk.Button(top, text="Guardar Usuario", command=lambda: guardar_usuario(top))
    guardar_button.pack(pady=10)


def apagar_raspberry():
    global camera  # Acceder a la variable global de la cámara
    if camera is not None:
        camera.close()  # Cerrar la cámara si está en uso

    # Crear una ventana emergente con dos botones (Apagar y Reiniciar)
    popup = tk.Toplevel()
    popup.title("Confirmar Apagado")

    label = tk.Label(popup, text="¿Desea apagar o reiniciar la Raspberry Pi?")
    label.pack(padx=10, pady=10)

    apagar_button = tk.Button(popup, text="Apagar", command=lambda: os.system("sudo shutdown now"))
    apagar_button.pack(pady=10)

    reiniciar_button = tk.Button(popup, text="Reiniciar", command=lambda: os.system("sudo reboot"))
    reiniciar_button.pack(pady=10)


root = tk.Tk()
root.title("Dispensador de Medicamentos")
root.geometry("145x265+1+1")
imagen_path = "/home/pi/Documents/proyectoPastillero/fondo.jpeg"  
imagenfondo = Image.open(imagen_path)
imagenfondo = ImageTk.PhotoImage(imagenfondo)
fondo_label = tk.Label(root, image=imagenfondo)
fondo_label.place(relwidth=1, relheight=1)

imagen_path = "/home/pi/Documents/proyectoPastillero/reg23.jpeg"  
imagenregistro = Image.open(imagen_path)
imagenregistro = ImageTk.PhotoImage(imagenregistro)

registrar_button = tk.Button(root, text="Registrar Usuario", image=imagenregistro, command=registrar_usuario)
registrar_button.place(x=20, y=15)

imagen_path = "/home/pi/Documents/proyectoPastillero/ap1.jpeg"  
imagen = Image.open(imagen_path)
imagen = ImageTk.PhotoImage(imagen)

apagar_button = tk.Button(root, text="Apagar Raspberry Pi", image=imagen, command=apagar_raspberry, width=95, height=95)
apagar_button.place(x=20, y=145)

root.mainloop()
