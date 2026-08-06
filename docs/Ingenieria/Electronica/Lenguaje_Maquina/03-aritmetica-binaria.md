---
titulo: "P03: Aritmética binaria"
fecha: REVISIÓN
autor: Lulo

progreso: 50

nivel: Fácil
tiempo: ~10 mins
etiquetas: [Binario, Aritmética]
imagen: pics/mini_elect.jpg

anterior: "../02-decimal-y-binario/"
siguiente: "../04-octal-hexadecimal-y-bcd/"

enlace_ejercicios: 
enlace_simulaciones: 

descripcion: 
destacado:

lecturas_previas:
  - titulo: "P02: Decimal y binario"
    nivel: "Fácil"
    tiempo: "20 min"
    fecha: "EN REVISIÓN"
    autor: "Lulo"
    url: "../02-decimal-y-binario/"

---

> ✍🏻 **Autor:** Lulo  
> 📚 **Nivel:** Fácil  
> ⌛ **Tiempo lectura:** ~10 min  
> 🧮 **Matemáticas:** Básicas   

Tras haber visto la relación que existe entre el [decimal y el binario](https://github.com/LuloGB/liCiencia2/blob/pre-publicaciones-electronica/Ingenieria/Electronica/Lenguaje_Maquina/02-decimal-y-binario.md), queda una cosa muy importante pendiente, siendo el cómo se trabaja de forma aritmética la base binaria.

# Suma

La principal y más básica función aritmética que usan los ordenadores es la suma, que no se diferencia demasiado cuando se cambia de una base a otra. Para ello, hay que tener en cuenta los dígitos en la que uno se encuentra. En la base binaria, tenemos dos números, que son el $1$ y el $0$. De los conocimiento básicos de suma sabemos que en caso que cualquier número que se sume $0$ no se cambia y cuando se le suma $1$ incrementa en $1$ es más que suficiente como para entender cómo funciona. En el caso que efectuemos la adición y como resultado de un número superior a $1$, lo que se hace es colocar un $1$ a la izquierda y un $0$ en la posición del antiguo valor. Este $1$ que se "desplaza" se le conoce como **acarreo**. Para entender mejor cómo es la suma, se puede ver más claro en el [Ejemplo 1](#ej1).

<div id="ej1"></div>

$$
\begin{aligned}
0+0&=0 \\
0+1&=1 \\
1+0&=1 \\
1+1&=10
\end{aligned} \tag{Ej. 1}
$$

# Resta

A parte de la suma, también existen otras operaciones aritméticas muy usadas, que son la resta, además que tiene un mismo comportamiento, que es cuando se opera con $0$ no hay cambios y cuando se opera con $1$ se reduce una posición, mostrado de manera más cómoda en el [Ejemplo 2](#ej2).

<div id="ej2"></div>

$$
\begin{aligned}
0-0&=0 \\
1-1&=0 \\
1-0&=1 \\
10-1&=1
\end{aligned} \tag{Ej. 2}
$$

En el caso de la suma existe el acarreo, y en su contraposición para la resta se tiene el **accarreo negativo**, que en vez de poner un $1$ a la derecha, lo que se hace es desplazar el $1$ una posición a la izquierda.

# Multiplicación

La multiplicación binaria es el cálculo aritmético más empleado de esta base. Al igual que cuando se trabaja con "verdadero" y "falso", la multiplicación binaria presenta un comportamiento muy parecido: cuando se multiplica por "falso", en nuestra aplicación $0$, siempre es "falso" ($0$), y cuando se multiplican dos veces "verdadero", para nuestro caso $1$, o dos veces "falso" ($0$), siempre termina dando "verdadero" ($1$). La aplicación numérica se muestra con el [Ejemplo 3](#ej3).

> ❗ **Curiosidad:** La multiplicación es bastante conocida como lógica de boole, basada en los trabajos de **George Boole**, aplicados sus estudios sobre todo en el campo estadístico.

<div id="ej3"></div>

$$
\begin{aligned}
0·0&=0 \\
0·1&=0 \\
1·0&=0 \\
1·1&=1
\end{aligned} \tag{Ej. 3}
$$

> 😬 **Experiencia:** Cuando empecé a trabjar electrónica llegué sin saber cómo funcionaba la multiplicación y actualmente estoy harto de ella.

# División

El dividir es algo más complicado que en el resto de bases, aunque normalmente se realiza primero una conversión de binario a decimal, se efectúa la división y el resultado es devuelto otra vez en binario. Pero, como es difícil de explicar de manera desarrollada, voy a proporcionar un ejemplo, como el [Ejemplo 4](#ej4): $110 \div 11$. Se empieza por comparar los dos primeros valores, de izquierda a derecha, de $110$, que es $11$, y las veces que hace falta multiplicar el denominador, $11$, para que sea igual es por $1$. Esto resulta en $00$, y, para este valor, sería por $0$. Entonces, de cociente termina valiendo $10$ y de resto $0$.

<div id="ej4"></div>

$$
\begin{array}{r|ll}
\text{Operación} & \text{Cociente} & \text{resto} \\
\hline
110 \div 11 & \mathbf{10} & \mathbf{0} \quad \\
\end{array} \tag{Ej. 4}
$$

> ❗ **Curiosidad:** Cuando ya hablamos de ordenadores, ellos no realizan los cálculos como nosotros hacemos: si necesitamos multiplicar, multiplicamos directamente, o dividir, pues recurrimos a la división. Las máquinas lo hacen enormemente más resumido: <u>todo lo hacen con la suma</u>.

---

A parte de efectuar cálculos, para que los humanos lleguen a entender mejor los resultados que no sea traduciendo solo a la base decimal, existen otras herramientas más cómodas y efectivas, de entre ellas bases como la **hexadecimal** y la **octal**, que profundizaremos en futuras publicaciones.

---
