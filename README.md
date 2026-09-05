# Actividad 2

# Selección de personal estricta

Esta actividad utiliza un algoritmo genético para formar un equipo de desarrollo a partir de 12 candidatos. 
Cada candidato tiene una puntuación de habilidad técnica y está representado por una posición dentro de un cromosoma binario. 
Un bit con valor 1 indica que la persona fue seleccionada y un bit con valor 0 indica que no fue seleccionada.

El objetivo es obtener el equipo con la mayor habilidad técnica posible. La restricción indica que el equipo debe estar formado por exactamente cinco personas.

# Aptitud y penalización

La función de aptitud primero cuenta los bits encendidos. Cuando el cromosoma tiene exactamente cinco bits con valor 1, la aptitud corresponde a la suma de las habilidades de las personas seleccionadas. Si la cantidad es diferente de cinco, se utiliza la penalización:

-1000 - (100 * diferencia con respecto a cinco)


Por ejemplo, un cromosoma que selecciona seis personas recibe una aptitud de -1100. Esta penalización hace que los individuos que incumplen la restricción tengan pocas posibilidades de ganar la selección por torneo.

# Flujo 

1 Se genera una población aleatoria de 40 cromosomas.
2 Cada cromosoma se decodifica para conocer las personas seleccionadas.
3 Se calcula la aptitud y se penalizan los equipos que no tienen cinco integrantes.
4 Se seleccionan padres por torneo.
5 Se aplican cruzamiento de un punto y mutación.
6 El proceso se repite durante 30 generaciones.
7 Se muestra el mejor equipo encontrado.

### Resultados

En la primera generación solamente 9 de los 40 individuos eran válidos. Debido a la penalización los equipos de cinco personas fueron aumentando y en la generación 10 los 40 individuos eran válidos. 
El mejor resultado obtenido con la semilla utilizada fue el genotipo 101010001010, que representa a Ana, Carla, Elena, Isabel y Karen. La habilidad técnica total fue de 452 puntos.


# Actividad 3

# Cruzamiento de dos puntos

Esta actividad modifica el operador de cruzamiento de un punto utilizado en el ejemplo de clase. En lugar de escoger un solo índice, la función cruzar_dos_puntos selecciona dos índices aleatorios. Los hijos conservan los extremos de sus padres e intercambian el segmento central.

El operador se incorporó al flujo completo del algoritmo genético y se utilizó con el ejemplo visto en clase: maximizar la función f(x) = x² para valores enteros entre 0 y 31. Cada valor se representa con un cromosoma binario de cinco bits.

## Ejemplo del cruzamiento

Con la semilla establecida, el ejemplo utiliza los puntos 1 y 3:


Padre 1: 11100
Padre 2: 00011
Hijo 1:  10000
Hijo 2:  01111


Los genes ubicados entre los dos puntos de corte son los que cambian de padre.

# Flujo

1 Se genera una población aleatoria de cromosomas de cinco bits.
2 Los cromosomas se convierten a números enteros.
3 La aptitud se calcula con f(x) = x².
4 Los padres se seleccionan por ruleta.
5 Se aplica el cruzamiento de dos puntos y después la mutación.
6 El proceso se repite durante 10 generaciones.

# Resultados

El algoritmo encontró el genotipo 11111, que corresponde al número 31. Su aptitud es `31² = 961`, que es el valor máximo posible dentro del espacio de búsqueda. El resultado también demuestra que el operador de dos puntos funciona dentro del ciclo completo del algoritmo genético.

