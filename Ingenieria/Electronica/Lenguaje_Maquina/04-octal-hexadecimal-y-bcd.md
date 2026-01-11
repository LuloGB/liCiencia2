# Octal, hexadecimal y BCD.

> ✍🏻 **Autor:** Lulo.  
> 📚 **Nivel:** Medio.  
> ⌛ **Tiempo lectura:** ~10 min.  
> 📖 **Lectura previa:** [Decimal y binario.](02-decimal-y-binario.md)  
> 🧮 **Matemáticas:** Básicas.  
> 🏷️ **Etiquetas:** `Conversión de bases`, `Binario`, `Hexadecimal`.

Ahora me gustaría aprovechar para coger un pequeño desvío. Ya hemos hablado de la [base dos](02-decimal-y-binario.md), pero hay otras bases que son igual de importante: la *hexadecimal* (base 16), *octal* (base 8) y *BCD* (Código Decimal Binario).

> ⚠️ **Cuidado:** Esta publicación es continuación directa de [Decimal y binario.](02-decimal-y-binario.md) Se va a estar pasando decimal a binario todo el rato, por lo que recomiendo que tengas un buen manejo de conversión de bases, o por lo menos entender cómo funcionan.

# Hexadecimal.

Tenemos la base diez, con diez caracteres del 0 al 9. Luego el binario, con dos caracteres, el 0 y el 1. La base *hexadecimal*, presenta 16 caracteres. Esto acarrea un problema, que no se llega a notar a primera vista: los diez caracteres de la base diez no son suficientes, por lo que hace falta recurrir a caracteres alfabéticos.

Vamos a contar en base 10: cero (0), uno (1), dos (2), tres (3)... nueve (9) y creamos el uno-cero (10), que llamamos diez. Es como cuando ya hemos usado todos los caracteres numéricos en una posición, sumamos uno a la posición superior y reiniciamos en la que nos encontrábamos. Ahora vamos a hacer lo mismo en base 16: cero (0), uno (1), dos (2), tres (3)... nueve (9) y... ¿Se vio? No podemos usar uno-cero, porque esto sería en base diez, y aún nos queda poner desde el diez hasta quince. Entonces, ¿cómo se soluciona esto? Pues vamos al abecedario: A (10), B (11), C (12), D (13), E (14) y F(15).

$$
\begin{aligned}
&\text{Decimal} & \text{Hexadecimal}  \\
&0 & 0 \\
&1 & 1 \\
&2 & 2 \\
&3 & 3 \\
&4 & 4 \\
&5 & 5 \\
&6 & 6 \\
&7 & 7 \\
&8 & 8 \\
&9 & 9 \\
&10 & A \\
&11 & B \\
&12 & C \\
&13 & D \\
&14 & E \\
&15 & F \\
\end{aligned}
$$

> ❗ **Curiosidad:** Si has ido a una ferretería o almacén a combrarte un cubo de pintura, las muestras que te dan a veces sale F3A8 o cosas así, y es porque está representado en hexadecimal.

## Conversión binario a hexadecimal.

Ya tenemos la equivalencia decimal-hexadecimal, pero hay un problema, y es que para poder convertir entre estas dos bases, es algo incómodo de hacer, por lo que nos vamos a ayudar del binario: primero convertimos el número, ya en decimal, ya en hexadecimal, a binario y luego se torna a la base deseada. La base decimal ya la hemos trabajado previamente, por lo que hoy voy a poner directamente binario-hexadecimal.

Tenemos un número en binario, el $1101011$, y, para poderlo convertir es muy sencillo: lo agrupamos de cuatro en cuatro de derecha a izquierda, quedando así: $0110 \text{ } 1011$. Cuando tenemos grupos menos de cuatro posiciones, se añaden $0$ hasta tener el grupo lleno. Ahora cada grupo lo pasamos a base diez:

$$
\begin{aligned}
0110 &= 6 \\
1011 &= 11
\end{aligned}
$$

Tenemos el $611$, pero no es el seiscientos once, sino el número en hexadecimal, pero sin convertir: nos hace falta cambiar el $11$ por su equivalente en hexadecimal: $B$. Hemos conseguido el $6B$, que es $1101011$ en base 16. 

> ☝🏻🤓 **Aclaración:** ¿Por qué se agrupan de 4 en 4? Cuenta de 0 a 1111 en decimal: vas a ver que pasamos de 0 a 15, que son los dígitos que representan el hexadecimal. Es así de simple.

## Conversión binario a hexadecimal.

Para poder deshacer el ejemplo anterior es tan sencillo como separar los dígitos, convertir cada uno a decimal y pasarlo de decimal a binario:

$$6B=6\text{ y }B = { \begin{matrix}
                    6 = 0110 \\
                    B = 1011 \\
                    \end{matrix}}
                    = 0110 \text{ } 1011
$$

### Converisón hexadecimal a decimal directa.

En verdad, sí existe una forma de convertir el hexadecimal al decimal y de forma directa: es mediante suma de pesos. Al igual que en el binario, teníamos a $2^n$, siendo $n$ la posición del dígito, empezando desde $0$. En hexadecimal es igual, pero en vez de $2^n$, usamos $16^n$.

Volvamos al ejemplo resuelto antes, que es el $6B$, y vamos a convertirlo:

$$6B=6*16^1[16]+B[11]*16^0[1]=96+11=107$$

> ❗ **Curiosidad:** Si uno se fija, de esta forma podemos compactar mucho números muy grandes: el 867455 en decimal es D3C7F en hexadecimal, y en binario son 20 dígitos, por lo que se nota la diferencia.

