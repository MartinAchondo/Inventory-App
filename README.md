# Gestor-Dominga
<p float="left">
<img src="https://img.shields.io/badge/version-1.2.1-success" >
<img src="https://img.shields.io/badge/status-stable-success" >
<img src="https://img.shields.io/badge/size-260MB-informational" >
<img src="https://img.shields.io/badge/front%20end-javascript-informational">
<img src="https://img.shields.io/badge/back%20end-python-informational">
<img src="https://img.shields.io/badge/open%20issue-0%25-%231FDEA4">
</p>

<p align="justify"> Una aplicación para gestionar el inventario y las ventas de la tienda de ropa Dominga & Co. Para esto, se diseño una interfaz que permite mostrar la información en la base con tablas y gráfcos, y además, comunicarse para añadir, editar o borrar registros en la base de datos.</p>

<p align="justify">La aplicación está diseñada en python como back end y una conexión mediante el módulo eel para usar chromium y crear una ventana con electron js. Esto permite que se utilize el máximo potenncial tanto de python como nodejs para todas las operaciones en el back.  Dado esto, todo el front end queda esta escrito en javascript, html y css permitiendo así se permita crear una interfaz bastante amigable con las herramientas web.</p>

<p align="justify">La ventana está hecha con electron js, de esta manera no es necesario tener un navegador instalado para correr el programa. Para una visualización amigable, se usaron las librerías de bootstrap y jquery. Con esto se creó el layaout. Además, la tabla se hizo con las datatables de bootstrap. Los gráficos se crearon con la librería de chart js. </p>

<p align="justify">El motor principal de la aplicación es python con el módulo de eel. Este se usó para conectar todos los códigos del back end con el front end. Además, todos los registros ingresados en la app se guardan en una base de datos usando el módulo de sqlite. El programa tiene la opción de subir la base de datos mediante el Google Drive API. De esta manera, se puede usar el programa desde distintos computadores.</p>

<p align="justify">En adición, el programa tiene la opción de exportar los datos a planillas excel. Para esto, se le añaden macros con VBA a las planillas para que al momento de abrir la planilla exportada, los datos se visualicen en una tabla de buena manera.</p>

<p align="justify">En la base de datos en SQLite se tiene almacenado los códigos existentes, sus identificadores y la nomenclatura de los códigos. Además, se tienen tablas con el inventario completo, las ventas y el historial. De esta manera, toda la información útil referente a la tienda esta almacenada y puede ser utilizada.</p>

<h2>Home</h2>
<p>En el inicio se tiene un análisis rápido de las ventas y el inventario.</p>
<img src=.github/f1.png width=100%>

<h2>Ingresar Prenda Nueva</h2>
<p>Se puede ingresar una prenda nueva al inventario. El programa creará un identificador único para la prenda.</p>
<img src=.github/f2.png width=100%>

<h2>Ingresar Prenda Existente</h2>
<p>Se puede ingresar un código ya creado. Se busca por código y descripción.</p>
<img src=.github/f3.png width=100%>

<h2>Ver Inventario</h2>
<p>Se puede revisar, filtrar y ordenar la información del inventario</p>
<img src=.github/f4.png width=100%>


<h2>Ver Código</h2>
<p>Se puede ver toda la información referida a un código, su foto y sus ventas.</p>
<img src=.github/f5.png width=100%>

<h2>Enviar a Tienda</h2>
<p>Ventana para enviar prendas a tienda.</p>
<img src=.github/f6.png width=100%>

<h2>Ingresar Venta</h2>
<p>Se ingresan las ventas.</p>
<img src=.github/f7.png width=100%>

<h2>Ventas</h2>
<p>Se puede ver, filtrar y ordenar toda la información de las ventas.</p>
<img src=.github/f8.png width=100%>

<h2>Historial</h2>
<p>Se guarda un análisis completo del historial del programa.</p>
<img src=.github/f9.png width=100%>

<h2>Análisis de Inventario</h2>
<p>Se realiza un análisis completo del inventario.</p>
<img src=.github/f10.png width=100%>

<h2>Análisis Ventas</h2>
<p>Se realiza un análisis completo de las ventas por periodo.</p>
<img src=.github/f11.png width=100%>

<h2>Cargar Base</h2>
<p>Para ser utilizado en varios PCs, la base se puede subir a drive. En la esquina derecha se indicará cuando hay que subirla o descargarla. Esta tarea se puede automatizar.</p>
<img src=.github/f12.png width=100%>

<h2>Planilla Inventrio</h2>
<p>Se puede exportar una planilla con la información completa del inventario.</p>
<img src=.github/f13.png width=100%>
<p>Se crean tablas dinámicas y gráficos.</p>
<img src=.github/f14.png width=100%>

<h2>Planilla Códigos</h2>
<p>Se puede exportar planilla con las fotos asociadas a cada código.</p>
<img src=.github/f15.png width=100%>

<h2>Planilla Ventas</h2>
<p>Se puede exportar planilla con la información de las ventas.</p>
<img src=.github/f16.png width=100%>

<h2>Querys</h2>
<p>Para una mayor libertad, se pueden realizar peticiones propias a la base de datos asociada.</p>
<img src=.github/f17.png width=100%>
