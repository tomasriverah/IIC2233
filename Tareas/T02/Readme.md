# Tarea 2: DCCampo :seedling: :corn:	

## General

Para esta tarea logré implementar casi todas las cosas pedidas, detallaré más abajo que se implementó  y que no. El juego funciona bien y en mi testeo no se cayó. Mi tarea está compuesta por 5 archivos ```main.py``` , ```front_end.py```, ```back_end.py```, ```parametros_generales.py``` y ```extras.py```. El archivo a correr para ejecutar la tarea es ```main.py```. A continuación explicaré más en detalle de que se trata cada uno.

## Implementación

Iré repasando los puntos en el orden que aparecen en el enunciado.

### Flujo de Juego

Se muestra la ventana de inicio con todos los elementos correspondientes, si se ingresa un mapa existente el juego comienza y se cierra la ventana, de lo contrario se muestra un mensaje de error y se pide otro nombre.

Se carga el mapa, los elementos y el personaje. Se comienza con el inventario vacío. A medida que se adquieren elementos estos se muestran en el inventario, si estos se agotan desaparecen del inventario. 

### Entidades

Personaje: Este se mueve mediante las teclas de w, a, s, d el personaje se mueve de manera fluida con sprites y avanza 10 pixeles por movimiento.

Cultivos: Los cultivos crecen con un reloj propio que corre en el mismo tiempo que el reloj principal. Estos crecen como se espera. Al alcanzar su fase final entregan frutos. En el caso de la alcachofa está implementado correctamente pero no lo alcance a realizar para el choclo.

Herramientas: La azada está implementada pero los espacios se pueden arar independiente si está equipada o no. Los arboles se pueden talar solo si el hacha está equipada. Hay un bug en el que los arboles solo pueden ser talados si "spawnearon" con el hacha implentada en el inventario. La tala se realiza mediante doble click y arar se realiza mediante click en un espacio váldio.

Aparición espontanea: Arboles y oro aparecen al comenzar un nuevo día solo aparecen en espacios dispinobiles.

Recursos: Están implementados correctamente excepto por el hecho de que no alcancé a implementar el choclo ni el hecho de que tanto el oro como la leña no tienen tiempo de desaparición.

## Interfaz

El juego está modelado mediante front y back end con comunicación mediante señales para eventos. 

El reloj interno del juego corre de modo que medio segundo real es 1 minuto en el juego y el día tiene 24 hrs.

Ventanas: La ventana de inicio funciona como lo esperado. La ventana principal funciona como se espera excepto por el boton de pausa el cual no está implementado y el boton de cerrar ventana el cual solo esconde la ventana pero no finaliza la ejecución del programa. La ventana de tienda tambien funciona como se espera.

##  Interacción del usuario

Drag & Drop implementado para el cultivo de semillas.

Es posible talar arboles mediante doble click y arar espacios mediante click.

La ventana tienda permite comprar y vender objetos al hacer click en los botones respectivos.

Cuando el personaje se para sobre la casa comienza un nuevo día y "spawnean" los objetos que deben.

El personaje no choca con los arboles, con las piedras no funciona muy bien y con los bordes está implementado correctamente.

## Funcionalidades Externas

Al presionar las teclas correspondientes en sucesión se ejecutan las funcionalidades esperadas.

Pausa no implementada.

## Bonus

No implementados.

# Archivos

```main.py```: Es el archvio sirve de y ejecución para el back y front.

```front_end.py```: Contiene todos los elementos graficos junto con algunos metodos para el funcionamiento del juego.

```back_end.py```: Contiene los elementos logicos y las operaciones necesarias para que el juego funcione.

```parametros_generales.py``` Contiene parametros relevantes para el juego junto con diccionarios que contienen rutas e información 
relevante.

```extras.py```: Contiene funciones y clases que son utilizadas para el funcionamiento del juego



# Referencias de codigo externo

### Drag & Drop

Se implementaron las clases ```DraggableLabel```y ```DroppableLabel``` para ser utilizadas.
Lineas 114 a 173 en ```extras.py```

Link: https://stackoverflow.com/questions/50232639/drag-and-drop-qlabels-with-pyqt5

### Funcion de redondeo

Se implementó la funcion ```roundup``` para redondear la posicion del personaje y usarla al calcular si en su posición recoge o no un elemento.
Lineas 176 a 180 en ```extras.py```

Link: https://stackoverflow.com/questions/34001496/how-do-i-round-up-a-number-to-the-nearest-10-in-python-3-4-0
