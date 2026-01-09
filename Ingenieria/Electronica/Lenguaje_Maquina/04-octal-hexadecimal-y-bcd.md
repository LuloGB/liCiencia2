# Octal, hexadecimal y BCD.

> ✍🏻 **Autor:** Lulo.  
> 📚 **Nivel:** Medio.  
> ⌛ **Tiempo lectura:** .  
> 📖 **Lectura previa:** [Decimal y binario.](02-decimal-y-binario.md)  
> 🧮 **Matemáticas:** Básicas.  
> 🏷️ **Etiquetas:** `Conversión de bases`, `Binario`, `Hexadecimal`.

Ahora me gustaría aprovechar para coger un pequeño desvío. Ya hemos hablado de la [base dos](02-decimal-y-binario.md), pero hay otras bases que son igual de importante que son la *hexadecimal* (base 16), *octal* (base 8) y *BCD* (Código Decimal Binario).

> ⚠️ **Cuidado:** Esta publicación es continuación directa de [Decimal y binario.](02-decimal-y-binario.md) Se va a estar pasando decimal a binario todo el rato, por lo que recomiendo que tengas un buen manejo de conversión de bases, o por lo menos entender cómo funcionan.

# Hexadecimal.

Tenemos la base diez, con diez caracteres del 0 al 9. Luego el binario, con dos caracteres, el 0 y el 1. Ahora, con la base *hexadecimal*, que presenta 16 caracteres. Hay un problema que no se llega a notar a primera vista cuando intentamos trabajar con esta base, y son los caracteres con los que los representamos: los diez caracteres de la base diez no son suficientes, por lo que hace falta recurir a caracteres alfabéticos.

Vamos a contar en base 10: cero (0), uno (1), dos (2), tres (3)... nueve (9) y creamos el uno-cero (10), que llamamos diez. Es como cuando ya hemos usado todos los caracteres numéricos en una posición, sumamos uno a la posición superior y reiniciamos esta. Ahora vamos a hacer lo mismo en base 16: cero (0), uno (1), dos (2), tres (3)... nueve (9) y... ¿Se vio? No podemos usar uno-cero, porque esto es base diez, y aún nos queda poner desde el diez hasta quince. Entonces, ¿cómo se soluciona esto? Pues vamos al abecedario: A (10), B (11), C (12), D (13), E (14) y F(15).

$$
\begin{aligned}
\text{Decimal} & \text{Hexadecimal}  \\
0 & 0 \\
1 & 1 \\
2 & 2 \\
3 & 3 \\
4 & 4 \\
5 & 5 \\                                    CORREGIR LOS ESPACIOS
6 & 6 \\
7 & 7 \\
8 & 8 \\
9 & 9 \\
10 & A \\
11 & B \\
12 & C \\
13 & D \\
14 & E \\
15 & F \\
\end{aligned}
$$

> ❗ **Curiosidad:** Si has ido a una ferretería o almacén a combrarte un cubo de pintura, las muestras que te dan a veces sale F3A8 o cosas así, y es porque está representado en hexadecimal. De hecho, ahora mismo escribiendo esto le puse # antes del ejemplo y me puso un cuadradito en ese color.

Para convertirlo es muy sencillo. Tenemos un número en binario, el $1101011$, y lo agrupamos de cuatro en cuatro de derecha a izquierda, así $0110 1011$, añadiendo $0$ para tener los grupitos llenos. Cada grupo se pasa a base diez:

$$
\begin{aligned}
0110 &= 

TERMINAR 
\end{aligned}
$$





REVISAR:
> 😬 **Experiencia:** Hasta que no empecé a trabajar con microprocesadores, no me di cuenta lo importante que es esta base: es como se numeran las memorias y como se representan los datos almacenados en memoria.









---
---
# Fuentes.

- *Fundamentos de sistemas digitales* – L. Floyd.

---
### Navegación.

- ➡️ **Siguiente:** [](#)
- ⬅️ **Anterior:** [Aritmética binaria](03-aritmetica-binaria.md)