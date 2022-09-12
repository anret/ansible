#!/usr/bin/python

import mysql.connector

config = {
  'user': 'autoscript',
  'password': 'autopassword',
  'host': '10.200.200.3',
  'database': 'inventory',
  'raise_on_warnings': True
}



cnx = mysql.connector.connect(**config)

cursor = cnx.cursor(buffered=True)

query = ('SELECT Hostname, IP_Address FROM hosts')

cursor.execute(query)

resp=[(str(elem[0]),str(elem[1])) for elem in cursor.fetchall()]

print(resp)

print(resp[0][0], resp[0][1])
print(type(resp[0][0]), type(resp[0][1]))


cursor.close()
cnx.close()

