# MCOC2020-P2-G6-E4

#### Output del ejemplo 4:

![alt text](https://github.com/FelipeAravenaR98/MCOC2020-P2-G6-E4/blob/main/reticulado.png?raw=true)

![alt text](https://github.com/FelipeAravenaR98/MCOC2020-P2-G6-E4/blob/main/Tensiones%20caso%201.png?raw=true)

![alt text](https://github.com/FelipeAravenaR98/MCOC2020-P2-G6-E4/blob/main/Tension%20caso%202.png?raw=true)

![alt text](https://github.com/FelipeAravenaR98/MCOC2020-P2-G6-E4/blob/main/Fu%20caso%201.png?raw=true)

![alt text](https://github.com/FelipeAravenaR98/MCOC2020-P2-G6-E4/blob/main/FU%20caso%202.png?raw=true)

Peso :

![alt text](https://github.com/FelipeAravenaR98/MCOC2020-P2-G6-E4/blob/main/Peso.JPG?raw=true)

Como se puede ver el reticulado se debe resideñar segun el caso 2 debido a que al reisar las combinaciones se ven cargas de mayor absoluto en el caso escogido que en el caso 1.



#### Escoja 5 barras interesantes del reticulado (identificadas por sus nodos) y manualmente realice el rediseño, buscando minimizar el peso de la barra y cumplir con FU < 1, pero cerca a 1.0 comparando con los resultados de su programa. 

Barras elegidas para rediseñar

 • 3 [nodos 0-7]

 • 7 [nodos3-10]

 • 20 [nodos 5-8]

 • 21 [nodos 1-5]

 • 22 [nodos 5-9]

 • 23 [nodos 2-5]

A estas barras se les cambio el valor del radio a 10 [cm] y el espesor a 3 [mm] Los cambios que se pueden observa rediseñando estas barras son cambio en las tensiones las cuales siguen cumpliendo el FU esto se debe al cambio de peso y de la geometria lo que produce cambios en la inercia que tambien afecta las tensiones de la estructura. Se observa un aumento en el FU pero es despreciable por lo que no se logra apreciar en la simulacion.

#### Explique en detalle su función de rediseño de cada barra. Si existen supuestos importantes, declarelos ahora. 
 * En primer lugar, el objetivo de la función de rediseño de cada barra,  fue calcular el valor más optimo para el radio y espesor, logrando así, que el F.U tienda a 1.
  * En segundo lugar, el supuesto más importante que se realizo fue que F.U debe ser menor o igual a 1. Con esto se aseguró que el puente, fuese una estructura segura y por lo tanto se encuentre dentro de los rangos óptimos de diseño. 
  * Cabe destacar, que a pesar de que las barras a rediseñar fueron previamente escogidas, se tiene toda la libertar que ver que hacer con la fuerza, es decir, utilizar las combinaciones de carga a elección del consumidor. 
  * Lo que realizó la función rediseñar en nuestro caso, fue encontrar un coeficiente(variable según el tipo de problema), el cual se amplificó por el radio y el espesor para así llegar al diseño estructural optimo del puente. 
  * Finalmente, la importancia de la función rediseñar es imprescindible para el problema, ya que de esta depende que los valores de los parámetros tengan sentido.
  
#### Mostrar los nuevos factores de utilización, fuerzas en las barras y deformada para cada combinación de carga. Para esto, Graficando todo lo pedido y explicando sus criterios de rediseño. 
Al rediseñar se obtiene el peso: 

![alt text](https://github.com/FelipeAravenaR98/MCOC2020-P2-G6-E4/blob/main/Peso%20redise%C3%B1o%20funcion.JPG?raw=true)

![alt text](https://github.com/FelipeAravenaR98/MCOC2020-P2-G6-E4/blob/main/Tensiones%20Redise%C3%B1o%20caso%202.png?raw=true)

![alt text](https://github.com/FelipeAravenaR98/MCOC2020-P2-G6-E4/blob/main/FU%20redise%C3%B1o%20caso%202.png?raw=true)

![alt text](https://github.com/FelipeAravenaR98/MCOC2020-P2-G6-E4/blob/main/Deformada%20redise%C3%B1o.png?raw=true)


#### ¿Cual es el desplazamiento vertical máximo en los nodos del tablero del reticulado antes y después de los cambios?

Antes de los cambios:

![alt text](https://github.com/FelipeAravenaR98/MCOC2020-P2-G6-E4/blob/main/Desplazamiento%20antes.JPG?raw=true)

Despues de los cambios:

![alt text](https://github.com/FelipeAravenaR98/MCOC2020-P2-G6-E4/blob/main/Desplazamientos%20nodos%20redise%C3%B1o%20funcion.JPG?raw=true)

Distancias en metros.

#### Comente respecto de la nueva distribución de FU del reticulado y el peso del mismo. ¿Que cambios globales se pueden hacer para mejorar aún más el costo (peso del acero) del mismo? 


Se modificaron las barras 3, 7 , 20  21, 22, 23 a un radio de 10 [cm] y un espesor de 3 [mm] 

A partir del rediseño realizado se puede observar que el FU para los elementos rediseñados no experimenta ningún cambio esto se debe a que las propiedades geométricas modificadas siguen cumpliendo con las solicitaciones de cargas sometidas a los elementos modificados. Sin embargo, estas modificaciones si disminuyeron el peso de la estructura de un valor de 24197 [kg] a 11856 [kg] lo que implica una optimización en el peso de la estructura. Al reducir el peso y teniendo el mismo comportamiento estructural se están economizando recursos con los cuales se desarrollará una estructura la cual tendrá un menor costo. Observando los resultados entregados se propone eliminar dos barras 0-7 y 3-10 ya que estas no influyen en el FU y además poseen tensiones nulas lo que no afectaría quitarlas del diseño para así reducir mas el peso y por ende el costo de la estructura.
