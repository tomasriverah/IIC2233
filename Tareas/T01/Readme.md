# Tarea 1: Inital P 🚗🚗 🏁🏁

## Importante
* Para la entrega de mi tarea el modulo Menus.py es una versión de hace dos semanas y no la de la entrega que correspondía, me equivoqué al actualizar el repositorio ya que cambié el nombre de Menus.py a menus.py y cuando actualizaba el repositorio en git el nuevo archivo no se actualizaba. Recién me percaté de esto el domingo a las 21 cuando comencé a escribir este readme, de todas maneras subí el archivo  que corresponde en ese instante. El programa no correrá con el modulo antiguo. Si se quisiera correr hay que usar el modulo nuevo, pese a esto entiendo que para corregir la tarea probablemente solo se pueda juzgar lo que está incluido en el último commit antes de la fecha de entrega.

## General 
### (Disclaimer todo es considerando menus.py nuevo 😢)

* El programa está compuesto por 6 archivos: main.py, funciones.py, menus.py, objetos.py, paramatros.py y compra_vehículos.csv sumado a los archivos .csv que fueron proporcionados con el enunciado. El archivo a corrrer para jugar es main.py.

* El juego comienza bien, se puede elegir entre una partida nueva y cargar partida, en ambos casos se recibe un nombre de usuario que en mi testeo es a prueba de errores. Continua con el flujo del juego donde se carga el menu principal y se puede elegir entre comprar un vehículo, inciar una carrera, guardar partida y salir.
  
* Para la compra de vehículos se usa el archvio compra_vehículos.csv, este usa un formato similar a los csv que fueron proporcionados y al cargarse permite al jugador comprar uno de los vehículos que se encuentran en el. El jugador debe elegir uno de los vehiculos y nombrarlo, si no tiene dinero suficiente le dice y le permite otra elección.
  
* Nueva carrera, en esta elección se pide al usuario elegir una pista, elegir uno de sus vehículos y posteriormente comenzar la carrera, al comenzar la carrera automaticamente se corre la primera vuelta por lo que no se puede entrar a pits. Posteriormente se elige entrar a pits al fin de cada vuelta por lo que aunque se decida entrar a pits aun pudes tener accidente en la vuelta antes que puedas llegar al "pit lane". Si todos los competidores son eliminados aun debes completar la carrera para ganar. Si eres eliminado la carrera termina.

* Guardar Partida, automaticamente guarda la partida del jugador reescrbiendo la entrada correspondiente a este en el archivo .csv, y si este es un nuevo jugador crea una nueva entrada.


## Ejecución
El módulo principal de la tarea a ejecutar es  ```main.py```.
El archivo compra_vehículos.csv se puede modificar manualmente y el juego funciona siempre y cuanto se respete el formato original.


## Librerías
### Librerías externas utilizadas

1. ```copy```: ```deepcopy()```
2. ```random```: ```random()```, ```choice()```, ```random()```, ```randint()``` 
3. ```math``` : ```floor()``` 
### Modulos Propios


1. ```objetos```: contiene a ```Juego```, ```Vehiculo```(y sus subclases), ```Piloto```, ```Contrincante```, ```Pista``` , ```Carrera```.
2. ```menus```: contiene a  ```Menu```, ```MenuSesion```, ```MenuPrincipal```, ```MenuPreparación```, ```MenuCarrera```, ```MenuPits```
3. ```juego```: contiene las funcionalidades básicas del juego, como ```cargar_partida_nueva()```, ```cargar_partida_existeste()```, etc.
4. ```parametros```: incluye los parametros del juego.
5. ```funciones```: Contiene funciones que se utilizan en todo el programa, desde el manejo de archivos hasta las formulas.
6. ```main```: llama de manera estructurada a las clases y metodos para tener un juego coherente.


## Consideraciones


* Para saber si ocurría un accidente o no, determiné que si la probabilidad de accidentes de acuerdo a la fórmula es menor a una instancia de ```random.random()``` el accidente ocurría.

* Al elegir el nombre de un auto nuevo igual al de un auto existente el juego podría caerse.

* Comprendo si no es posible utilizar el archivo menus.py correcto para correr el juego yo debi revisar mis push en git y ver que efectivamente todos los archivos se actualizaran en mi repositorio. Fui muy ~~estúpido~~ volado al no darme cuenta antes para haber alcanzado a la entrega atrasad por último 😭 😭. 
