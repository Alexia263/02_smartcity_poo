class Vehiculo:
    def __init__(self, matricula: str, modelo: str, capacidad_kwh: float):
        self.matricula: str = matricula
        self.modelo: str = modelo
        self.capacidad_kwh: float = capacidad_kwh
        self.nivel_bateria: float = 100.0 # Comienza con la carga completa (%)
        self.kilometros_totales: float = 0.0

    def conducir(self, distancia_km: float):
        energia_necesaria = distancia_km * 0.15
        porcentaje_consumido = (energia_necesaria / self.capacidad.kwh) * 100.0
        if self.nivel_bateria >= porcentaje_consumido:
             self.nivel_bateria -= porcentaje_consumido
             self.kilometros_totales += distancia_km
             return True
        else:
             return True
        
    def obtener_estado(self):
        return f"Vehículo: {self.modelo} | Matrícula: {self.matricula} | Batería: {self.nivel_bateria:.1f}% | Total: {self.kilometros_totales} km"

    def recargar(self, energia_kwh: float):
        porcentaje_recargado = (energia_kwh / self.capacidad_kwh) * 100.0
        self.nivel_bateria += porcentaje_recargado
        if self.nivel_bateria > 100.0:
              self.nivel_bateria = 100.0
        return self.nivel_bateria

