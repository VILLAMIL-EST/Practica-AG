## Ejercicio 4: Análisis de Resultados

### ¿Cómo afectó la penalización fuerte a la supervivencia de las soluciones?

En el Ejercicio 1, implementamos una penalización fuerte de **10**. Si el costo total superaba el presupuesto de $100, significaba que cada dólar excedente restaba $10 al retorno total.

**Generación tras generación:**
1.  **Generaciones iniciales:** Muchas soluciones se pasaban del presupuesto y, por consiguiente, recibían una penalización enorme, lo que las hacía "inviables" (es decir, tenían un **fitness muy bajo**). Por consecuencia, **desaparecían rápido** de la población.
2.  **Generaciones intermedias:** El algoritmo aprendió a evitar combinaciones que excedían el presupuesto. En vez de eso, se enfocaba en priorizar soluciones "casi viables" o dentro del límite.
3.  **Generaciones finales:** Casi todas las soluciones sobrevivientes estaban **dentro del presupuesto**, lo que generó un enfoque en maximizar el retorno sin riesgo de exceder el límite.

**¿Qué pasaría con una penalización más suave (por ejemplo, 1)?**
- Las soluciones que excedían el presupuesto no tendrían una penalización tan drástica.
- El algoritmo seguiría probando combinaciones inviables por más tiempo.
- Podría terminar seleccionando una solución que **excede el presupuesto** (no válida) pero con un retorno alto.

**Conclusión:**
La penalización fuerte de **10** fue clave para que el algoritmo **aprendiera rápido a evitar violar la restricción**, asegurando que las soluciones finales fueran **viables y óptimas**. Sin ella, podríamos decir que el algoritmo tardaría más o elegiría soluciones inviables, lo que demoraría más el trabajo enfocado en la eficiencia.

#