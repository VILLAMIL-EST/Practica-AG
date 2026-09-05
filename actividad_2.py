import random


random.seed(42)

CANDIDATOS = [
    {"nombre": "Ana", "habilidad": 88},
    {"nombre": "Brayan", "habilidad": 72},
    {"nombre": "Carla", "habilidad": 95},
    {"nombre": "Daniel", "habilidad": 80},
    {"nombre": "Elena", "habilidad": 91},
    {"nombre": "Felipe", "habilidad": 76},
    {"nombre": "Gabriela", "habilidad": 89},
    {"nombre": "Hugo", "habilidad": 70},
    {"nombre": "Isabel", "habilidad": 93},
    {"nombre": "Juan", "habilidad": 78},
    {"nombre": "Karen", "habilidad": 85},
    {"nombre": "Luis", "habilidad": 90},
]


def decodificar_personal(genotipo):
    seleccionados = []

    for posicion, bit in enumerate(genotipo):
        if bit == 1:
            seleccionados.append(CANDIDATOS[posicion])

    return {
        "seleccionados": seleccionados,
        "cantidad": len(seleccionados),
        "habilidad_total": sum(persona["habilidad"] for persona in seleccionados),
    }


def aptitud_personal(fenotipo):
    # La solucion solo es valida cuando selecciona exactamente cinco personas.
    if fenotipo["cantidad"] != 5:
        diferencia = abs(fenotipo["cantidad"] - 5)
        return -1000 - (100 * diferencia)

    return float(fenotipo["habilidad_total"])


class AlgoritmoGenetico:
    def __init__(self, tamano_poblacion, longitud_cromosoma, pc, pm):
        self.tamano_poblacion = tamano_poblacion
        self.longitud_cromosoma = longitud_cromosoma
        self.pc = pc
        self.pm = pm
        self.poblacion = []
        self.mejor_genotipo = []
        self.mejor_aptitud = float("-inf")

    def inicializar_poblacion(self):
        self.poblacion = [
            [random.randint(0, 1) for _ in range(self.longitud_cromosoma)]
            for _ in range(self.tamano_poblacion)
        ]

    def calcular_aptitudes(self):
        return [
            aptitud_personal(decodificar_personal(individuo))
            for individuo in self.poblacion
        ]

    def seleccionar_por_torneo(self, aptitudes):
        seleccionados = []

        for _ in range(self.tamano_poblacion):
            participantes = random.sample(range(self.tamano_poblacion), 5)
            ganador = max(participantes, key=lambda posicion: aptitudes[posicion])
            seleccionados.append(self.poblacion[ganador][:])

        return seleccionados

    def cruzar_un_punto(self, padre_1, padre_2):
        if random.random() < self.pc:
            punto = random.randint(1, self.longitud_cromosoma - 1)
            hijo_1 = padre_1[:punto] + padre_2[punto:]
            hijo_2 = padre_2[:punto] + padre_1[punto:]
            return hijo_1, hijo_2

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

            validos = sum(sum(individuo) == 5 for individuo in self.poblacion)
            print(
                f"Generacion {generacion:02d} | "
                f"validos: {validos:02d}/{self.tamano_poblacion} | "
                f"mejor aptitud: {self.mejor_aptitud:.0f}"
            )

            padres = self.seleccionar_por_torneo(aptitudes)
            random.shuffle(padres)
            nueva_poblacion = []

            for posicion in range(0, self.tamano_poblacion, 2):
                hijo_1, hijo_2 = self.cruzar_un_punto(
                    padres[posicion], padres[posicion + 1]
                )
                nueva_poblacion.append(self.mutar(hijo_1))
                nueva_poblacion.append(self.mutar(hijo_2))

            # El mejor individuo reemplaza al peor para no perderse entre generaciones.
            aptitudes_nuevas = [
                aptitud_personal(decodificar_personal(individuo))
                for individuo in nueva_poblacion
            ]
            peor_posicion = min(
                range(self.tamano_poblacion), key=lambda i: aptitudes_nuevas[i]
            )
            nueva_poblacion[peor_posicion] = self.mejor_genotipo[:]
            self.poblacion = nueva_poblacion

        return self.mejor_genotipo, self.mejor_aptitud


print("ACTIVIDAD 2 - SELECCION ESTRICTA DE PERSONAL")
print("Un cromosoma valido debe tener exactamente cinco bits encendidos.\n")

ejemplo_invalido = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
fenotipo_invalido = decodificar_personal(ejemplo_invalido)
print("EJEMPLO DE LA RESTRICCION")
print("Genotipo:", "".join(map(str, ejemplo_invalido)))
print("Personas seleccionadas:", fenotipo_invalido["cantidad"])
print("Aptitud penalizada:", aptitud_personal(fenotipo_invalido))
print()

ag_personal = AlgoritmoGenetico(
    tamano_poblacion=40,
    longitud_cromosoma=len(CANDIDATOS),
    pc=0.8,
    pm=0.01,
)

mejor_genotipo, mejor_aptitud = ag_personal.ejecutar(generaciones=30)
mejor_equipo = decodificar_personal(mejor_genotipo)

print("\nRESULTADO FINAL")
print("Mejor genotipo:", "".join(map(str, mejor_genotipo)))
print("Cantidad de personas:", mejor_equipo["cantidad"])
print("Habilidad total:", int(mejor_aptitud))
print("Equipo seleccionado:")

for persona in mejor_equipo["seleccionados"]:
    print(f"- {persona['nombre']}: {persona['habilidad']} puntos")
