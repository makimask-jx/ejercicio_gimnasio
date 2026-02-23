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
            # print(f"ERROR: No estas apuntado/a a la clase: {clase}")
            print(f"{self.nombre} se ha dado de baja de {clase}")

    def __str__(self):
        return f"Socio: {self.nombre} - Clases activas: {len(self.mis_clases)}"


class SocioVip(Socio):
    def __init__(self, nombre: str, acceso_spa: bool) -> None:
        super().__init__(nombre)
        self.acceso_spa = acceso_spa

    def __str__(self):
        return f"Socio VIP: {self.nombre} - Clases activas: {len(self.mis_clases)} - Spa: {'Si' if self.acceso_spa else 'No'}"


def clases_en_comun(socio1: Socio | SocioVip, socio2: Socio | SocioVip):
    clases_comunes = socio1.mis_clases & socio2.mis_clases
    if clases_comunes:
        print(f"{socio1.nombre} y {socio2.nombre} coinciden en {clases_comunes}")
    else:
        print(f"{socio1.nombre} y {socio2.nombre} no coinciden en ninguna clase")


# 1. Crear socios
socio1 = Socio("Jorge")
socio2 = SocioVip("Ana", acceso_spa=True)
print("--- INSCRIPCIONES ---")
# 2. Apuntar a clases
socio1.apuntar("Yoga")
socio1.apuntar("Pilates")
socio1.apuntar("Natación")  # Debería dar ERROR (no existe)
socio2.apuntar("Crossfit")
socio2.apuntar("Yoga")
socio2.apuntar("Yoga")  # No debería duplicarse internamente
print("\n--- BORRADOS ---")
# 3. Borrar de forma segura
socio2.borrar("Crossfit")
socio2.borrar("Zumba")  # No está apuntado, NO debe dar error
print("\n--- RESUMEN ---")
# 4. Comprobar el __str__ de ambas clases
print(socio1)
print(socio2)
print("\n--- COINCIDENCIAS ---")
# 5. Comprobar intersección de conjuntos
clases_en_comun(socio1, socio2)
