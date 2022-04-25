#creación de APIRest con funciones de escritura, lectura 
from datetime import datetime
from flask import Flask, request
from flask_cors import CORS
import sqlite3
import json

database_name = r"C:\Users\capenaloza\Documents\Prueba\examples.db"

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
#primera petición
@app.route("/create_order",methods=['POST'])
def create_order():
    print(str(request.data))
    if request.method == 'POST':
        response = {
            "Error":False,
            "Mensaje":"",
            "id": None
        }
        print(request.json)
        data= json.loads(request.data)
         
        if not data['date']:
            response["Mensaje"] = 'Fecha no suministrada'
            response["Error"] = True
            return json.dumps(response)
        
        if not data['address']:
            response["Mensaje"] = 'Direccion no suministrada'
            response["Error"] = True
            return json.dumps(response)

        print(data['id_customer'])
        # validar que el id customer sea valido
        if not validate_customer(data['id_customer']):
            response["Mensaje"]= "No existe el customer, no está registrado"
            response["Error"]= True
            return json.dumps(response)
        
        # validar que los productos sean los que el cliente puede comprar
        selected_products_list_id =[sp['id'] for sp in data['products']]
        if not validate_products(data['id_customer'], selected_products_list_id):
            response["Mensaje"]= "Productos no permitidos"
            response["Error"]= True
            return json.dumps(response)
        
        #validar cantidad de productos 
        quantity = sum([int(sp['quantity']) for sp in data['products']]) #nos dará la cantidad de productos que se tiene
        if quantity >5:
            response["Mensaje"]= "Excede la cantidad de productos"
            response["Error"]= True
            return json.dumps(response)
        try:

            con = sqlite3.connect(database_name)
            cur = con.cursor()
            date = datetime.strftime(datetime.strptime(data['date'], '%d-%m-%Y'),'%d-%m-%Y')
            cur.execute(f"INSERT INTO modif_order VALUES (NULL,'{data['address']}','{date}',{data['id_customer']})")
            lastrowid = cur.lastrowid
            
            con.commit()
            con.close()
            if not add_order_detail(lastrowid, data['products']):
                response["Mensaje"]= "Orden creada sin detalles"
                response["Error"]= True
                response['id']=lastrowid
                
                return json.dumps(response)
            else:
                response["Mensaje"]= "Orden creada...completado"
                response["Error"]= False
                response['id']=lastrowid
                
                return json.dumps(response)
        except:
            response["Mensaje"]= "Error al conectar base de datos"
            response["Error"]= True
            return json.dumps(response)
    else:
        return "get request"

def validate_customer(id_customer):
    
    con = sqlite3.connect(database_name)
    cur = con.cursor()

    customer = cur.execute(f'SELECT * FROM modif_customer WHERE c_customer_id == {id_customer}').fetchone() 
    print('customer:', customer)
    con.commit()
    con.close()

    if customer: 
        
        return True

    return False   

def validate_products(id_customer, selected_products_list_id): 
    con = sqlite3.connect(database_name)
    cur= con.cursor()
    available_products= [ap[0] for ap in cur.execute(f'SELECT cp_product_id FROM modif_customer_product WHERE cp_customer_id == {id_customer}').fetchall()]
    print("esto es available", available_products)
    print("esto es select_list", selected_products_list_id)
    #vamos a recorrer toda la lista de productos seleccionados, si no se encuentra el producto porque nos da cero, nos dará un False. 
    for sp in selected_products_list_id: 
        if available_products.count(sp)==0: #count contará cuantas veces esta el id de productos disponibles en la lista
            return False
    con.commit()
    con.close()
    return True

#funcion para añadir detalles a la orden
def add_order_detail(order_id, products_detail):
    con = sqlite3.connect(database_name)
    cur= con.cursor()
    pd =[[p['quantity'], p['id']] for p in products_detail]
    try:
        for p in pd:

            cur.execute(f"INSERT INTO modif_order_detail VALUES (NULL,{p[0]},{order_id},{p[1]})")
    except:
        return False
    con.commit()
    con.close()
    return True 

#_______________________________________________________________________________________________________________#


#segunda petición

@app.route('/get_order_by_date',methods=['POST'])
def get_order_by_date():

    data= json.loads(request.data)
    res={
        "orders":[],
        "Mensaje":"",
        "Error": True

    }
    if not data['id_customer']:
        res["Mensaje"] ="Id de customer no suministrado"
        return json.dumps(res)
    if not data['date1']:
        res["Mensaje"] ="Fecha inicial no suministrada"
        return json.dumps(res)
    #consultar tabla de modif_order y filtrar por fechas - nos traemos todas las ordenes
    con = sqlite3.connect(database_name)
    cur= con.cursor()
    
    try:  
        date2 = data['date2'] if data['date2'] else datetime.strftime(datetime.now(), "%d-%m-%Y")
        #WHERE mo.o_date BETWEEN '{data['date1']}' AND '{date2}'
        lista_order= cur.execute(f'''
        SELECT mo.o_order_id, mo.o_delivery_address, mo.o_date, mp.p_product_id, mp.p_product_name, mp.p_product_price, mod.od_quantity
        FROM modif_order AS mo
        INNER JOIN modif_order_detail AS mod ON mo.o_order_id = mod.o_order_id
        INNER JOIN modif_product AS mp ON mod.p_product_id = mp.p_product_id
        WHERE mo.o_date BETWEEN '{data['date1']}' AND '{date2}'
        AND MO.o_customer_id = {data['id_customer']}
        ''').fetchall()

        orders=[]

        id_orders = list(set([i[0] for i in lista_order]))
        id_orders

        for ido in id_orders:
            total =0
            date=""
            address =""
            products =[]
            for lo in lista_order:
                if ido == lo[0]:
                    total = total + int(lo[5])*int(lo[6])
                    date= lo[2]
                    address = lo[1]
                    p ={
                        "product":lo[4],
                        "id":lo[3],
                        "quantity":lo[6],
                        "unit_price":lo[5]
                    }
                    products.append(p)

            current_order = {

                "id_order":ido,
                "date":date,
                "address":address,
                "total":total,
                "products":products


            }
            orders.append(current_order)
        
        res["orders"]=orders
        res["Mensaje"]="Solicitud completada con exito"
        res["Error"]=False
    except:       
        res["Mensaje"]="Error al consultar base de datos"
        res["Error"]=True

    return json.dumps(res)


if __name__ =='__main__':
    app.run(debug=True, port=5000)