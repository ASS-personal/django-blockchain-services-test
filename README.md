# Aplicación de consulta de datos en base de datos blockchain.

En esta aplicación se va a poder consultar los datos registrado de compras y ventas en órdenes L3 registrados en la base de datos https://api.blockchain.com/v3/

El dividendo empleado es en `dólares americanos ('BTC-USD')`.

# Estructura de ficheros

La aplicación esta realizada bajo en framework Django empleando las libreriás rest-framework (API), Pandas (algorítmia), drf-yasg (Swagger), y requests (HTTP service).

Todos los ficheros relacionados con la aplicación se localizan en la carpeta `blockchain`. En el fichero `admin.py` se localiza toda la configuración del panel de administración. En el fichero `models.py` se encuentran los modelos de datos sobre los que se va a sostener la base de datos. En el fichero `urls.py` se enceuntran los nombres de los servicios. Finalmente, en el fichero `views.py` encontramos la parte del controlador de los servicios. En este último se localiza toda la lógica y algritmia asociada a cada servicio.

La clase `PurchaseView` contiene la algoritmia aplicada para el servicio `statistics/purchase`. La clase `SalesView` contiene la algoritmia aplicada para el servicio `statistics/sales`. Finalmente, la clase `GeneralView` contiene la algoritmia aplicada para el servicio `statistics`.

# Ejecución

Para poder enejutar la palicación, necesita disponer de `python3.9`, `pip` y `virtualenv` instalados.

En el mismo directorio donde se encuentra la aplicación, debemos ubicar el entorno que se va a emplear para su ejecución. Para ello emplearemos la sentencia:
```bash
virtualenv -p python3.9 .venv (en Linux)
py -m virtualenv .venv (en Windows)
```

Una vez instalado el entorno, lo cargamos (`source .venv/bin/activate` en Linux ó `.venv/Scripts/Activate.ps1` en Windows) y procedemos de la siguiente manera:

1. Intalación de dependencias `pip install -r requirements.txt`
2. Carga de datos blockchain `python manage.py update_blockchain_data` (1min aprox.)
3. iniciamo el servidor `python manage.py runserver`
4. Realizamos la prueba consultando la URL [http://localhost:8000/admin/](http://localhost:8000/admin/). Se tiene que ver el login de acceso al panel de administración de la aplicación.

# Manejo de la API

Con el fin de hacerlo sencillo, se ha incluido un panel para hacer las consultas y, así, no tener que hacerlas por el navegador o una aplicación API-REST.

El acceso a este panel se realiza por la URL `http://localhost:8000/swagger`

# Servicios

`statistics`: Estadíticas generales.

`statistics/purchase`: Estadíticas de compras.

`statistics/sales`: Estadísticas de ventas.

# Consulta de datos desde backoffice

Hay un panel de administración disponible para ver los datos (en bruto) cargados en la aplicación. El usuario de login es `test` y el password `1234567.` (punto final incluido).