import pyrebase
from datetime import datetime
from servo003 import *
from servo002 import *
import time
from notificador import *
from modoViaje import *
from twopantallasegunda import *
from buzzer import *


# Configuración de la conexión a Firebase
config = {
    "apiKey": "AIzaSyC4g_kyof0tw_eq8kUBlqLF3rOS-xQxGPg",
    "authDomain": "registro-alarmas.firebaseapp.com",
    "databaseURL": "https://registro-alarmas-default-rtdb.firebaseio.com",
    "projectId": "registro-alarmas",
    "storageBucket": "registro-alarmas.appspot.com",
    "messagingSenderId": "606369683568",
    "appId": ""
}


# Inicialización de la conexión a Firebase
firebase = pyrebase.initialize_app(config)

# Obtención de una referencia a la base de datos
db = firebase.database()



while True:
    

    # Ejemplo: Leer datos de Firebase
    data = db.child("RegistroAlarmas/").get()
    print(data.val())
    dictionary = data.val()
    datos=(dict(dictionary))
    print('******')
    print(datos)
    print(type(datos))
    
    
    
    #Extraccion de compartimientos
    datoDefecto={'Hora': '"','Minuto': '"','Medicamento':'"','ampm': '"','cant':'"' }
    comp1= datos.get('Compartimiento 1', datoDefecto)
    comp2= datos.get('Compartimiento 2', datoDefecto)
    comp3= datos.get('Compartimiento 3', datoDefecto)
    comp4= datos.get('Compartimiento 4', datoDefecto)
    comp5= datos.get('Compartimiento 5', datoDefecto)
    comp6= datos.get('Compartimiento 6', datoDefecto)
    
    
    
    
    ###Ingresar demás compartimientos <-
    horaComp1=""
    minutosComp1=""
    ampmComp1=""
    horaComp2=""
    minutosComp2=""
    ampmComp2=""
    horaComp3=""
    minutosComp3=""
    ampmComp3=""
    horaComp4=""
    minutosComp4=""
    ampmComp4=""
    horaComp5=""
    minutosComp5=""
    ampmComp5=""
    horaComp6=""
    minutosComp6=""
    ampmComp6=""
    cant1=""
    cant2=""
    cant3=""
    cant4=""
    cant5=""
    cant6=""

    try:
        #Extrar horas compartimientos
        #Compartimiento 1
        hComp1 = comp1['Hora']
        mComp1= comp1['Minuto']
        ampComp1= comp1['ampm']
        #Compartimiento 2
        hComp2 = comp2['Hora']
        mComp2= comp2['Minuto']
        ampComp2= comp2['ampm']
        #Compartimiento 3
        hComp3 = comp3['Hora']
        mComp3= comp3['Minuto']
        ampComp3= comp3['ampm']
        #Compartimiento 4
        hComp4 = comp4['Hora']
        mComp4= comp4['Minuto']
        ampComp4= comp4['ampm']
        #Compartimiento 5
        hComp5 = comp5['Hora']
        mComp5= comp5['Minuto']
        ampComp5= comp5['ampm']
        #Compartimiento 6
        hComp6 = comp6['Hora']
        mComp6= comp6['Minuto']
        ampComp6= comp6['ampm']
        #Cantidades
        cant1 = comp1['cant']
        cant2 = comp2['cant']
        cant3 = comp3['cant']
        cant4 = comp4['cant']
        cant5 = comp5['cant']
        cant6 = comp6['cant']


        #Convertir a enteros

        
        def entero(valor):
            entero = valor.strip('"')
            if not entero.strip():
                salida = 'No'
            else:
                print('punto v')
                try:
                    salida = int(entero)
                except ValueError:
                    
                    salida = 'No'
            return salida
        
        ###Conversor cantidades a mostrar
        def enteroCant(valor):
            entero = valor.strip('"')
            if not entero.strip():
                salida = 0
            else:
                try:
                    salida = int(entero)
                except ValueError:
                    
                    salida = 0
                    
            return salida



        
        def horario(valor):
            salida= valor.strip('"')
            if not salida:
                return 'Noampm'
                
            
            return salida


        #Compartimiento 1
        horaComp1=entero(hComp1)
        minutosComp1=entero(mComp1)
        ampmComp1= horario(ampComp1)
        #Compartimiento 2
        horaComp2=entero(hComp2)
        minutosComp2=entero(mComp2)
        ampmComp2= horario(ampComp2)
        #Compartimiento 3
        horaComp3=entero(hComp3)
        minutosComp3=entero(mComp3)
        ampmComp3= horario(ampComp3)
        #Compartimiento 4
        horaComp4=entero(hComp4)
        minutosComp4=entero(mComp4)
        ampmComp4= horario(ampComp4)
        #Compartimiento 5
        horaComp5=entero(hComp5)
        minutosComp5=entero(mComp5)
        ampmComp5= horario(ampComp5)
        #Compartimiento 6
        horaComp6=entero(hComp6)
        minutosComp6=entero(mComp6)
        ampmComp6= horario(ampComp6)
        #Cantidades
        cantComp1 = enteroCant(cant1)
        print('control 1')
        cantComp2 = enteroCant(cant2)
        print('control 2')
        cantComp3 = enteroCant(cant3)
        print('control 3')
        cantComp4 = enteroCant(cant4)
        print('control 4')
        cantComp5 = enteroCant(cant5)
        print('control 5')
        cantComp6 = enteroCant(cant6)
        print('control 6')
        listaCantidades = [cantComp1, cantComp2, cantComp3, cantComp4, cantComp5, cantComp6]
        print(listaCantidades, "########lllllll######")


    except Exception as e:
        print('Revisión')

    #Extraer Hora del sistema
    hora_total= datetime.now().time()
    horaActualS= int(hora_total.strftime("%H"))
    horaActualS2= int(hora_total.strftime("%H"))
    if horaActualS>12:
        horaActualS= horaActualS-12
    minutoActualS = int(hora_total.strftime("%M"))
    horario=''
    if horaActualS2>=12:
        horario='PM'
    else:
        horario='AM'
    print('horario del reloj', horario)
    print(horaActualS, "hora del reloj**")
    print(minutoActualS, "minutos del reloj")


    #Extraer nombre de medicamentos
    medicamento_comp1 = comp1.get('Medicamento')
    medicamento_comp2 = comp2.get('Medicamento')
    medicamento_comp3 = comp3.get('Medicamento')
    medicamento_comp4 = comp4.get('Medicamento')
    medicamento_comp5 = comp5.get('Medicamento')
    medicamento_comp6 = comp6.get('Medicamento')
    

    #ACCIONAMIENTO SERVOS
    varControl=False
    lista=['','','','','','']

    
    
    #Condiciones Compartimiento 1
    if horaComp1==horaActualS and horario==ampmComp1:
        print('Hora cumple')
        if minutosComp1==minutoActualS:
            #Ejecuta el bot con la notificación
            notifRecordatorio(horaComp1,minutosComp1,ampmComp1,'Compartimiento 1',medicamento_comp1)
            recordatorio_alarma()
            varControl=True
            lista[0]=1
             
            #correrServo2(17)

        

    #Condiciones Compartimiento 2
    if horaComp2==horaActualS and horario==ampmComp2:
        #print('Hora cumple')
        if minutosComp2==minutoActualS:
            #print('Ejecutando función del servo')
            #correrServo1(17)
            notifRecordatorio(horaComp2,minutosComp2,ampmComp2,'Compartimiento 2',medicamento_comp2)
            varControl = True
            lista[1]=2
    
    #Condiciones Compartimiento 3
    if horaComp3==horaActualS and horario==ampmComp3:
        #print('Hora cumple')
        if minutosComp3==minutoActualS:
            #print('Ejecutando función del servo')
            #correrServo1(17)
            #reproduccion_buzzer()
            notifRecordatorio(horaComp3,minutosComp3,ampmComp3,'Compartimiento 3',medicamento_comp3)
            varControl=True
            lista[2]=3
    
    #Condiciones Compartimiento 4
    if horaComp4==horaActualS and horario==ampmComp4:
        #print('Hora cumple')
        if minutosComp4==minutoActualS:
            #print('Ejecutando función del servo')
            #correrServo1(17)
            notifRecordatorio(horaComp4,minutosComp4,ampmComp4,'Compartimiento 4',medicamento_comp4)
            varControl=True
            lista[3]=4
        
    #Condiciones Compartimiento 5
    if horaComp5==horaActualS and horario==ampmComp5:
        print('Hora cumple')
        if minutosComp5==minutoActualS:
            print('Ejecutando función del servo')
            notifRecordatorio(horaComp5,minutosComp5,ampmComp6,'Compartimiento 5',medicamento_comp5)
            varControl=True
            lista[4]=5
            #correrServo1(17)
        
    #Condiciones Compartimiento 6
    if horaComp6==horaActualS and horario==ampmComp6:
        
        print('Hora cumple')
        if minutosComp6==minutoActualS:
            print('Ejecutando función del servo')
            #correrServo1(17)
            notifRecordatorio(horaComp6,minutosComp6,'Compartimiento 6',medicamento_comp6)
            varControl=True
            lista[5]=6
        
    #Función activadora rec facial y servos
    def Accionador(condicionFinal, lista):
        global listaCantidades
        if condicionFinal == True:
            correcto= False
            correcto = pantalla()
            if correcto==True:
                notifRetiroSi()
                print('lista')
                funServos(lista)
                #Mostrar la cantidad
                for i, elemento in enumerate(lista):
                    if isinstance(elemento, int) or isinstance(elemento, float):
                        if listaCantidades[i] > 0:
                            listaCantidades[i] -= 1
                print(listaCantidades)
                entrega_pastilla()
                #Subiendo a la base de datos:
                compartimientos = ['Compartimiento 1', 'Compartimiento 2', 'Compartimiento 3', 'Compartimiento 4', 'Compartimiento 5', 'Compartimiento 6']
                for i in range(len(compartimientos)):
                    compartimiento = compartimientos[i]
                    cantidad = listaCantidades[i]
                    data = {'cant': f'"{cantidad}"'}
                    db.child('RegistroAlarmas').child(compartimiento).update(data)
                
                ##
            else:
                notifRetiroNo()

    
    #Accionamiento servos juntos
    def funServos(valor):
        listaInterna= valor
        
        if listaInterna[0]==1:
            correrServo2(25)
            #informar bot
        
        if listaInterna[1]==2:
            correrServo1(24)
            #agregar los demas
        if listaInterna[2]==3:
            correrServo1(23)
            #agregar los demas
        if listaInterna[3]==4:
            correrServo1(27)
            #agregar los demas
        if listaInterna[4]==5:
            correrServo1(22)
            #agregar los demas
        if listaInterna[5]==6:
            correrServo1(17)
            #agregar los demas
    
    
    
    Accionador(varControl, lista)
    varControl=False
    varControl, lista= modoViaje()
    print(varControl, lista)
    Accionador(varControl, lista)
        
        
    time.sleep(60)

