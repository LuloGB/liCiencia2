# Aritmética binaria.

> ✍🏻 **Autor:** Lulo.  
> 📚 **Nivel:** Fácil.  
> ⌛ **Tiempo lectura:** ~10 min.  
> 📖 **Lectura previa:** [Decimal y binario.](02-decimal-y-binario.md)  
> 🧮 **Matemáticas:** Básicas.  
> 🏷️ **Etiquetas:** `Binario`.  

Hemos pasado de [decimal a binario](https://github.com/LuloGB/liCiencia2/blob/pre-publicaciones-electronica/Ingenieria/Electronica/Lenguaje_Maquina/02-decimal-y-binario.md), pero para poder efectuar cálculos y no querer marearnos con los números, sale más efectivo aprender cómo se hace en base 2.

Seguramente habrás oído el chiste informático de 1+1 es igual a 10. Hoy estás en tu día de suerte (o mala suerte), porque vas a entenderlo.

# Suma.

Como en el colegio, lo que nos enseñan justo después de contar, es sumar. En binario es exactametne igual: si sumas a $0$, el resultado es el mismo. Y cuando sumamos un número que da mayor a $1$ (como $1+1$), tenemos algo que llamaremos *acarreo* o *carry* /ˈkæɹi/ y consiste en que desplazamos el $1$ que nos sobra a la izquierda y ponemos un 0 en la derecha. Es como si cogiéramos el uno sobrante, ponemos el resultado a cero y lo sumamos a la posición de la izquierda.

> ☝🏻🤓 **Aclaración:** Si sumas 9 + 1, sucede que te da 10. Esto es porque hemos metido un acarreo de 1, y ponemos el número más pequeño a la derecha, que es cero. En todas las bases es así.

$$
\begin{aligned}
0+0&=0 \\
0+1&=1 \\
1+0&=1 \\
1+1&=10
\end{aligned}
$$

Pues en esta tabla se ve el chiste informático.

# Resta.

Al igual que existe la suma, también tenemos resta, que es muy parecido, pero en signo contrario: si tenemos dos unos, los quitamos, y si tenemos ceros, se deja igual.

$$
\begin{aligned}
0-0&=0 \\
1-1&=0 \\
1-0&=1 \\
10-1&=1
\end{aligned}
$$

Al igual que teníamos el acarreo, existe el *accarreo negativo*, que este es como cuando restamos 10 - 1, y tenemos 9, pues en binario, si le quitamos 1 a 10, tenemos 1, porque si convertimos 10 a decimal es 2, y si le quitamos 1 a 2, nos da 1. Es algo confuso al comienzo, pero uno se acostumbra.

# Multiplicación.

Seguramente ya sabían multiplicar binario antes de llegar a leer esto: si es verdadero y lo pongo falso es falso; si es verdadero y verdadero, es verdadero; pero si es falso y falso, es verdadero. Si cambiamos "verdadero" por 1 y "falso" por 0, tenemos multiplicación binaria.

> ❗ **Curiosidad:** Toda la lógica, incluyendo la multiplicación, está basada en los trabajos de *George Boole*, que seguramente te suene más por estadística.

$$
\begin{aligned}
0·0&=0 \\
0·1&=0 \\
1·0&=0 \\
1·1&=1
\end{aligned}
$$

> 😬 **Experiencia:** Les prometo que de toda la aritmética binaria, de la multiplicación se van a hartar, por lo que es muy importante entenderlo ahora.

# División.

Sinceramente, para dividir tuve que aprender solo para explicarlo aquí, ya que siempre ha resultado hacerlo más rápido pasándolo todo a decimal, efectuar el cálculo y el resultado convertirlo. Aunque, si quieren saberlo, funciona igual que la división que hemos tenido que hacer en las divisiones sucesivas.

Para no parecer que lo dejo a medias, les voy a dar un ejemplo muy sencillo: $110 \div 11$. Empezamos por comparar los dos primeros valores, de izquierda a derecha, de $110$, que es $11$, y las veces que hace falta multiplicar el denominador, $11$, para que sea igual es por $1$. Luego, nos queda $00$, y, para este caso, sería por $0$. Entonces, de cociente nos queda $10$ y de resto $0$.

$$
\begin{array}{r|ll}
\text{Operación} & \text{Cociente} & \text{resto} \\
\hline
110 \div 11 & \mathbf{10} & \mathbf{0} \quad \\
\end{array}
$$

> 📒 **Ejercicio:** Si no me crees, convierte $110$ y $11$ a decimal, efectua la división y luego, el resultado, pásalo a binario a ver si no es igual a $10$.

---

Ya creo que hemos tenido suficientes matemáticas. Antes quiero coger un pequeño desvío que va a consistir en explicar otras bases que existen, como el hexadecimal y el octal, que nos resultarán extremadamente útiles cuando veamos cómo procesan la información los ordenadores.

---
---
# Fuentes.

- *Fundamentos de sistemas digitales* – L. Floyd.

---
### Navegación.

- ➡️ **Siguiente:** [Octal, hexadecimal y BCD.](04-octal-hexadecimal-y-bcd.md)
- ⬅️ **Anterior:** [Decimal y binario.](02-decimal-y-binario.md)