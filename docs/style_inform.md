# Integrantes: 
## JUAN SEBASTIAN DIAZ
## JULIAN MENDOZA
## SANTIAGO VALENCIA
## ALEJANDRO LONDOÑO
## ALEJANDRO CASTRO


# Standard commit 

Primera línea: Algo breve pero descriptivo
               de lo que se ha hecho
               ¡Que sirva para algo! :-S
               Que facilite las búsquedas si es preciso
   Debe empezar por uno de estos prefijos:
   - WIP: si lleva trabajo sin terminar
   - END: si es código final, listo para revisar
   Además, según el tipo de código, debe llevar un de estos:
   - #NNN: número de tarea a la que pertenece el trabajo
   - BUG: cuando corrige un bug
   - DOC: si se está tocando documentación
   - REF: si es solo una refactorización
   - IMG: si son retoques estéticos/de imagen
   - PRF: retoques de rendimiento
   - TST: código relacionado con tests
   - CID: cambios al proceso de CI/CD

   Por ejemplo:
   - WIP:#123: Nuevo formulario de crear usuario
   - END:bug: Problema con cálculo de hash
   - WIP:DOC: Actualizado manual del alumno
----------------------------------------------------------
Info extra (opc)
   Si la línea anterior no tiene todo lo necesario
   o si el id de tarea no existe, ofrecer detalles sobre
   - por qué se han hecho los cambios
   - detalles importantes sobre cambios
   - posible rotura de compatibilidad
   - cambios de funcionalidad
   - etc...

----------------------------------------------------------

Recursos relacionados - Donde ver información extra (opc)

   Por ejemplo, urls a documentos internos/externos
   sobre técnicas utilizadas, funcionalidad,
   casos de uso, docs técnicos, etc..

----------------------------------------------------------



# Coding styles: pep8, ext VisualS Code: autopep8


1. **Indentación:**
   - Utiliza 4 espacios por nivel de sangría.
   - Evita el uso de tabuladores para la sangría.

```python
# Correcto
def funcion_ejemplo():
    if condicion:
        bloque_de_codigo()
    else:
        otro_bloque()

# Incorrecto
def funcion_mala():
  if condicion:
      bloque_mal_indentado()
  else:
    bloque_mal_indentado()
```

2. **Longitud de línea:**
   - Limita las líneas a 79 caracteres para el código y 72 para comentarios y documentación.
   - Divide líneas largas con paréntesis si es necesario.

```python
# Correcto
resultado = funcion_larga(param1, param2, param3,
                          param4, param5)

# Incorrecto
resultado = funcion_larga(param1, param2, param3, param4, param5)
```

3. **Espacios en blanco:**
   - Usa espacios alrededor de operadores y después de comas.
   - Evita espacios en blanco innecesarios al final de las líneas.

```python
# Correcto
lista = [1, 2, 3]
suma = 2 + 2
funcion(param1, param2)

# Incorrecto
lista=[1,2,3]
suma = 2+2
funcion( param1 , param2 )
```

4. **Comentarios:**
   - Escribe comentarios para explicar el código cuando sea necesario, pero evita comentarios obvios o innecesarios.
   - Utiliza docstrings para documentar funciones y módulos.

```python
# Correcto
# Calcula el promedio de una lista de números.
def calcular_promedio(lista):
    # Suma los elementos y divide por la cantidad.
    suma = sum(lista)
    promedio = suma / len(lista)
    return promedio

# Incorrecto
# Esta función suma los elementos y calcula el promedio.
def promedio(lista):
    total = sum(lista)  # Aquí sumamos la lista.
    prom = total / len(lista)  # Calculamos el promedio.
    return prom  # Devolvemos el resultado.
```
