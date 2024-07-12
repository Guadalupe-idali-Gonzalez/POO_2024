import mysql.connector 

#crear la conexion con la bd 
conexion=mysql.connector.connect(
    host='localhost'
    user=='root'
    password=



 #verificar la conexion 
  if conexion.is_connected():
      print("se crea  la conexion con exito")



    #crear otro objeto para ejecutar las instrucciones 
   micurosr=conexion.cursor()

   #crear la BD desde python 
    sql="create database bd_python"
    micursor.execute(sql)

  #verificar que se se creo la BD
   if micursor:
  print("se creo la BD exitosamente ")

 #mostrar las BD que existen en mi servidor de MySQL 
   micursor.execute("show database")

   for x in micursor:
       print(x)

        