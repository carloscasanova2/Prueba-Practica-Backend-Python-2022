# Prueba-Pr-ctica-Backend-Python-2022
## Desarrollo de prueba práctica backend python para Beitech SAS

**El repositorio cuenta con seis (6) archivos**

![image](https://user-images.githubusercontent.com/95709562/165093035-9658d193-a33a-49f8-80bf-a0200ea852ee.png)


El primer archivo es:
[config_database.py](https://github.com/carloscasanova2/Prueba-Pr-ctica-Backend-Python-2022/blob/084f32eb669134c499655191f7f4f2f9be1ba37c/config_database.py)

En este archivo se inicializa la base de datos que se utilizará con datos suministrados para la prueba como ejemplo, esta se realizó con SQLITE3. Se desarrolló directamente en VSCODE conectado la librería de sqlite3 junto con Python.

_**Asegurese de tener instalada la libreria sqlite3 y sus paquetes**_

Tenemos una base de datos como ejemplo:
[examples.db](https://github.com/carloscasanova2/Prueba-Pr-ctica-Backend-Python-2022/blob/9b87e59d6660bbe8c7817f749f6b65c02b9e12c7/examples.db)

Sin embargo, si se quiere hacer uso de otra, o simplemente crear una nueva, se debe realizar cambios a la ruta de acceso de ésta. 

_**la base de datos debe estar en la misma ruta o carpeta de todos los archivos**_


## Tenemos el diagrama entidad relación suministrado en la prueba:


![image](https://user-images.githubusercontent.com/95709562/165097448-e103d62b-4980-4dd7-807b-d3a144c1e285.png)


### Al diagrama anterior se le aplican algunos cambios y queda así:


![image](https://user-images.githubusercontent.com/95709562/165097378-eb6f432c-960c-4f67-86e8-cad910297121.png)



### Se crean las tablas con los cambios hechos en el diagrama entidad-relación

![image](https://user-images.githubusercontent.com/95709562/165100530-c4057d8e-6bff-40fe-afd7-45d28200444c.png)

Posterior a esto, se le ingresan los valores a las tablas.


## los siguientes archivos son: 

[rest.py](https://github.com/carloscasanova2/Prueba-Pr-ctica-Backend-Python-2022/blob/9b87e59d6660bbe8c7817f749f6b65c02b9e12c7/rest.py)

### rest.py contiene el código desarrollado para el backend que contiene los microservicios


[peticiones.py](https://github.com/carloscasanova2/Prueba-Pr-ctica-Backend-Python-2022/blob/9b87e59d6660bbe8c7817f749f6b65c02b9e12c7/peticiones.py)

### peticiones.py es un archivo para realizar peticiones y hacer test de los microservicios


[ilustraciones.pdf](https://github.com/carloscasanova2/Prueba-Pr-ctica-Backend-Python-2022/blob/35e983ec4d23ef9bccbd45c31daf08c4874c63bd/Ilustraciones.pdf)

### Ilustraciones.pdf corresponde a la documentación detallada de los métodos del API REST 


## El ultimo archivo es: 

[index.html](https://github.com/carloscasanova2/Prueba-Pr-ctica-Backend-Python-2022/blob/35e983ec4d23ef9bccbd45c31daf08c4874c63bd/index.html)

### Al igual que peticiones.py, index.html permite validar el funcionamiento de los microservicios y a su vez renderizar los datos obtenidos desde el backend en el formato que se solicita en la prueba,

### La interfaz se divide en dos partes, la primera es la creación de la orden para el cliente. Esta se visualiza en la siguiente imagen:

![image](https://user-images.githubusercontent.com/95709562/165102313-213e20df-e009-4c26-a5a2-c107b519f191.png)


La segunda es la visualización detallada de las ordenes consultadas por cliente y rango de fechas:

![image](https://user-images.githubusercontent.com/95709562/165102442-8910056b-c070-4072-9750-fea919ff8d78.png)
















