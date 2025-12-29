# Señal Continua y discreta.
El elemento más básico e importante en la electrónica es el *electrón*. Este, al desplazarse por los diferentes elementos hace que surja la *intensidad*, pero para que exista este movimiento tenemos algo que llamaremos  **voltaje** -o **tensión**, que usaremos indistintamente: esta puede ser grande, pequeña o negativa. Esta variación, si la medimos a lo largo del tiempo, conseguiremos una *amplitud*. Si esta amplitud varía, conseguimos una *señal continua* (*Fig 1.*), que es la base de la electrónica analógica.
El trabajar este tipo de señales es muy costoso: son necesarios grandes aparatos que generalmente son difíciles de usar. Esto surge por el hecho que trabajamos con "la señal completa". Una solución es medir cada cierto tiempo -llamado *periodo*- la tensión que hay en ese instante. De esta forma tenemos una **señal discreta**, que son las que usan nuestros ordenadores.

<div align="center">
  <img src="" alt="Señal continua" width="400">
  <br>
  <sub>*Fig 1. Señal continua.*</sub>
</div>

Imaginemos una señal como la de la figura 1. En el eje vertical tenemos <u>la amplitud</u>, que llamaremos *V*, y en el horizontal el tiempo *t*. Cuando va pasando el tiempo, vemos que la señal ha ido cambiando su valor de amplitud: es porque es una señal variable. Vamos a *discretizarla*.

<div align="center">
  <img src="" alt="Señal discretizada" width="400">
  <br>
  <sub>*Fig 2. Señal discretizada sobre Señal conitnua.*</sub>
</div>

Tomamos un periodo *T*, que es una cantidad de tiempo fija, y medimos V cada dicho T. Esto genera unos puntos que, si los unimos con rectas horizontales y verticales, nos queda algo parecido a una escalera (Fig 2.), pero que es parecida a la señal original. De esta forma, hemos *digitalizado* una señal: así es como piensan en verdad los ordenadores.

---

# El 0 y el 1.

Vamos a simplificarlo un poco más y vamos a usar solo dos valores: voltaje bajo $V_L$ y voltaje alto $V_H$. Montamos un circuito simple, de solo una fuente y un bombillo (Fig 3.). Vamos a imaginarnos que la fuente, una simple pila, da $V_H$ cuando el cable está conectado, y cuando no está conectado, como no existe un circuito cerrado, pues da $V_L$.

<div align="center">
  <img src="" alt="Ejemplo bombillos" width="400">
  <br>
  <sub>*Fig 3. Ejemplo con bombillos. Izquierda en $V_H$. Derecha en $V_L$.*</sub>
</div>

Si lo volvemos aún más simple, podemos pasar de un bombillo a un número, que sería el equivalente a que esté encendido a un 1, y si está apagado a un 0. Conceptualmente, así funciona el binario en lo ordenadores.
Aunque vamos a ser sinceros, los ordenadores no entienden de números, solo de tensiones, que sus <u>valores típicos son de 5V o 3.3V a 0V</u>.

<div align="center">
  <img src="" alt="Rangos de tensión" width="400">
  <br>
  <sub>*Fig 4. Rangos de tensión de una señal de ordenador.*</sub>
</div>

En la figura 4 tenemos una representación en la que dividimos voltaje alto y bajo. Como no son señales perfectas, tenemos un rango, comprendido en máximo y mínimo. Con este rango otenemos la franja de *High* /ha🇮/ y *Low* /ləΩ/, alto y bajo, respectivamente. En medio, entre $V_{\text{H(min)}}$ y $V_{\text{L(max)}}$ surge algo llamado incertidumbre, que es lo bueno de las señales digitales: como estamos midiendo solo entre algo y bajo, todo el *ruido*, que es basura que porta la señal, es "comido" por esta incertidumbre, eliminando posibles problemas.

---

# Señal binaria.

De esta forma tenemos defininda nuestra señal binaria, pero es angosto trabajar de esta forma, por lo que vamos a verlo de manera gráfica.

## Señal ideal.

Recordemos la señal discretizada, la de los escaloncitos. Teniendo High y Low vamos a hacer que la señal alterne entre estos dos valores. Si tomamos una foto de uno de estos instantes tenemos una especie de rectángulo. Vamos a ver sus partes.

<div align="center">
  <img src="" alt="Señal Ideal" width="400">
  <br>
  <sub>*Fig 5. Partes de una señal ideal.*</sub>
</div>

Con el ejemplo de la figura 5 podemos ver todo: viendo de izquierda a derecha partimos del valor Low y, en un instante $t$, saltamos a High. A este salto se le da el nombre de *flanco de subida*. Si seguimos, vemos otro paso de High a Low, que también es un flanco, pero esta vez *de bajada*. Con esto, ya tenemos una señal digital.

## Señal real.

En la realidad, no es así. Para los curiosos, aquí les vengo a contar la verdad: las señales digitales no son así en absoluto, ya que presentan muchas más partes y se tienen otros muchos factores en cuenta.

<div align="center">
  <img src="" alt="Señal Real" width="400">
  <br>
  <sub>*Fig 6. Partes de una señal real.*</sub>
</div>

Vamos a volver a la señal ideal, y supongamos que pasamos de bajo a alto. Ahora sucede algo distinto: la señal asciende muy lentamente. Esto es porque existen efectos capacitivos que no teníamos en cuenta antes. Poco a poco va subiendo y cuando ha pasado el 90% del total de la señal, podemos decir que estamos en High. De lo que ha tarado de pasar del 10% al 90 se le llama *tiempo de subida*. 
Cuando llega a alta, no se queda quieto de inmediato, sino aparece una "inercia" que le hace continuar un poco más. El punto más alto se le llama *Sobreimpulso*. Luego, como también hay otros efectos, ocurre una oscilación, que es el *rizado* (a tener en cuenta que siempre aparece cuando se cambia de un estado a otro, ya sea de alto a bajo como de bajo a alto). Por último, la señal se estabiliza y permanece en ese estado.
Por último, al igual que pasa con el flanco de subida que hay un tiempo de subida, en el flanco de bajada hay un *tiempo de bajada*. Pero, ¿y el tiempo del pulso? Sencillo: es lo que ha tardado de pasar del 50% de un flanco a otro flanco, denominado *ancho de pulso*.

---

Con esto ya tenemos lo básico para entender lo que es una señal digital, pero ahora surge un inconveniente: ¿con qué herramienta matemática nos podemos ayudar? El binario es la solución para esto.

---
---
# Fuentes.

- *Fundamentos de sistemas digitales* – L. Floyd.

<hr>
<table width="100%" style="border: none;">
  <tr>
    <td width="50%" align="left" style="border: none;">
      <a href="https://github.com/LuloGB/liCiencia2/tree/main/Ingenieria/Electronica/Lenguaje_Maquina">
        <strong>⬅️ Atrás</strong><br>
        <small>Volver al inicio</small>
      </a>
    </td>
    <td width="50%" align="right" style="border: none;">
      <a href="">
        <strong>Siguiente ➡️</strong><br>
        <small>Decimal y binario.</small>
      </a>
    </td>
  </tr>
</table>