# Respuestas TP5-CSP

## Describir en detalle una formulación CSP para el Sudoku.

**Variables**: Cada posicion en el tablero 
**Dominios**: {1,2,3,4,5,6,7,8,9}
**Restricciones**: 
- Todos los valores en una fila deben ser distintos
- Todos los valores en horizontal deben ser distintos
- Todos los valores dentro de cada submatriz deben ser distintos

## Utilizar el algoritmo AC-3 para demostrar que la arco consistencia puede detectar la inconsistencia de la asignación parcial {WA=red, V=blue} para el problema del colorar el mapa de Australia (Figura 5.1 AIMA 2da edición).

- Comenzamos teniendo el estado inicial (Sin asignaciones)
- Se elije el color rojo para WA
- Se verifica la consistencia de arco
- Se elije el color azul para V
- Se verifica la consistencia de arco
	- **WA** -> Rojo
	- **NT** -> Azul
	- **Q** -> -
	- **NSW** -> Rojo
	- **V** -> Azul
	- **SA** -> Verde
	- **T** -> Rojo | Azul | Verde
 
Luego de verificar la consistencia de arco vemos que el dominio de Q quedo vacio. Por lo tanto es inconsistente


## Cual es la complejidad en el peor caso cuando se ejecuta AC-3 en un árbol estructurado CSP. (i.e. Cuando el grafo de restricciones forma un árbol: cualquiera dos variables están relacionadas por a lo sumo un camino).

O(nd^2)

## Demostrar la correctitud del algoritmo CSP para árboles estructurados (sección 5.4, p. 172 AIMA 2da edicion). Para ello, demostrar: 
##             a. Que para un CSP cuyo grafo de restricciones es un árbol, 2-consistencia (consistencia de arco) implica n-consistencia (siendo n número total de variables)
##             b. Argumentar por qué lo demostrado en a es suficiente.

- **a**: Cualquier CSP estructurado por árbol puede resolverse en tiempo lineal en el número de variables. El algoritmo tiene los siguientes pasos:
1. Elija cualquier variable como la raíz del árbol, y ordene las variables desde la raíz a las hojas de tal modo que el padre de cada nodo en el árbol lo precede en el ordenamiento. Etiquetar las variables X1…, Xn en orden. Ahora, cada variable excepto la raíz tiene exactamente una variable padre.
2. Para j desde n hasta 2, aplicar la consistencia de arco al arco (Xi, Xj), donde Xi es el padre de Xj, quitando los valores del DOMINIO[Xi] que sea necesario.
3. Para j desde 1 a n, asigne cualquier valor para Xj consistente con el valor asignado para Xi, donde Xi es el padre de Xj.

- **b**: Primero, después del paso 2 el PSR es directamente arco-consistente, entonces la asignación de valores en el paso 3 no requiere ninguna vuelta atrás. Segundo, aplicando la comprobación de consistencia de arco en orden inverso en el paso 2, el algoritmo asegura que cualquier valor suprimido no puede poner en peligro la consistencia de arcos que ya han sido tratados.

Finalmente, queda demostrada la correctitud del algoritmo CSP.