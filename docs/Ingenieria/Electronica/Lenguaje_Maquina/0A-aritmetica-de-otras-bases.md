---
titulo: "P0A: Aritmética de otras bases"
fecha: "REDACCIÓN"
autor: "Lulo"

progreso: 35

nivel: "Complementario"
tiempo: "~30 min"
etiquetas: [Hexadecimal, Aritmética, Complementarios]
imagen: "pics/mini_elect.jpg"

anterior: 
siguiente: 

enlace_ejercicios: 
enlace_simulaciones: 

descripcion: 
destacado:

lecturas_previas:
  - titulo: "P02: Decimal y binario"
    nivel: "Fácil"
    tiempo: "20 min"
    fecha: "REVISIÓN"
    autor: "Lulo"
    url: "../02-decimal-y-binario/"
  - titulo: "P03: Aritmética binaria"
    nivel: "Fácil"
    tiempo: "~10 min"
    fecha: "REVISIÓN"
    autor: "Lulo"
    url: "../03-aritmetica-binaria/"
  - titulo: "P04: Octal, hexadecimal y BCD"
    nivel: "Básico"
    tiempo: "~10 min"
    fecha: "REVISIÓN"
    autor: "Lulo"
    url: "../04-octal-hexadecimal-y-bcd/"
  - titulo: "P07: Complemento a 1"
    nivel: "Básico"
    tiempo: "5 min"
    fecha: "REVISIÓN"
    autor: "Lulo"
    url: "../07-complemento-a1/"
  - titulo: "P08: Complemento a 2"
    nivel: "Básico"
    tiempo: "~5 min"
    fecha: "REVISIÓN"
    autor: "Lulo"
    url: "../08-complemento-a2/"
---

> ✍🏻 **Autor:** Lulo  
> 📚 **Nivel:** Complementario  
> ⌛ **Tiempo lectura:** ~30 min   
> 🧮 **Matemáticas:** Medio  

---

> ⚠️ **Cuidado:** Esta publicación es una expansión de [Octal, hexadecimal y BCD](04-octal-hexadecimal-y-bcd.md).

---

Teniendo en mente las diferentes bases del [hexadecimal, el octal y el BCD](04-octal-hexadecimal-y-bcd.md), queda aún hablar de cómo se trabaja con ellos aritméticamente. También al final hablaré de la suma de números de distinto signo de los complementos [a 1](07-complemento-a1.md) y [a 2](08-complemento-a2.md).

# Aritmética hexadecimal

## Suma hexadecimal

Es muy parecida a la decimal pero teniendo en cuenta que tenemos los números de $A$ a $F$, que será trabajar con su equivalencia en decimal. Supongamos $2A$ y $1C$, que los vamos a sumar. Realizamos como primer paso las equivalencia de $A$ y $C$ a decimal, que son $10$ y $12$: si los sumamos los queda $22$, pero es mayor a $15$, que es el valor máximo alcanzable. Entonces, tenemos que restarle al resultado este número, resultando $7$: ya tenemos nuestro primer dígito, con un acarreo al siguiente. Para el segundo valor, tenemos $2$, $1$ y otro $1$, debido a que antes cuando sumamos $A$ y $C$ tuvimos un desbordamiento: entonces, la suma nos queda en $4$, que sí es menor a $15$, por lo que no hay nuevo acarreo, y de resultado queda $47$.

$$2A + 1C = (20 + 10) + (A(10) + C(12)) = 30 + (10 + 7) = 47$$

## Resta hexadecimal

Como la resta consiste en sumar dos elementos de signo contrario, ocurre que al segundo valor hace falta cambiarle el signo. En las máquinas, el hexadecimal se usa como simplificación del binario, por lo que tiene que seguir las mismas reglas: nada de signo. Por lo que, podemos ayudarnos del complemento a 2: si tenemos los dos valores en complemento a 2, resulta que, por ejemplo, con dos dígitos en hexadecimal, podemos representar desde el -128 hasta el 127, en complemento a 2.

Para la conversión, podemos emplear tres métodos:

### Hexadecimal-binario

Ya sabemos convertir de hexadecimal a binario y biceversa. En este método es simplemente aplicarlo. Supongamos el $67$, que sería su equivalente a $103$ en decimal. Bueno, pues vamos a convertirlo a binario:

$$67 = 6 // 7 = 0110 // 0111 = 0110 0111$$

Ya tenemos el número en binario complemento a 2, pero en positivo, por lo que hace falta invertirlo para conseguir su versión negativa: pasamos de $01100111$ a $10011000$, con lo que ya tenemos $-67$ en binario. Pero queda un paso final, y es pasar ese valor a hexadecimal, ya que el $-67$ no es posible porque tiene signo. Por ello, hemos de hacer el primer paso, pero hacia atrás y con este nuevo dígito:

