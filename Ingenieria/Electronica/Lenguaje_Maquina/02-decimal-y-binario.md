# Bases.

> ✍🏻 **Autor:** Lulo.  
> 📚 **Nivel:** Fácil.  
> ⌛ **Tiempo lectura:** 20 min.  
> 📖 **Lectura previa:** No necesaria.  
> 🧮 **Matemáticas:** Básicas.  
> 🏷️ **Etiquetas:** `Binario`, `Decimal`, `Conversión de bases`.  

El manejo de los números es algo que nos acompaña en nuestro día a día, y una herramienta accesible que empleamos son los dedos de nuestras manos. Con ellos, podemos contar desde el cero al diez: esto es lo que conforma la *base diez*.

> ☝🏻🤓 **Aclaración:** Más concretamente, la base diez emplea los dígitos del 0 al 9.

Ya entendiendo la [señal digital](https://github.com/LuloGB/liCiencia2/blob/main/Ingenieria/Electronica/Lenguaje_Maquina/01-senial-digital.md), teníamos el problema de que no sabíamos trabajar matemáticamente eso. Como primer punto, como ya habíamos hecho, fue convertir High en un uno, y Low en un cero. Con estos dos símbolos, podemos representar toda una base numérica, que vamos a darle el nombre de **binario**.
Hemos logrado pasar de cuadrados a números, que con ellos podremos hacer cuentas, pero antes de ponernos locos sumando y restando, vamos a intentar primero traducirlos: antes de ponerse uno a hacer oraciones en inglés, tenemos que saber cómo pasar del español al inglés. Con las bases, sucede lo mismo, por lo que lo siguiente será aprender *conversiones de bases*.

# Conversión binario a decimal.

Repasaremos primero cómo se construye la base diez. Tomemos el número $157$, en el cual tenemos tres dígitos: el $1$, el $5$ y el $7$. Si lo descomponemos, en verdad lo que vemos son el $100$, el $50$ y el $7$. Cada uno multiplica por $10^n$, siendo $n$ la posición en la que se encuentra, y se suman.

$$1 · 10^2 + 5 · 10^2 + 7 · 10^0 = 157$$

> ☝🏻🤓 **Aclaración:** Cuando empezamos a contar, no iniciamos en $10^1$, sino en $10^0$.

Este método de "descomponer" se puede usar también para el binario. Ahora tenemos el número $10011101$. Repetimos el mismo procedimiento, pero esta vez estamos en la base binaria, en la que solo hay dos símbolos, por tanto, no se eleva a $10$, sino a $2$. Entonces, tomando el dígito y multiplicándolo por la posición, tenemos lo siguiente:

$$1 · 2^7 | 0 · 2^6 | 0 · 2^5 | 1 · 2^4 | 1 · 2^3 | 1 · 2^2 | 0 · 2^1 | 1 · 2^0 $$

> 🧐 **Interpretación:** El truco para leer el binario es solo decir "uno" y "cero", no, como ahora, "diez millones once mil ciento uno", que es hasta pesado. Imagínate hacerlo cuando tenemos 32 dígitos, que es lo normal.

Con esto, tenemos el número catalogado, pero lo sorprendente viene después, que es sumándolo:

$$1 · 2^7 + 0 · 2^6 + 0 · 2^5 + 1 · 2^4 + 1 · 2^3 + 1 · 2^2 + 0 · 2^1+ 1 · 2^0 \Rightarrow 1 · 2^7 + 1 · 2^4 + 1 · 2^3 + 1 · 2^2 + 1 · 2^0 = 157 $$

> ☝🏻🤓 **Aclaración:** $n^0$, siendo $n$ cualquier número real, quitando el cero, siempre da $1$.

De esta forma hemos pasado de una ristra de unos y ceros a un número que entendemos más: así funciona el *método de conversión binario-decimal*. Ahora, ¿qué pasa si lo queremos hacer al revés?

> 📒 **Ejercicio:** Esto también funciona cuando tenemos números de coma flotante. Intenta hacer la conversión de 1011,110101, a ver si te sale. **Pista:** Igual que para las unidades y superiores usamos enteros de $0$ hacia arriba, para los que están por debajo de la coma son con enteros negativos.

# Conversión decimal a binario.

Ahora es necesario meter un nuevo concepto que son *los pesos de 2*. En base diez es muy cómodo el convertir de notación exponencial a normal, que es poner el número de ceros que sale en el exponente. Cuando estamos en base dos, es mucho más cómodo pasarlo todo a decimal, que para ello solo hace falta saberse la tabla del dos:

$$
\begin{aligned}
2^0 &= 1 \\
2^1 &= 2 \\
2^2 &= 4 \\
2^3 &= 8 \\
2^4 &= 16 \\
2^5 &= 32 \\
2^6 &= 64 \\
2^7 &= 128 \\
2^8 &= 256 \\
\vdots
\end{aligned}
$$

Estos son los nueve principales pesos de $2$, que son en verdad muy importante sabérselos, pero por ahora, solo necesito que lo entiendas.

> ❗ **Curiosidad:** ¿La secuencia de números te suena? 16 GB, 32 GB, 128 GB, 256 GB... A que si vas a una tienda de discos de memoria, como pendrives o disco duros, te los venden en esta secuencia. Pues es por los pesos de 2.

## Suma de pesos.

Vamos a descomponer el $157$, pero no como lo hicimos al comienzo, sino esta vez en pesos de dos: el número más próximo de la secuencia sería el $128$, que es $2^7$. Lo que le queda a $128$ para llegar a nuestro número son $29$, pero esto no se puede quedar así, por lo que hace falta buscar un nuevo peso cercano: el $16$, que es $2^4$. Nos está sobrando $13$, al que tenemos $8$, que es $2^3$ como el más cercano. Y si seguimos así, nos sobra $5$, tenemos $4$, siendo $2^2$ más $1$, llegamos al final, ya que $1$ es $2^0$ y hemos terminado.

$$
\begin{aligned}
&\quad \mathbf{157}=128[2^7]+\mathbf{29} \\
&\qquad \hspace{2cm} \swarrow \\
&\qquad \mathbf{29}=16[2^4]+\mathbf{13} \\
&\qquad \hspace{2cm} \swarrow \\
&\qquad \quad \mathbf{13}=8[2^3]+\mathbf{5} \\
&\qquad \hspace{2cm} \swarrow \\
&\qquad \qquad \mathbf{5}=4[2^2]+\mathbf{1} \\
&\qquad \hspace{2cm} \swarrow \\
&\qquad \qquad \quad \mathbf{1}=1[2^0]
\end{aligned}
$$

Lo que nos queda es ver la posición de cada peso, que sería viendo su exponente, y aquellos que aparezcan, se pone un 1, si no, 0.

$$2^7 2^6 2^5 2^4 2^3 2^2 2^1 2^0$$
$$1 \hspace{1.5mm} 0 \hspace{1.5mm} 0 \hspace{1.5mm} 1 \hspace{1.5mm} 1 \hspace{1.5mm} 1 \hspace{1.5mm} 0 \hspace{1.5mm} 1$$

Volvimos a tener el $10011101$ del comienzo, que, como demostramos antes, es el $157$. En la realidad, un ordenador que trabaje con 8 unidades, es muy raro: tu ordenador y móvil trabajan a 64, por lo que estar trabajando desde $2^{64}$ no es cuestión. Para eso tenemos la *división sucesiva*.

## División sucesiva.

Este método es mucho más sencillo y solo hace falta saber dividir entre dos.

> 😬 **Experiencia:** Recuerdo en Informática cuando tuvimos que aprender a usar este método y lo que más nos costó fue recordar cómo se dividía obteniendo el resto, y sin tener que usar la calculadora.

Volvamos a nuestro querido $157$ y vamos a irlo dividiendo entre dos hasta que solo quede dividir $1$/$2$. Comenzamos primero dividiendo $157$ entre dos, con lo que tenemos $78$ y de resto $1$. Anotemos el resto, que es importante. El cociente dado, hay que seguirlo trabajando, volviendo a efectuar la división, quedando $39$ de cociente y $0$ de resto. Importante, los ceros hay que también apuntarlos: todos los restos nos van a dar la solución.

$$
\begin{array}{r|ll}
\text{División} & \text{Cociente} & \text{Resto} \\
\hline
157 / 2 & 78 & \mathbf{1} \quad \\
78 / 2 & 39 & \mathbf{0} \quad  \\
39 / 2 & 19 & \mathbf{1} \quad  \\
19 / 2 & 9 & \mathbf{1} \quad  \\
9 / 2 & 4 & \mathbf{1} \quad  \\
4 / 2 & 2 & \mathbf{0} \quad  \\
2 / 2 & 1 & \mathbf{0} \quad  \\
1 / 2 & \mathbf{0} & \mathbf{1} \quad
\end{array}
$$

Para poder ver cuál es el número en binario, solo hay que reordenar los restos y ponerlos del último conseguido al primero: $10011101$, que es nuestro $157$.

> 📒 **Ejercicio:** si en verdad lo entendiste, inténtalo con un número más grande, como el 1612, a ver si logras pasarlo a binario.


# Fracción decimal a binario.

Con estas herramientas somos capaces de pasar cualquier número entero a binario, pero ¿qué pasa con los decimales?

## Suma de pesos.

Esto tiene algo de truco, y es que la suma de pesos funciona igual: para los decimales, en vez de elevar a naturales, hay que hacerlo a enteros negativos.

> ☝🏻🤓 **Aclaración** ¿Por qué se empieza en -1 y no en -0? Muy simple, porque si elevamos cualquier número a -0, este sería la inversa del mismo número elevado a 0, que da 1, y la inversa de 1 es 1, por tanto, esto nos da igual.

$$
\begin{aligned}
2^{-1} &= 0.5 \\
2^{-2} &= 0.25 \\
2^{-3} &= 0.125 \\
2^{-4} &= 0.0625 \\
2^{-5} &= 0.03125 \\
2^{-6} &= 0.015625 \\
2^{-7} &= 0.0078125 \\
2^{-8} &= 0.00390625 \\
\vdots
\end{aligned}
$$

Como me gusta hacerlo todo a base de ejemplos, te voy a dar el $0.6875$. Para la lectura aquí, toma papel y lápiz e intenta convertirlo ayudándote de la tabla superior. La solución te quedaría en $0.1011$. Abajo te pongo el desarrollo, aunque es exactamente igual a como hice antes con los números enteros.

$$
\begin{aligned}

&\quad \mathbf{0.6875} = 0.5[2^{-1}] + \mathbf{0.1875} \\
&\qquad \hspace{3cm} \swarrow \\
&\qquad \quad \mathbf{0.1875} = 0.125[2^{-3}] + \mathbf{0.0625} \\
&\qquad \hspace{3cm} \swarrow \\
&\qquad \qquad \mathbf{0.0625} = 0.0625[2^{-4}] \\

\end{aligned}
$$

## Multiplicación sucesiva.

Ahora tenemos el mismo dilema: si son grandes los decimales, no apetece tener una tabla infinita con casi infinitos números para lograrlo convertir: por eso, como en los enteros teníamos la división sucesiva, aquí tenemos la *multiplicación sucesiva*.

Con saber multiplicar es más que suficiente, pero esta vez, hay un pequeño truco, ya que, lo que nos va a dar el valor convertido, no es lo que sobre, sino la unidad.

Tenemos nuestro ejemplo, el $0.6875$ y lo multiplicamos por $2$, teniendo $1.375$. Separamos lo que tengamos de unidad ($1$) y nos quedamos con los valores a la derecha de la coma ($0.375$), con los que vamos a seguir trabajando. Volviendo a duplicar, conseguimos $0$ y $.75$, y así seguimos hasta llegar al final no tener nada tras la coma.

$$
\begin{array}{r|ll}
\text{Operación} & \text{Entero} & \text{Decimales} \\
\hline
0.6875 \cdot 2 = 1.375 & \mathbf{1} & \mathbf{.375} \\
0.375 \cdot 2 = 0.75 & \mathbf{0} & \mathbf{.75} \\
0.75 \cdot 2 = 1.5 & \mathbf{1} & \mathbf{.5} \\
0.5 \cdot 2 = 1.0 & \mathbf{1} & \mathbf{.0}
\end{array}
$$

> ☝🏻🤓 **Aclaración:** Tanto en división como en multiplicación sucesiva para construir los números de izquierda a derecha, se apuntan los resultados del último al primero; y si se quieren poner de derecha a izquierda, es al revés el apunte, de arriba a abajo.

Y, mirando los valores de abajo hacia arriba, para construirlo de la coma para la derecha, hemos vuelto a conseguir $0.1011$.

---

Con esto ya podemos pasar de base diez (humano) a base dos (máquina), pero si queremos que la máquina sume o reste no la vamos a hacer pasar a binario para poder efectuar el cálculo, por lo que en la próxima publicación, explicaré cómo se hace.

---
---
# Fuentes.

- *Fundamentos de sistemas digitales* – L. Floyd.

---
### Navegación.

- ➡️ **Siguiente:** [Aritmética binaria.](03-aritmetica-binaria.md)
- ⬅️ **Anterior:** [La señal digital.](01-senial-digital.md)
- 🔗 **Publicación en Blogger:** [Decimal y binario.](https://licienciados.blogspot.com/2025/11/decimal-y-binario.html)
