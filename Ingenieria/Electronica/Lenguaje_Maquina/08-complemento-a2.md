# Complemento a 2.

> ✍🏻 **Autor:** Lulo.  
> 📚 **Nivel:** Básico.  
> ⌛ **Tiempo lectura:** ~5 min.  
> 📖 **Lectura previa:** [Complemento a 1.](07-complemento-a1.md)  
> 🧮 **Matemáticas:** Básicas.  
> 🏷️ **Etiquetas:** `Binario`, `Conversión de bases`.

[Magnitud y signo](06-representacion-con-signo.md) y el [complemento a 1](07-complemento-a1.md) tenían el principal problema que representaban el cero de dos formas distintas. El complemento a 2 es la solución.

# Diferencia con el resto de binarios.

Este complemento es exactamente igual al a 1: para los negativos, el primer paso es reservar un bit de signo y luego invertimos los valores, pero, el paso que hace la diferencia, es, después de la conversión, sumarle $1$.

Tenemos a nuestro $-12$, que, su módulo en 8 bits, era $00001100$. Ahora lo vamos a convertir en complemento a 1, que sería invertir los ceros poniendo un uno y los unos colocando un cero en su lugar: $11110011$. Por último, lo hacemos en complemento a 2, que es solo sumarle uno, teniendo $11110100$. Así de simple.

| **Decimal** | **Binario natural** | **Complemento a 2** |
| :---: | :---: | :---: |
| -12 | -1100 | 11110100 |

## Conversión a decimal.

Con la misma idea que el signo y magnitud y el complemento a 1, en el a 2, si es positivo, se convierte aplicando las mismas reglas que en el binario natural, y si es negativo, que se observa en el bit de signo, se invierte y se le vuelve a sumar $1$.

Es algo complicado de ver, pero vamos a intetar "positivar" el $11110100$: primero lo invertimos, siendo $00001011$, y luego le sumamos $1$, por lo que nos queda $00001100$, que resulta en el módulo de $-12$. Pues así se hace con todos los números con este complemento, ya en un sentido u en otro: mirar bit de signo, y si es negativo invertir y sumar uno, ya sea de binario a decimal o decimal a binario.

# Limitaciones.

¿Sigue existiendo el problema del cero? Tenemos $00000000$, que sería el equivalente a $+0$. Intentémos negarlo: primero, invertimos todos los bits, $11111111$, y le sumamos el uno del complemento a 2: $100000000$, pero como tenemos 8 bits, nos quitamos el que está de más, quedando $00000000$. De esta forma vemos que:

$$+0 == 00000000 == -0$$

Ahora, como representamos el cero con un solo carácter, podemos representar en total $256$ carácteres, del rango de $-128$ hasta $127$, tomándose el cero como positivo.

## Overflow.

Me gustaría meter un término que por ahora no habíamos trabajado que es el *overflow* /ˈəʊvəˌfləʊ/ (desbordamiento, en castellano). Cuando trabajamos la [aritmética binaria](03-aritmetica-binaria.md) vimos qué sucedía con la suma, que aparecía el acarreo, que era un bit que se sumaba al superior. Cuando trabajamos con un número limitado de bits, sucede que si nos salimos del rango, surgen problemas.

> 😬 **Experiencia:** Cuando he trabajado con simulaciones y montajes de ALUs (calculadoras binarias), normalmente se tenía que poner un bit de desbordamiento, para así saber que el resultado que se estaba indicando estaba mal.

En el ejemplo anterior que vimos con el cero, sucedió eso mismo: sumamos uno a un valor que terminaba con un acarreo en el bit 9, bit que está fuera del rango. Este último bit se tiene que eliminar, porque si lo volvemos a introducir nos va a dar problemas de representación.

> ❗ **Curiosidad:** Hay un ejemplo que me gusta mucho dar sobre el overflow, aunque hay que resaltar que es una leyenda muy extendida: en el videojuego de Civilization 1 había un error de código que, cada vez que hacías cosas que le gustaban a otros jugadores, estos bajaban su nivel de agresividad. En el caso de Ghandi, que era el jugador con menor nivel, se decía que se podía bajar tanto que en el código resultaba en un overflow negativo (underflow), pero como se guardaba en un dato en binario natural de 8 bits, no pasaba a -1, sino saltaba a 255, que era el nivel máximo.

# Tabla resumen.

Cuando estamos en binario natural, solo podemos representar en papel el "-", pero las máquinas no lo pueden hacer. De ahí que exista el bit de signo, que se puede usar con el signo y magnitud, que es solo reservando un bit para indicar si es positivo o negativo; tenemos el complemento a 1, que es invirtiendo todos los bits; y por último el complemento a 2, que es el complemento a 1 sumándole $1$ al final para solucionar el problema de la doble representación del cero.

| **Representación** | **Valor (8 bits)** |
| :---: | :---: |
| **Decimal** | $-12$ |
| **Binario natural** | $-00001100$ |
| **Signo y magnitud** | $10001100$ |
| **Complemento a 1** | $11110011$ |
| **Complemento a 2** | $11110100$ |

---

Problema del signo, resuelto. Pero ahora nos surge un nuevo problema: las comas. Vimos que los decimales los representábamos poniendo una coma, pero resulta que en binario **tampoco** podemos usar comas. ¿Solución? Los números en coma flotante.

---
---

# Fuentes.

- *Fundamentos de sistemas digitales* – L. Floyd.

---

### Navegación.

- ➡️ **Siguiente:** [Números en coma flotante.](09-numeros-en-coma-flotante.md)
- ⬅️ **Anterior:** [Complemento a 1.](07-complemento-a1.md)
- 🔗 **Publicación en Blogger:** [Complemento a 2.]()