# Reporte TP3

## a
El objetivo es, dado un punto de inicio y un punto final, mostrar el camino que se toma para ir desde el inicio al final. Esto va a ocurrir en un entorno de 100 por 100 con obstáculos generados aleatoriamente. 

Primero creo el ambiente. Para esto armo una función **createMaze()** la cual recibe como parámetro el numero de obstáculos y devuelve un ambiente de 100 por 100 con dicha cantidad de obstáculos posicionados aleatoriamente.

Luego se colocan el punto inicial y el punto final. Finalmente se corre el algoritmo A* el cual devuelve, de ser posible, el mejor camino para ir del punto inicial al punto final evitando los obstáculos. En caso de no existir dicho camino devolvera **None**.

## b
Tomamos **f(n) = g(n) + h(n)**:
	* **g(n):** costo de la ruta desde el nodo raiz hasta el nodo n.
	* **h(n):** costo desde el nodo n al nodo objetivo.




