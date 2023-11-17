import pyrebase
#from servo002 import *
#from servo003 import *

#Conf Firebase
def modoViaje():

  config = {
    "apiKey": "AIzaSyCL_d0yPOanoQgUpmFZz4iKulrsd7K9xf4",
    "authDomain": "modo-viaje.firebaseapp.com",
    "databaseURL": "https://modo-viaje-default-rtdb.firebaseio.com",
    "projectId": "modo-viaje",
    "storageBucket": "modo-viaje.appspot.com",
    "messagingSenderId": "265547756375",
    "appId": "1:265547756375:web:5dd17f2bf3c217f6a58412"
  };

  #Inicializacion de la conexión firebase
  firebase = pyrebase.initialize_app(config)
  db = firebase.database()


  

  #Ejemplo: Leer datos de Firebase
  data = db.child("ModoViaje/").get()
  print(data.val())
  #print(type(data))
  dictionary = data.val()
  #print(dictionary)
  #print(type(dictionary))
  datos=(dict(dictionary))
  print('******')
  print(datos)
  print(type(datos))

  #Editar datos
  #firebase.put('DispensadorDeMedicinas/Compartimiento 1:','Valor','no')
  data = {'Valor': 'no'}
  db.child('ModoViaje').child('Compartimiento 1:').update(data)
  data = {'Valor': 'no'}
  db.child('ModoViaje').child('Compartimiento 2:').update(data)
  data = {'Valor': 'no'}
  db.child('ModoViaje').child('Compartimiento 3:').update(data)
  data = {'Valor': 'no'}
  db.child('ModoViaje').child('Compartimiento 4:').update(data)
  data = {'Valor': 'no'}
  db.child('ModoViaje').child('Compartimiento 5:').update(data)
  data = {'Valor': 'no'}
  db.child('ModoViaje').child('Compartimiento 6:').update(data)

  datoDefecto={'Compartimiento': '"','Valor': '"'}
  comp1= datos.get('Compartimiento 1:', datoDefecto)
  comp2= datos.get('Compartimiento 2:', datoDefecto)
  comp3= datos.get('Compartimiento 3:', datoDefecto)
  comp4= datos.get('Compartimiento 4:', datoDefecto)
  comp5= datos.get('Compartimiento 5:', datoDefecto)
  comp6= datos.get('Compartimiento 6:', datoDefecto)

  print(comp1)
  print(comp2)
  print(comp3)
  print(comp4)
  print(comp5)
  print(comp6)

  condicionModoViaje = False

  valComp1 = comp1['Valor']
  valComp2 = comp2['Valor']
  valComp3 = comp3['Valor']
  valComp4 = comp4['Valor']
  valComp5 = comp5['Valor']
  valComp6 = comp6['Valor']

  print(valComp1)
  print(valComp2)
  print(valComp3)
  print(valComp4)
  print(valComp5)
  print(valComp6)

  listaViaje=['','','','','','']
  listaViaje[0]=valComp1
  listaViaje[1]=valComp2
  listaViaje[2]=valComp3
  listaViaje[3]=valComp4
  listaViaje[4]=valComp5
  listaViaje[5]=valComp6

  if listaViaje[0]=='"si"':
    listaViaje[0]=1
  if listaViaje[1]=='"si"':
    listaViaje[1]=2
  if listaViaje[2]=='"si"':
    listaViaje[2]=3
  if listaViaje[3]=='"si"':
    listaViaje[3]=4
  if listaViaje[4]=='"si"':
    listaViaje[4]=5
  if listaViaje[5]=='"si"':
    listaViaje[5]=6
  
  print(listaViaje, '######################')

  #def modoViaje():
  #modoViaje()
  if valComp1=='"si"' or valComp2=='"si"' or valComp3=='"si"' or valComp4=='"si"' or valComp5=='"si"' or valComp6=='"si"':
    return True, listaViaje
  else: 
    return False, listaViaje





varia= modoViaje()
print(varia)





