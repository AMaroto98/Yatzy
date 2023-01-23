# Yatzy

Yatzy es un juego de mesa desarollado por Antonio Maroto como alumno del Instituto Francesc de Borja Moll para la asignatura de Programación.

---

## Índice

 - [¿Qué es Yatzy?](#¿qué-es-yatzy)

 - [¿Cómo jugar a Yatzy?](#¿cómo-jugar-a-yatzy)

 - Desarollo

---

## ¿Qué es Yatzy?

Yatzy es un juego de dados cuyo objetivo es obtener la mayor puntuación posible tras sumar las 13 combinaciones disponibles en la tabla de puntuaciones. Puede jugar cualquier número de jugadores, incluso se puede jugar en solitario

---

## ¿Cómo jugar a Yatzy?

Yatzy es un juego simple de dados. Cada jugador lanza 5 dados de 6 caras cada uno. Puedes volver a lanzar los dados hasta un máximo de tres veces (incluyendo el lanzamiento original)

Según la combinación de números que obtiene un jugador puntúa una cantidad u otra.

Las puntuaciones se anotan en la tabla de puntuaciones

---

### Tabla de puntuaciones

Aquí tenemos un ejemplo de una tabla de puntuaciones para jugar a Yatzy.

![Puntuación](images/Puntuacion.jpg)

Tenemos dos secciones donde podemos puntuar:

- Sección superior
- Sección inferior

### Sección superior

En la sección superior podemos anotar la suma de todos los números iguales que hemos obtenido.

Por ejemplo, supongamos que hemos obtenido estos dados:

    1,1,3,3,5

Podríamos anotar una opción de la siguientes:

    2 Puntos en "Unos"

    6 Puntos en "Treses"

    5 Puntos en "Cincos"

Si elegimos puntuar los 6 puntos en "Treses" ya no podemos volver a anotar en "Treses" hasta el final de la partida.

Podemos obtener puntuación extra (35 puntos) si la suma de todas las casillas de la sección superior es igual o superior a 63 puntos.

---

### Sección inferior

Así como la sección superior se rige por una misma norma, la suma de todos los números iguales, la sección inferior mayoritariamente es diferente, veámoslo en detalle:

#### 3 iguales

Es igual que en la sección superior, se produce cuando obtenemos tres dados iguales.

La puntuación es la suma de los tres dados iguales.

Por ejemplo:

    3,3,3,4,5

La puntuación en este caso sería de 9 puntos.

---

#### 4 iguales

Es igual que en la sección superior, se produce cuando obtenemos cuatro dados iguales.

La puntuación es la suma de los cuatro dados iguales.

Por ejemplo:

    2,2,2,2,1

La puntuación en este caso sería de 8 puntos.

---

#### Full / Full House:

Se produce cuando obtenemos la combinación de dos y tres dados iguales.

La puntuación con Full House es de 25 puntos.

Por ejemplo:

    3,3,4,4,4

---

#### Escalera corta:

Se produce cuando obtenemos una secuencia de cuatro números consecutivos.

La puntuación de la escalera corta es de 30 puntos.

Por ejemplo:

    1,2,3,4,4

---

#### Escalera larga:

Se produce cuando obtenemos una secuencia de cinco números consecutivos.

La puntuación de la escalera larga es de 40 puntos.

Por ejemplo:

    1,2,3,4,5

---

#### Yatzy:

 Se produce cuando obtenemos cinco números iguales.

 La puntuación de Yatzy es de 50 puntos.

Por ejemplo:

    1,1,1,1,1

---

#### Azar / Chance:

Se produce siempre, y podemos decidir usarlo cuando queramos, sería algo así como un comodín.

La puntuación de Azar / Chance es la suma de los cinco dados.

Por ejemplo:

    1,1,2,2,3

La puntuación en este caso sería de 9 puntos.

---

#### Extra

Si a lo largo de la partida un jugador consigue hacer más de un Yatzy se le suman 50 puntos.

---

#### Importante

Si durante el transcurso de la partida algún jugador obtiene una combinación de 5 dados que no le aporta nada en ninguna de las secciones, está obligado a puntuar 0 puntos.

Todos los jugadores deben puntuar siempre en todos los turnos.

#### Total general

Es la suma de ambas secciones.

Gana el jugador que obtiene la mayor puntuación


### Ejemplo

Supongamos que el jugador ha conseguido los siguientes dados:

    3,4,5,5,2

El jugador decide guardar los dados (-,-,5,5,-) y vuelve a lanzar los tres dados restantes (3,4,-,-,2):

    5,2,5,5,1

El jugador decide guardar los dados en los que ha obtenido un cinco (5,-,5,5,-) y vuelve a lanzar los dos dados restantes (-,2,-,-,1):

    5,3,5,5,3

Una vez tenemos los dados finales podemos observar que hemos obtenido una de la siguientes opciones Full House, 3 iguales, Chance / Azar, Treses o Cincos. 

Ahora ya es decisión del jugador elegir donde puntuar.

## Desarollo



