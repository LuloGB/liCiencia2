# Representación con signo.

> ✍🏻 **Autor:** Lulo.  
> 📚 **Nivel:** Básico.  
> ⌛ **Tiempo lectura:**  min.  
> 📖 **Lectura previa:** [Decimal y binario.](02-decimal-y-binario.md) [Aritmética binaria.](03-aritmetica-binaria.md) [Bit, byte y nibble](05-bit-byte-y-nibble.md)  
> 🧮 **Matemáticas:** Básicas.  
> 🏷️ **Etiquetas:** `Binario`, `Aritmética`, `Conversión de bases`.

En el mundo de la electrónica existen diferentes tipos de binarios. El usar uno u otro depende de la estructura del microprocesador, la capacidad de memoria, la potencia y, en general, para qué lo vamos a usar. En las siguientes publicaciones vamos a ver por qué existen varios binarios.

# Problema del signo.

Hasta el momento solo hemos dado [binario natural](02-decimal-y-binario.md): con él podemos representar con comodidad todos los números mayores de cero, incluído este. Pero nos ha surgido un problema y es cómo representar valores menores a cero. Si lo hacemos a lo bruto, podemos añadir solo un "-" al comienzo: que $-6$ sea $-110$ en binario. Si volvemos al funcionamiento del binario, esto no tiene sentido, debido a que las máquinas no pueden representar valores diferentes a 1 y 0 (alto y bajo, si lo pasamos a niveles de tensión).  Para solucionar este inconveniente, surge algo llamado *bit de signo*.

# Signo-magnitud.
REVISAR

Cuando nosotros queremos representar $6$. Para esto, hacen falta tres bits, porque es $110$ en binario. Ahora lo volvemos a intentar con el $-6$, pero esta vez ayudándonos del bit de signo: este bit es un valor que se añade al inicio del valor y que representa si es positivo (0) o negativo (1), quedando $1101$.

Aquí empiezan a surgir muchas dudas: ¿pero el $1101$ no es $13$ en binario? Eso sería si estuviéramos en binario natural, pero ahora estamos en signo-magnitud de 4 bits (importante decir con cuántos bits trabajamos).



## Limitaciones.






HABLAR DE OVERFLOW PAG 76

---

---
---

### Navegación.

- ➡️ **Siguiente:** [Complemento a1.](#)
- ⬅️ **Anterior:** [Bit, byte y nibble.](05-bit-byte-y-nibble.md)
- 🔗 **Publicación en Blogger:** [Representación con signo.]()