$$10011000 = 1001 // 1000 = 9 // 8 = 98$$

Entonces, $67$, su versión negativa es $98$ en complemento a 2. Es antintuitivo, lo sé, pero es así como funciona: no podemos trabajar con un "-", por lo que usamos el complemento a 2, y, para no estar poniendo cantidades ingentes de 0 y 1, compactamos empleando el hexadecimal.

### Restar máximo

Este paso no require tanta conversión, sino solo usar matemáticas: supongamos un rango de $0$ a $100$, en el que $50$ es el centro; si tenemos el número $80$, este está a $30$ unidades de diferencia del centro, ¿cómo sabemos cuál sería su equivalente al lado contrario del centro? Pues, si tenemos el límite superior, pues quitarle a ese límite máximo ($100$) este valor y, lo restante, sumarlo al límite inferior ($0$); esto nos da $20$, y, si obtenemos la distancia que hay con el centro, que sería $30$, es la misma distancia que hay con el ejemplo ($80 - 50 = 30$). Pues esto mismo se hace con este método, pero teniendo como límite superior $FF$, que sería $127$:

$$FF - 67 = F(15) - 6// F(15) - 7 = 9 // 8 = 98$$

### Secuencia inversa

Este es el método más abstracto, pero es exactamente igual al anterior: en vez de tener que efectuar la resta, se busca su equivalente en invertido. Para ello, nos vamos a ayudar con la siguiente tablita:

| **Ordenado** | **Invertidor** |
| :---: | :---: |
| 0 | F |
| 1 | E |
| 2 | D |
| 3 | C |
| 4 | B |
| 5 | A |
| *6* | *9* |
| *7* | *8* |
| 8 | 7 |
| 9 | 6 |
| A | 5 |
| B | 4 |
| C | 3 |
| D | 2 |
| E | 1 |
| F | 0 |

Si nos fijamos, tenemos a la izquierda el $67$ y a la derecha nos cae el $98$.

# Aritmética octal

En este base, no es tan enrevesado, ya que trabajamos con valores que van de $0$ a $7$, por lo que cuando efectuamos sumas o restas, realizamos los acarreos necesarios. Tenemos el $14$, y le restamos $6$: sabemos que $14$, para llegar a nueve, tenemos que quitarle cinco, por lo que pasamos a tener $9 - 1$, pero el nueve está prohibido en esta base, así que pasamos a $7 - 1$, que $7$ es el valor máximo. Entonces, efectuamos la última resta y nos queda $6$.

$$14 - 6 = (7 + 5) - 6 = (7 + 0) - 1 = 7 - 1 = 6$$

En este caso, no tenemos que tener en cuenta el signo o temas de usar el complemento a 2 como en el hexadecimal porque el octal se usa escensialmente en el papel: los ordenadores usan binario y para simplificar se usa directamente el hexadecimal, sin pasar por el octal.

# Aritmética BCD

Esta base tiene un truco, y es que todas las operaciones se comportan de la misma manera: si al efectuarla, el valor resultante entra dentro del ranto (de $0000$ a $1001$), entonces ese es el resultado; si no, lo que esté sobrando se emplea como acarreo. Para emplear un ejemplo simplificado, vamos a sumar $4$ y $7$.

Los pasos son los siguientes: se pasa a binario en BCD, se efectúa la suma. ¿Es un valor permitido? Tenemos el resultado. ¿No? Toca llevar uno de acarreo y lo que nos sobra se queda en esa posición.

$$4 + 7 = 0100 + 0111 = 1011\quad (PROHIBIDO) = 0001\quad (1011 - 1010(10)) = 0001(1) \quad 0001(1) = 11$$

# Aritmética de los complementos

Ahora queda la aritmética de valores con signo, que, para ello, vamos a usar los [complementos](07-complemento-a1.md). Los dos casos funcionan diferente pero tienen algo en común: la importancia de los signos de los valores trabajados y el número de bits.

## Complemento a 1

Cuando efectuamos una suma, puede ser de uno de estos casos: que ambos números sean positivos, que sean de distinto signo, siendo el positivo o el negativo el mayor; y que ambos sean negativos. Y no solo este factor es importante, sino también con cuántos bits trabajamos, ya que este limita el rango de valores.





 PAG 75
explicar resta y suma


## Complemento a 2

solo decir que exactamente igual al 1 pero quitando el paso final de añadirle 1

Indicar el problema de overflow

---




---
