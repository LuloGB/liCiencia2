---
titulo: "P06: Representación con signo"
fecha: "REVISIÓN"
autor: "Lulo"

progreso: 50

nivel: "Básico"
tiempo: "~5 min"
etiquetas: [Binario, Conversión de bases]
imagen: "pics/mini_elect.jpg"

anterior: "../05-bit-byte-y-nibble/"
siguiente: "../07-complemento-a1/"

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
  - titulo: "P05: Bit, byte y nibble"
    nivel: "Básico"
    tiempo: "~5 min"
    fecha: "REVISIÓN"
    autor: "Lulo"
    url: "../05-bit-byte-y-nibble/"
---

> ✍🏻 **Autor:** Lulo  
> 📚 **Nivel:** Básico  
> ⌛ **Tiempo lectura:** ~5 min  
> 🧮 **Matemáticas:** Básicas.  

En el mundo de la electrónica existen diferentes tipos de binarios. El usar uno u otro depende de la estructura del microprocesador, la capacidad de memoria, la potencia y, en general, para qué lo vamos a usar. En las siguientes publicaciones vamos a ver por qué existen varios binarios.

# Problema del signo

Hasta el momento solo hemos dado [binario natural](02-decimal-y-binario.md): con él podemos representar con comodidad todos los números mayores de cero, incluido este. Pero nos ha surgido un problema y es cómo representar valores menores a cero. Si lo hacemos a lo bruto, podemos añadir solo un "-" al comienzo: que $-6$ sea $-110$ en binario. Si volvemos al funcionamiento del binario, esto no tiene sentido, debido a que las máquinas no pueden representar valores diferentes a 1 y 0 (alto y bajo, si lo pasamos a niveles de tensión).  Para solucionar este inconveniente, surge algo llamado *bit de signo*.

# Signo-magnitud

Cuando se quiere representar un número, como el $6$, en binario natural, vamos a necesitar tres bits, ya que es $110$. Ahora vamos a hacerlo con $-6$, pero ayudándonos del bit de signo: este bit es un valor que se añade al comienzo del número y con el que representamos si es positivo (0), o negativo (1): de esta forma queda en $1101$.

Vamos a hacer otro ejemplo pero un poco más complejo: el $-12$. Para el módulo de este número hacen falta $4$ bits, $1100$, pero vamos a representarlo en signo y magnitud con $8$ bits: tenemos el primer bit que es el signo, que sería $1$ al ser negativo; luego le sigue el módulo del ejemplo en binario natural, $1100$; con esto nos dan en total $5$ bits, pero para llegar a $8$ quedan tres, que será la cantidad de $0$ que se colocan entre el signo y el módulo. Así, la conversión sería la siguiente:

| **Decimal** | **Binario natural** | **Signo-magnitud** |
| :---: | :---: | :---: |
| -12 | -1100 | 10001100 |

Así se puede hacer con todos los números, a los positivos les añadimos un cero al comiezo y a los negativos un uno.

## Conversión a decimal

Ahora quizás uno empiece a confundirse: pero si transformamos el $1101$ a decimal nos queda $13$, no $-6$. Eso sería si estuviéramos en binario natural, pero al encontrarnos en signo y magnitud, solo tenemos que poner aparte el primer bit, ver si es negativo o positivo, y con el resto del dato convertirlo a decimal como si de binario natural se tratase.

> ⚠️ **Cuidado:** Cuando se trabajan con diferentes tipos de binario, sobre todo con magnitud y signo, es importante decir el tipo que es y con cuántos bits se trabajan, para así evitar confusiones.

## Limitaciones

En binario natural podemos contar desde $0$ hasta $2^n-1$, siendo $n$ el número de bits con los que trabajamos. Ahora hay un problema, y es que tenemos que sacrificar el último bit para indicar el signo. Hemos pasado a contar de $-2^{n-1}-1$ hasta $2^{n-1}-1$.

| **nº bits** | **Rango Binario natural** | **Rango magnitud-signo** |
| :---: | :---: | :---: |
| 8 | 0 a 255 | -127 a 127 |

Ahora quiero que reflexiones lo siguiente que te voy a plantear: si con $8$ bits podemos representar en binario hasta $256$ combinaciones diferentes, ¿por qué en signo y magnitud represento solo $254$, que son $127$ dos veces? Esto es porque no hemos tenido en cuenta el $0$. Si sumamos este carácter, solo nos suman $255$. Sigue faltando uno. Pues seguimos sin tener en cuenta una cosa.

Intentemos representar el $0$. Ponemos primero el bit del signo y el resto de bits a cero. ¿Pero qué signo? Es obligatorio ponerlo en esta representación del binario. ¿El cero es positivo o negativo? Pues en signo y magnitud el cero es positivo *y* negativo al mismo tiempo.

$0 == 00000000 == 10000000$

> ❗ **Curiosidad:** Si un ordenador solo entienden unos y ceros, ¿cómo sabe en qué binario trabaja los números? Pues cuando se le mandan datos, estos van acompañados de trozos de códigos (ceros y unos) que le dicen al procesador cómo tiene que trabajar esos valores.

---

Ahora tenemos una forma de representar números negativos, pero nos encontramos con el problema del cero, que bastantes veces es algo muy poco deseado. Para esto existen los complementos a1 y a2.

---
