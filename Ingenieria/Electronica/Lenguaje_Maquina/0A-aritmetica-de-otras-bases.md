# Aritmética de otras bases.

> ⚠️ **Cuidado:** Esta publicación es una expansión de [Octal, hexadecimal y BCD.](04-octal-hexadecimal-y-bcd.md)

> ✍🏻 **Autor:** Lulo.  
> 📚 **Nivel:** Complementario.  
> ⌛ **Tiempo lectura:** AÑADIR---------------------  
> 📖 **Lectura previa:** [Decimal y binario.](02-decimal-y-binario.md) [Aritmética binaria.](03-aritmetica-binaria.md) [Octal, hexadecimal y BCD.](04-octal-hexadecimal-y-bcd.md) [Complemento a 1.](07-complemento-a1.md) [Complemento a 2.](08-complemento-a2.md)  
> 🧮 **Matemáticas:** Medio.  
> 🏷️ **Etiquetas:** `Hexadecimal`, `Aritmética`, `Complementarios`.

Teniendo en mente las diferentes bases del [hexadecimal, el octal y el BCD](04-octal-hexadecimal-y-bcd.md), queda aún hablar de cómo se trabaja con ellos aritméticamente. También al final hablaré de la suma de números de distinto signo de los complementos [a 1](07-complemento-a1.md) y [a 2](08-complemento-a2.md).

# Aritmética hexadecimal.

## Suma hexadecimal.

Es muy parecida a la decimal pero teniendo en cuenta que tenemos los números de $A$ a $F$, que será trabajar con su equivalencia en decimal. Supongamos $2A$ y $1C$, que los vamos a sumar. Realizamos como primer paso las equivalencia de $A$ y $C$ a decimal, que son $10$ y $12$: si los sumamos los queda $22$, pero es mayor a $15$, que es el valor máximo alcanzable. Entonces, tenemos que restarle al resultado este número, resultando $7$: ya tenemos nuestro primer dígito, con un acarreo al siguiente. Para el segundo valor, tenemos $2$, $1$ y otro $1$, debido a que antes cuando sumamos $A$ y $C$ tuvimos un desbordamiento: entonces, la suma nos queda en $4$, que sí es menor a $15$, por lo que no hay nuevo acarreo, y de resultado queda $47$.

$$2A + 1C = (20 + 10) + (A(10) + C(12)) = 30 + (10 + 7) = 47$$

## Resta hexadecimal.

pag 88




hablar del problema del hexadecimal, que no tiene signo en ordenador y que se usa en hexadecimal en rango 2^n mientras que el binario que representa es en a2




### Hexadecimal en complemento a 2.

explicar los tres métodos de hexadecimal a a2





# Aritmética octal.

En este base, no es tan enrevesado, ya que trabajamos con valores que van de $0$ a $7$, por lo que cuando efectuamos sumas o restas, realizamos los acarreos necesarios. Tenemos el $14$, y le restamos $6$: sabemos que $14$, para llegar a nueve, tenemos que quitarle cinco, por lo que pasamos a tener $9 - 1$, pero el nueve está prohibido en esta base, así que pasamos a $7 - 1$, que $7$ es el valor máximo. Entonces, efectuamos la última resta y nos queda $6$.

$$14 - 6 = (7 + 5) - 6 = (7 + 0) - 1 = 7 - 1 = 6$$

En este caso, no tenemos que tener en cuenta el signo o temas de usar el complemento a 2 como en el hexadecimal porque el octal se usa escensialmente en el papel: los ordenadores usan binario y para simplificar se usa directamente el hexadecimal, sin pasar por el octal.

# Aritmética BCD.

solo hablar de la suma



# Aritmética de los complementos

## Complemento a 1.


explicar resta y suma


## Complemento a 2.

solo decir que exactamente igual al 1 pero quitando el paso final de añadirle 1



---




---
---

# Fuentes.

- *Fundamentos de sistemas digitales* – L. Floyd.

---

### Navegación.

- ➡️ **Siguiente:** [Números en coma flotante.](09-numeros-en-coma-flotante.md)
- ⬅️ **Anterior:** [Octal, hexadecimal y bcd.](04-octal-hexadecimal-y-bcd.md)
- 🔗 **Publicación en Blogger:** [Aritmética de otras bases.](#)