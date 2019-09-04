# Diagrama de Clases, Tarea 01: Initial P 🚗🏁

## General

* Este diagrama de clases es una version preeliminar en relación a como estará estructurado finalmente mi programa. Debido a que aun me queda mucho codgio por escribir no tengo 100% claro la interaccion entre algunas clases ni certeza de que metodos y atributos implementare en estas finalmente. No obstante este diagrama da una idea general de como estará estructurado el programa.
* Cada cuadrado en el diagrama representa una clase, el titulo es el nombre de la clase; el rectangulo superior incluye a los atributos de las clases y el rectangulo inferior incluye los metodos de las clases.
* Las flechas cuya punta es solida (negra completa) representan comunicacion entre las clases, mientras que las flechas con punta solo contorneadas (blanca con borde negro) representan que las clases heredan de una superclase.
* Por ultimo el color coding en el diagrama es para tratar de agrupar las clases que heredan de una superclase.

## Diagrama

* Mi programa esta constituido por una clase juego, en esta se establecera que partida será la jugada, ya sea una nueva partida o una cargada, guardara el jugador y los contrincantes junto con las pistas y los vehiculos que estarán disponibles. 
* Para la interacción del usuario habrá un conjunto de clases ***Menu*** las cuales hereden de la superclase y sean como el juador interactuará con el programa.
* Para poblar el programa se usarán las clases ***pistas***, ***contrincantes*** y ***vehiculos***, la ultima teniendo 4 subclases que representan a cada tipo de vehículo.
* Para el jugador tambien habrá una clase piloto la cual guardará los atributos de este y tendra los metodos que este pueda usar.

Disclaimer, perdón por la pobreza del diagrama pero no tengo del todo claro como funcionará mi programa.