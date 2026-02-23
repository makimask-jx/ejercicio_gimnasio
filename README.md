# ejercicio_gimnasio

# Gestión de Gimnasio (Sets y Herencia)

## KEYWORDS
**Principales:** #POO #herencia #super #sets #interseccion 
**Secundarias:** #pertenencia #f_strings

---

## Objetivo

Vas a crear un sistema para gestionar las inscripciones de los socios de un gimnasio. Los `sets` (conjuntos) son la estructura perfecta para esto porque:
1. Un socio no puede estar inscrito dos veces a la misma clase (evita duplicados).
2. Nos permiten comparar rápidamente qué clases tienen en común dos personas usando operaciones matemáticas de conjuntos.
3. Practicarás la herencia creando un tipo de socio especial (VIP) que reutiliza la lógica del socio normal.

Trabajarás en un archivo llamado `gimnasio_apellidos_nombre.py`.
- Si no tienes apellido2 no lo pongas.
- Si tienes acentos no los pongas.
- Si tu nombre o apellido tiene espacios, sustituye el espacio por un guion `-`.
Por ejemplo "Miguel Ángel González Pérez" sería `gimnasio_gonzalez_perez_miguel-angel.py`.

---

## REQUISITOS

### 1) Clases del Gimnasio
* Crea una variable global llamada `CLASES_OFICIALES` que sea un set con los siguientes textos: `"Yoga", "Crossfit", "Pilates", "Zumba", "Boxeo"`.

### 2) Clase `Socio` (Clase Padre)
Representa a un cliente base del gimnasio.

* **Atributos de Instancia:**
  * `nombre` (str)
  * `mis_clases` (set): Debe inicializarse como un **set vacío** en el constructor.

* **Métodos:**
  * `__init__(self, nombre)`: Guarda el nombre e inicializa el set vacío.
  * `apuntar(self, clase)`:
    * Comprueba si la clase existe dentro de `CLASES_OFICIALES` usando `in`.
    * Si existe, añádela al set del socio e imprime: `"[Nombre] se ha apuntado a [clase]"`.
    * Si no existe, imprime: `"ERROR: [clase] no se imparte en este gimnasio"`.
  * `borrar(self, clase)`:
    * Elimina la clase del set del socio de **forma segura** (no debe dar error si el socio intenta borrarse de una clase a la que no estaba apuntado). Revisa los apuntes sobre cómo borrar sin generar `KeyError`.
    * Imprime: `"[Nombre] se ha dado de baja de [clase]"`.
  * `__str__(self)`: Retorna un texto formateado: `"Socio: [Nombre] - Clases activas: [Cantidad de clases]"`. Usa `len()` para obtener la cantidad.

### 3) Clase `SocioVIP` (Clase Hija)
Representa a un socio con beneficios extra.

* **Herencia:** Debe heredar de `Socio`.
* **Métodos:**
  * `__init__(self, nombre, acceso_spa)`: Recibe el nombre y un booleano (`True`/`False`). Debe usar la función `super()` para que la clase padre inicialice el `nombre` y el set `mis_clases`. Después, guarda el nuevo atributo `acceso_spa`.
  * `__str__(self)`: Sobrescribe el método del padre para dar un formato especial. Debe retornar: `"Socio VIP: [Nombre] - Clases activas: [Cantidad] - Spa: [Sí/No]"`. *(Pista: Puedes usar un condicional ternario o un if normal para traducir True/False a Sí/No).*

### 4) Función externa: `clases_en_comun`
* Crea una función (fuera de las clases) que reciba dos objetos `Socio` (pueden ser VIP o normales).
* Debe usar la **intersección de conjuntos** para averiguar a qué clases van juntos.
* Si tienen clases en común, imprime: `"[Nombre1] y [Nombre2] coinciden en: {clases}"`.
* Si no tienen ninguna, imprime: `"No tienen clases en común."`

---

## DATOS INICIALES Y PRUEBA

Copia este código al final de tu archivo para comprobar que todo funciona:

```python
# 1. Crear socios
socio1 = Socio("Jorge")
socio2 = SocioVIP("Ana", acceso_spa=True)

print("--- INSCRIPCIONES ---")
# 2. Apuntar a clases
socio1.apuntar("Yoga")
socio1.apuntar("Pilates")
socio1.apuntar("Natación") # Debería dar ERROR (no existe)

socio2.apuntar("Crossfit")
socio2.apuntar("Yoga")
socio2.apuntar("Yoga") # No debería duplicarse internamente

print("\n--- BORRADOS ---")
# 3. Borrar de forma segura
socio2.borrar("Crossfit")
socio2.borrar("Zumba") # No está apuntado, NO debe dar error

print("\n--- RESUMEN ---")
# 4. Comprobar el __str__ de ambas clases
print(socio1)
print(socio2)

print("\n--- COINCIDENCIAS ---")
# 5. Comprobar intersección de conjuntos
clases_en_comun(socio1, socio2)

```

---

## EJEMPLO DE EJECUCIÓN ESPERADO

```bash
--- INSCRIPCIONES ---
Jorge se ha apuntado a Yoga
Jorge se ha apuntado a Pilates
ERROR: Natación no se imparte en este gimnasio
Ana se ha apuntado a Crossfit
Ana se ha apuntado a Yoga
Ana se ha apuntado a Yoga

--- BORRADOS ---
Ana se ha dado de baja de Crossfit
Ana se ha dado de baja de Zumba

--- RESUMEN ---
Socio: Jorge - Clases activas: 2
Socio VIP: Ana - Clases activas: 1 - Spa: Sí

--- COINCIDENCIAS ---
Jorge y Ana coinciden en: {'Yoga'}
```