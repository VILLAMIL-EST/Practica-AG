import random


random.seed(42)


def decodificar_binario(genotipo):
    return int("".join(map(str, genotipo)), 2)


def aptitud_cuadratica(fenotipo):
    return float(fenotipo**2)


class AlgoritmoGenetico:
    def __init__(self, tamano_poblacion, longitud_cromosoma, pc, pm):
        self.tamano_poblacion = tamano_poblacion
        self.longitud_cromosoma = longitud_cromosoma
        self.pc = pc
        self.pm = pm
        self.poblacion = []
        self.mejor_genotipo = []
        self.mejor_aptitud = float("-inf")
        self.ultimos_puntos = ()

    def inicializar_poblacion(self):
        self.poblacion = [
            [random.randint(0, 1) for _ in range(self.longitud_cromosoma)]
            for _ in range(self.tamano_poblacion)
        ]

    def calcular_aptitudes(self):
        return [
            aptitud_cuadratica(decodificar_binario(individuo))
            for individuo in self.poblacion
        ]

    def seleccionar_por_ruleta(self, aptitudes):
        if sum(aptitudes) == 0:
            return random.choices(self.poblacion, k=self.tamano_poblacion)

        return random.choices(
            self.poblacion,
            weights=aptitudes,
            k=self.tamano_poblacion,
        )

    def cruzar_dos_puntos(self, padre_1, padre_2):
        if random.random() < self.pc:
            punto_1, punto_2 = sorted(
                random.sample(range(1, self.longitud_cromosoma), 2)
            )
            self.ultimos_puntos = (punto_1, punto_2)

            hijo_1 = (
                padre_1[:punto_1]
                + padre_2[punto_1:punto_2]
                + padre_1[punto_2:]
            )
            hijo_2 = (
                padre_2[:punto_1]
                + padre_1[punto_1:punto_2]
                + padre_2[punto_2:]
            )
            return hijo_1, hijo_2

        self.ultimos_puntos = ()
        return padre_1[:], padre_2[:]

    def mutar(self, cromosoma):
        hijo = cromosoma[:]

        for posicion in range(self.longitud_cromosoma):
            if random.random() < self.pm:
                hijo[posicion] = 1 - hijo[posicion]

        return hijo

    def ejecutar(self, generaciones):
        self.inicializar_poblacion()

        for generacion in range(1, generaciones + 1):
            aptitudes = self.calcular_aptitudes()
            mejor_posicion = max(range(self.tamano_poblacion), key=lambda i: aptitudes[i])

            if aptitudes[mejor_posicion] > self.mejor_aptitud:
                self.mejor_aptitud = aptitudes[mejor_posicion]
                self.mejor_genotipo = self.poblacion[mejor_posicion][:]

            promedio = sum(aptitudes) / len(aptitudes)
            print(
                f"Generacion {generacion:02d} | "
                f"promedio: {promedio:7.2f} | "
                f"mejor: {self.mejor_aptitud:.0f}"
            )

            padres = self.seleccionar_por_ruleta(aptitudes)
            padres = [padre[:] for padre in padres]
            random.shuffle(padres)
            nueva_poblacion = []

            for posicion in range(0, self.tamano_poblacion, 2):
                hijo_1, hijo_2 = self.cruzar_dos_puntos(
                    padres[posicion], padres[posicion + 1]
                )
                nueva_poblacion.append(self.mutar(hijo_1))
                nueva_poblacion.append(self.mutar(hijo_2))

            aptitudes_nuevas = [
                aptitud_cuadratica(decodificar_binario(individuo))
                for individuo in nueva_poblacion
            ]
            peor_posicion = min(
                range(self.tamano_poblacion), key=lambda i: aptitudes_nuevas[i]
            )
            nueva_poblacion[peor_posicion] = self.mejor_genotipo[:]
            self.poblacion = nueva_poblacion

        return self.mejor_genotipo, self.mejor_aptitud


print("ACTIVIDAD 3 - CRUZAMIENTO DE DOS PUNTOS")

ag = AlgoritmoGenetico(
    tamano_poblacion=10,
    longitud_cromosoma=5,
    pc=0.8,
    pm=0.05,
)

# Ejemplo directo para observar el intercambio del segmento central.
padre_1 = [1, 1, 1, 0, 0]
padre_2 = [0, 0, 0, 1, 1]
probabilidad_original = ag.pc
ag.pc = 1.0
hijo_1, hijo_2 = ag.cruzar_dos_puntos(padre_1, padre_2)
ag.pc = probabilidad_original

print("\nEJEMPLO DEL OPERADOR")
print("Padre 1:", padre_1)
print("Padre 2:", padre_2)
print("Puntos de corte:", ag.ultimos_puntos)
print("Hijo 1: ", hijo_1)
print("Hijo 2: ", hijo_2)

print("\nEJECUCION DEL ALGORITMO PARA f(x) = x^2")
mejor_genotipo, mejor_aptitud = ag.ejecutar(generaciones=10)

print("\nRESULTADO FINAL")
print("Mejor genotipo:", "".join(map(str, mejor_genotipo)))
print("Mejor fenotipo:", decodificar_binario(mejor_genotipo))
print("Mejor aptitud:", mejor_aptitud)
