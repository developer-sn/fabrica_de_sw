import mysql.connector

def connectionBD():
  mydb = mysql.connector.connect(
        host="developerservice2024.mysql.pythonanywhere-services.com",
        user="developerservice",
        password="Root.2024",
        database="developerservice$default"
  )

  if mydb:
    print("Conexión exitosa")
  else:
    print("Error en la conexión a la BD")
  return mydb