# Octal.

Otra base muy interesante es la octal, con ocho dígitos, del $0$ al $7$, que es igual de sencilla como la hexadecimal: no podemo hacer conversiones directas octal-decimal, pero sí indirectamente con el binario, pero esta vez no agrupando de cuatro en cuatro, sino de tres en tres.

## Conversión binario a octal.

Vamos a usar el mismo ejemplo de antes, el $1101011$. Recordemos que estamos en octal, por lo que vamos a agruparlo de tres en tres y convertir cada valor a su equivalente en decimal:

$$
1101011=001\text{ }101\text{ }011={ \begin{matrix}
                    001 = 1 \\
                    101 = 5 \\
                    011 = 3
                    \end{matrix} }
                    = 153
$$

Entonces, nos termina quedando el $153$ en base octal. 

> ☝🏻🤓 **Aclaración:** En octal no nos hace falta añadir más dígitos porque como usamos los mismos que en decimal, y este tiene hasta diez dígitos, pues en verdad nos sobran dos, el 8 y el 9.

## Conversión octal a binario.

Esto tampoco tiene demasiada ciencia: es volver a usar el concepto de conversión hexadecimal-binario, pero haciéndolo de tres en tres.

$$
153=1\text{, }5\text{ y }3={ \begin{matrix}
                    1 = 001 \\
                    5 = 101 \\
                    3 = 011
                    \end{matrix}}
                    = 001\text{ }101\text{ }011
$$

### Conversión octal a decimal directo.

En base dos tenemos $2^n$, en base dieciseis $16^n$ y, por intuición, en base ocho es $8^n$, que, aplicando la definición de los pesos, podemos pasar de base octal a base diez:

$$153=1*8^2[64]+5*8^1[8]+3*8^0[1]=64+40+3=107$$

Con lo que hemos obtenido el mismo valor pasándolo del binario al decimal a través del hexadecimal como del octal.

# BCD.

El *código decimal binario*, o, como sus siglas en inglés, el *Binary Coded Decimal*, es una forma "bruta" de convertir decimal a binario: en vez de hacerlo convirtiéndolo de base diez a base dos, solo lo hacemos con los diez dígitos de la base diez y los agrupamos tal cual salgan.

Existen mil y un formas de representar el código BCD: por ejemplo podemos poner a $1$ representado por $1011010101$ y al $2$ por $101111100$ y el $12$ por ejemplo ponerlo como $1011010101\text{ }101111100$. Es muy feo, lo sé, pero se puede hacer.

## Código 8421.

Aquí no somos artistas, sino ingenieros, por lo que hace falta simplificar lo máximo posible, y para eso tenemos el *BCD 8421*. En esta representación vamos a trabajar con 4 dígitos, que, como hemos usado en el binario anteriormente, es con los que hacen falta representar los diez dígitos del decimal:

$$
\begin{array}{|c|c|}
\textbf{Decimal} & \textbf{Binario} \\
0 & 0000 \\
1 & 0001 \\
2 & 0010 \\
3 & 0011 \\
4 & 0100 \\
5 & 0101 \\
6 & 0110 \\
7 & 0111 \\
8 & 1000 \\
9 & 1001 \\
\end{array}
$$

> ☝🏻🤓 **Aclaración:** Los números 8421 es por los pesos: como usamos 4 dígitos para representarlos, el cuarto valor se multiplica por 8, el tercero por 4, el segundo por 2 y el último por 1, y por último se suman.

## Conversión decimal a BCD.

Vamos a coger el valor que conseguimos antes en decimal, el $107$ y vamos a convertirlo: es coger cada dígito y pasarlo al binario con 4 valores.

$$107=1\text{, }0\text{ y }7={ \begin{matrix}
                    1 = 0001 \\
                    0 = 0000 \\
                    7 = 0111
                    \end{matrix} }
                    = 0001\text{ }0000\text{ }0111
$$

> ⚠️ **Cuidado:** La conversión BCD a decimal está algo más limitada: se agrupan de cuatro en cuarto y se va cambiando su equivalente a base diez, pero existen valores prohibidos: por ejemplo el 1100, que es el 12, en BCD no se puede representar, porque solo se pueden usar los valores del 0 al 9, por tanto, ese valor en binario sería ilegal en este caso.

# Tabla resumen.

$$
\begin{matrix}
&\textbf{Decimal}&\textbf{Binario}&\textbf{Hexadecimal}&\textbf{Octal}&\textbf{BCD}\\
&107&1101011&6B&153&000100000111
\end{matrix}
$$

> 😬 **Experiencia:** ¿Para qué sirve todo esto si con el binario es suficiente? Cuando empecé a trabajar con microprocesadores me di cuenta de lo importante que es el hexadecimal y cuando apliquemos decodificadores con 7 segmentos quizás vean que el BCD 8421 tiene verdadera utilidad.

---

Aún quedan puntos como la aritmética con estas bases o la conversión de coma flotante, pero eso haría que esta publicación se volviera casi eterna, por lo que lo pondré en otra a parte. Con entender bien cómo se representa el hexadecimal y que existe el BCD, con eso, es más que suficiente como para poder seguir adelante.

---
---
# Fuentes.

- *Fundamentos de sistemas digitales* – L. Floyd.

---
### Navegación.

- ➡️ **Siguiente:** [Bit, Byte y Nyble.](#)
- ⬅️ **Anterior:** [Aritmética binaria.](03-aritmetica-binaria.md)