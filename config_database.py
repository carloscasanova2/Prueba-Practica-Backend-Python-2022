import sqlite3
#realizamos conexión con BBDD, si no existe crea el archivo .db
con = sqlite3.connect('examples.db')

#permite realizar las sentencias sql con la BBDD
cur = con.cursor()

#Creamos la tabla 
#create table: nombre
#parentesis-columnas y al lado el tipo de columna
cur.execute('''CREATE TABLE modif_order_detail 
               (od_id INTEGER PRIMARY KEY, od_quantity int, o_order_id int, p_product_id int)''')


cur.execute('''CREATE TABLE modif_product
               (p_product_id INTEGER PRIMARY KEY, p_product_name text, p_product_price int)''')


cur.execute('''CREATE TABLE modif_order
               (o_order_id INTEGER PRIMARY KEY, o_delivery_address text, o_date text , o_customer_id int)''')
    

cur.execute('''CREATE TABLE modif_customer
               (c_customer_id INTEGER PRIMARY KEY, c_customer_name text, c_customer_email text)''')


cur.execute('''CREATE TABLE modif_customer_product 
               (cp_id INTEGER PRIMARY KEY, cp_customer_id int, cp_product_id int)''')



#insertamos los datos a las tablas
#primero se insertan los valores de los clientes 
cur.execute("INSERT INTO modif_customer VALUES (NULL,'Manny Bharma','manny@bharma.com')")
cur.execute("INSERT INTO modif_customer VALUES (NULL,'Alan Briggs','alan@briggs.com')")
cur.execute("INSERT INTO modif_customer VALUES (NULL,'Mike Simm','mike@simm.com')")


#segundo insertamos los valores de producto
cur.execute("INSERT INTO modif_product VALUES (NULL,'product A',25)")

cur.execute("INSERT INTO modif_product VALUES (NULL,'product B',35)")

cur.execute("INSERT INTO modif_product VALUES (NULL,'product C',45)")

cur.execute("INSERT INTO modif_product VALUES (NULL,'product D',55)")


#tercero insertamos los valores de producto del cliente
#cliente 1
cur.execute("INSERT INTO modif_customer_product VALUES (NULL,1,1)")
cur.execute("INSERT INTO modif_customer_product VALUES (NULL,1,2)")
cur.execute("INSERT INTO modif_customer_product VALUES (NULL,1,3)")

#cliente 2
cur.execute("INSERT INTO modif_customer_product VALUES (NULL,2,2)")

#cliente 3
cur.execute("INSERT INTO modif_customer_product VALUES (NULL,3,1)")
cur.execute("INSERT INTO modif_customer_product VALUES (NULL,3,4)")

con.commit()
con.close()
#cuarto insertamos los valores de las ordenes
# cur.execute("INSERT INTO modif_order VALUES (NULL,'carrera 47 #64-26','02-08-2022',1)")
# cur.execute("INSERT INTO modif_order VALUES (NULL,'carrera 47 #64-26','02-08-2022',2)")
# cur.execute("INSERT INTO modif_order VALUES (NULL,'carrera 47 #64-26','02-08-2022',3)")


#quinto insertamos los valores de las ordenes detalladas
#primera orden cliente 1 detallada
# cur.execute("INSERT INTO modif_order_detail VALUES (NULL,1,1,1)")
# cur.execute("INSERT INTO modif_order_detail VALUES (NULL,1,1,2)")
# cur.execute("INSERT INTO modif_order_detail VALUES (NULL,1,1,3)")

#segunda orden cliente 2 detallada
# cur.execute("INSERT INTO modif_order_detail VALUES (NULL,1,2,2)")

#tercera orden cliente 3 detallada
# cur.execute("INSERT INTO modif_order_detail VALUES (NULL,1,3,1)")
# cur.execute("INSERT INTO modif_order_detail VALUES (NULL,1,3,4)")  
