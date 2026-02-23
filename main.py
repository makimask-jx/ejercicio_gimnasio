CLASES_OFICIALES: set = set(["Yoga", "Crossfit", "Pilates", "Zumba", "Boxeo"])


class Socio:
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self.mis_clases = set()

    def apuntar(self, clase):
        if clase in CLASES_OFICIALES:
            self.mis_clases.add(clase)
            print(f"{self.nombre} se ha apuntado a {clase}")
        else:
            print(f"ERROR: {clase} no se imparte en este centro")
            return

    def borrar(self, clase):
        if clase in self.mis_clases:
            self.mis_clases.discard(
                clase
            )  # Discard no lanza un error si no encuentra  la clase, al contrario que .remove
            print(f"{self.nombre} Se ha dado de baja de {clase}")
        else:
            print(f"ERROR: No estas apuntado/a a la clase ")

    def __str__(self):
        return f"Socio: {self.nombre} - Clases activas: {len(self.mis_clases)}"


class SocioVip(Socio):
    def __init__(self, nombre: str, acceso_spa: bool) -> None:
        super().__init__(nombre)
        self.acceso_spa = acceso_spa

    def __str__(self):
        return f"Socio VIP: {self.nombre} - Clases activas: {len(self.mis_clases)} - Spa: {'Si' if self.acceso_spa else 'No'}"
