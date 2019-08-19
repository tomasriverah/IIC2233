# Tarea 0: LegoSweeper

## General
* El juego carga y funciona todo lo pedido en el enunciado en general. Las partidas cargan de buena manera, y se guardan sin problemas. En mi testeo no tuve problemas con el desarrollo del juego en si.

* Respecto a guardar y cargar archivos, cuando se carga una partida el juego toma en cuenta que el nombre del usuario es el que se introdujo para cargar la partida, en retrospectiva quizás debí implentar la opción de que el usuario que carga una partida pueda elegir otro nombre distinto al de carga del archivo. 

## Formato, guarda y carga de archivos.
* El juego guarda las partidas en un archivo ```.txt``` con el nombre que el jugador introdujo al empezar esta. La partida se guarda dentro de una carpeta /partidas, esta carpeta se crea automaticamente si es que no existe en la dirección desde donde se ejecuta el programa.
* Las partidas se guardan con el siguiente formato, ``` [tablero_de_juego];[tablero_oculto]``` donde tablero de juego es el que se muestra en consola e interactua el jugador y tablero oculto es el tablero que contiene los legos y la cantidad de legos adyacentes a cada cuadrado.
* Para guardar los puntajes estos se guardan en un archivo ```.txt```  Con el formato ```nombre: puntaje``` y el siguiente jugador se guarda en la linea siguiente. Los jugadores estan ordenados por orden de partida jugada y no por su puntaje.
* Al momento de cargar el ranking de puntaje el programa lee el archivo ```puntaje.txt``` y ordena a los 10 primeros, si es que hay menos jugadores ordena solamente a estos.


## Ejecución
El archivo de la tarea es  ```main.py```. Al ejecutarse se abrira el menú de inicio el cual permite al jugador elegir como continuar.

## Librerías
La lista de librerías externas que utilicé fueron las siguientes sumadas a ```tablero.py``` y ```parametros.py``` que fueron entregados:

1. ```math```
2. ```random```
3. ```ast```
4. ```copy```
5. ```os``` 
-------

## Referencias de código externo 

Para mi tarea saqué codigo de:
1. https://www.programiz.com/python-programming/methods/list/sort ; Este codigo lo use pare definir una función que me permita ordenar una lista de listas de acuerdo al segundo elementento de cada sub-lista.
   