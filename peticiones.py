import requests
import json
from datetime import datetime


now = datetime.now()
date = datetime.strftime(now, "%d-%m-%Y")

'''
PRIMERA PETICIÓN: Crear una orden. Este microservicio valida la cantidad de productos disponibles por cliente
Además valida si el cliente se ha creado, luego de las validaciones se registra una nueva orden y se añaden los productos de esta,
como respuesta retorna un json que indica si hubo un error, muestra el error que ocurrió y en caso de no haber error, retorna el id
de la ultima orden registrada.
'''

new_order = {

    'date':'23-4-2022',
    'address':'cra 34 45',
    'id_customer':1,
    'products':[
        {
            'id':1,
            'quantity':1
        },
        {
            'id':2,
            'quantity':1
        },
        {
            'id':3,
            'quantity':1
        }
    ],
}
str_new_order =json.dumps(new_order)
byteContent = bytearray(str_new_order, 'utf-8')
len(byteContent)

hdrs = {
    'Content-type': 'application/json',
    'Content-length':str(len(byteContent))
}
r = requests.post(url = 'http://127.0.0.1:5000//create_order', data=byteContent, headers=hdrs)
print(r.text)

#___________________________________________________________________________________________________________#
'''
SEGUNDA PETICIÓN: Listar ordenes por fecha y cliente 
'''

get_list_order = {

    'date1':'07-05-2022',
    'date2':'22-05-2022',
    'id_customer':1
}

str_get_list_order =json.dumps(get_list_order)
byteContent = bytearray(str_get_list_order, 'utf-8')
len(byteContent)

hdrs = {
    'Content-type': 'application/json',
    'Content-length':str(len(byteContent))
}
r = requests.post(url = 'http://127.0.0.1:5000//get_order_by_date', data=byteContent, headers=hdrs)
print(r.text)


ft = datetime.strftime(datetime.strptime('23-4-2022', '%d-%m-%Y'),'%d-%m-%Y') 
ft
import sqlite3
import json

database_name = r'examples.db'
con = sqlite3.connect(database_name)
cur = con.cursor()
lista_order= cur.execute('SELECT * FROM modif_order').fetchall()
lista_order
con.close()