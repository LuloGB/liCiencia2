---
titulo: "P05: Bit, byte y nibble"
fecha: "REVISIÓN"
autor: "Lulo"

progreso: 50

nivel: "Básico"
tiempo: "~5 min"
etiquetas: [Binario, Teoría y conceptos]
imagen: "pics/mini_elect.jpg"

anterior: "../04-octal-hexadecimal-y-bcd/"
siguiente: "../06-representacion-con-signo/"

enlace_ejercicios: 
enlace_simulaciones: 

descripcion: 
destacado:

lecturas_previas:
  - titulo: "P02: Decimal y binario"
    nivel: "Fácil"
    tiempo: "20 min"
    fecha: "26-10-2026"
    autor: "Lulo"
    url: "../02-decimal-y-binario/"
---

> ✍🏻 **Autor:** Lulo  
> 📚 **Nivel:** Básico  
> ⌛ **Tiempo lectura:** ~5 min  
> 🧮 **Matemáticas:** Nulas  

{{ mostrar_etiquetas() }}

Lo de hoy es un poco de teoría y vamos a explicar algunos de los conceptos que más vamos a usar. Además, estás harto de escucharlos, pero nunca has sabido sus significados.

# Bit

Recordemos cuando dimos en el inicio del todo lo que es una [señal digital](01-senial-digital.md): una alternancia de unos y ceros. Este estado, ya se alto o bajo, representa la cantidad mínima de información que se puede almacenar, y se llama *bit* /ˈbɪt/.

Si has estado atento, en alguna publicación de seguro que se me ha escapado esa palabra para referirme a los dígitos binarios, que, cada uno de ellos es un bit y en su conjunto forman el dato que ora queremos almacenar, ora queremos trabajar.

# Nibble

Los bits se pueden agrupar, y el primer grupo que nos encontramos son los *nibbles* /ˈnɪbl̩/. Estos son grupos conformados por cuatro bits, desde $0000$ hasta $1111$, y estos son los dígitos máximo y mínimo de la base [hexadecimal](04-octal-hexadecimal-y-bcd.md). Entonces, de esta forma, cada número en hexadecimal es un nibble de información.

> 😬 **Experiencia:** Este término no lo conocí hasta cuando empecé a estudiar el d (uno de los libros que estoy usando actualmente). Es un término que normalmente se omite, pero es interesante conocerlo.

# Byte

Giga Byte, Mega Byte, Tera Byte... Estas palabras las llegamos a usar en nuestro día a día, pero generalmente no conocemos su significado: al igual que Kilo es $10^3$, Mega es $10^6$, Giga $10^9$ y Tera $10^{12}$; luego, el *byte* /baɪt/ corresponde a la unidad, que son dos grupos de nibble u ocho bits de información.

A este valor se le da tanta importancia porque es la unidad mínima para poder almacenar tanto todo tipo de datos como hasta caracteres alfabéticos, además que los primeros ordenadores trabajaban con este tamaño de datos.

## Word

¿De verdad mi ordenador trabaja a 8 bits, osea, un byte? No. No estamos en los años 70. La tecnología ha ido avanzando enormemente al punto que un microcontrolador de 16 bits (2 bytes) se considera muy limitado, por lo que lo más normal es encontrar de 32 y 64 bits (en este último caso, tu móvil u ordenador). Dependiendo de lo compleja que sean las instrucciones, un microprocesador puede tener un tamaño de *palabra* (*word* /wɝːd/) más grande o más pequeño.

> ❗ **Curiosidad:** Existen superordenadores que ya trabajan con 128 bits, que eso equivale a poder almacenar $2^{128}$ instrucciones. En este caso, más no significa mejor: consumen más energía, ocupan más espacio... Esto es solo para ordenadores experimentales.

---

Ya sabemos usar el binario, entendemos cómo se pueden agrupar y cómo se trabaja, pero hay un problema al que no nos hemos enfrentado directamente y es ¿cómo representamos valores que son negativos? Si solo tenemos los símbolos 1 y 0, no podemos usar el "-". Esto lo abarcaremos en la siguiente publicación.

---
