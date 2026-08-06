---
titulo: "P07: Complemento a 1"
fecha: "REVISIÓN"
autor: "Lulo"

progreso: 50

nivel: "Básico"
tiempo: "~5 min"
etiquetas: [Binario, Conversión de bases]
imagen: "pics/mini_elect.jpg"

anterior: "../06-representacion-con-signo/"
siguiente: "../08-complemento-a2/"

enlace_ejercicios: 
enlace_simulaciones: 

descripcion: 
destacado:

lecturas_previas:
  - titulo: "P06: Representación con signo"
    nivel: "Básico"
    tiempo: "~5 min"
    fecha: "REVISIÓN"
    autor: "Lulo"
    url: "../06-representacion-con-signo/"
---
> ✍🏻 **Autor:** Lulo  
> 📚 **Nivel:** Básico  
> ⌛ **Tiempo lectura:** 5 min  
> 🧮 **Matemáticas:** Básicas  

Para poder representar valores negativos nos servía con el [signo y magnitud](06-representacion-con-signo.md), pero teniendo una doble representación del $0$. Pero, ¿esta es la única manera de representar los negativos? No, pues existen dos más, que son mucho más comunes que esta.

# Diferencia con signo-magnitud

En esta base también nos ayudamos del bit de signo, por lo que el primer bit será un $0$ si es positivo y $1$ si es negativo. ¿Cuál es la diferencia? Que cuando queremos representar un valor negativo, no lo hacemos con binario natural, sino "invertimos" esa parte.

Tenemos el $12$, pero lo vamos a hacer en complemento a1 en $8$ bits: primero el bit de signo, $0$, luego tres bits que nos hacen falta de relleno y por último el valor en binario natural, obteniendo $00001100$. Para hacer el $-12$, vamos a tomar su representación positiva e invertirla: cada cero se cambia por un uno y cada uno por un cero. De esta forma nos queda: $11110011$. Es en verdad bastante sencillo.

| **Decimal** | **Binario natural** | **Complemento a 1** |
| :---: | :---: | :---: |
| -12 | -1100 | 11110011 |

## Conversión a decimal

Para pasarlo a decimal es solo repetir todo el proceso al revés: si el bit de signo es $0$, solo hay que convertir el resto del número como si de binario natural se tratara; en el caso de tener un signo $1$, que quiere decir que es negativo, se invierte todo el número y se convierte a binario natural.

> ❗ **Curiosidad:** Aunque parezca un poco raro el complemento a 1, este método era el que se usaba en los primeros ordenadores, y hoy en día se sigue usando para ciertos protocolos de internet.

# Limitaciones

En este caso tenemos un mismo rango de valores que en la representación de magnitud y signo, que es de $-(2^{n-1}-1)$ a $2^{n-1}-1$. Esto es debido a que tenemos el mismo problema de antes, que el $0$ tiene doble representación.

$$0 == 00000000 == 11111111$$

---

Si hemos entendido el signo y magnitud, el complemento a 1 es igual de sencillo: si es negativo, darle la vuelta. Y aún tenemos el problema de la doble representación del $0$, pero tiene solución, y se llama *complemento a 2*, que lo veremos en la siguiente publicación.

---
