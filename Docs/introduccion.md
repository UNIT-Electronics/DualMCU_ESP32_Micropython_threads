# Introducción a los Hilos en MicroPython

Los hilos, también conocidos como threads en inglés, son una forma poderosa de realizar múltiples tareas de manera concurrente en un programa de software. En MicroPython, los hilos nos permiten dividir la ejecución de nuestro programa en múltiples secuencias de instrucciones, lo que puede mejorar significativamente la eficiencia y la capacidad de respuesta de nuestras aplicaciones en plataformas como DualMCU ESP32.

## ¿Qué es un Hilo?
Un hilo es una unidad básica de ejecución en un programa. Piensa en un programa como un conjunto de tareas que deben realizarse. Un hilo es como un "subprograma" dentro de un programa más grande que puede ejecutarse de manera independiente y concurrente. Esto significa que puedes tener varios hilos ejecutándose al mismo tiempo, cada uno haciendo su trabajo de manera independiente.

#### Ventajas de Usar Hilos en MicroPython
La programación multihilo en MicroPython ofrece varias ventajas, especialmente en aplicaciones de IoT y sistemas embebidos:

- **Mejora de la Eficiencia** : Los hilos permiten que partes del programa se ejecuten en paralelo, lo que puede acelerar la ejecución de tareas.

- **Mayor Capacidad de Respuesta**: Con hilos, tu programa puede realizar múltiples tareas simultáneamente, lo que mejora la capacidad de respuesta de las aplicaciones.

- **Gestión de Tareas Concurrentes**: Los hilos son ideales para tareas que deben ejecutarse en segundo plano mientras otras tareas principales continúan funcionando.

## Uso de Hilos en MicroPython
MicroPython, una implementación de Python optimizada para sistemas embebidos, permite trabajar con hilos mediante la biblioteca **_threads**. A continuación, se presenta una guía básica para comenzar a utilizar hilos en MicroPython:

1. ***Importar la Biblioteca _threads.***
Para comenzar, debes importar la biblioteca _threads en tu programa de MicroPython. Puedes hacerlo con la siguiente instrucción:

    ```python
    import _threads as threads
    ```
2. ***Crear una Función que Represente el Hilo***
Define una función que contenga el código que deseas que se ejecute en paralelo en un hilo separado. Por ejemplo:

    ```python
    def mi_funcion_hilo():
    ```
   
3. ***Crear y Iniciar un Hilo***
Usa la función start_new_thread() de la biblioteca _threads para crear y comenzar un nuevo hilo. Puedes hacerlo de la siguiente manera:

    ```python
    threads.start_new_thread(mi_funcion_hilo, ())
    ```
4. ***Esperar la Finalización de los Hilos (Opcional)***
Si necesitas esperar a que los hilos terminen antes de continuar con el programa principal, puedes usar threads.thread_join() de la siguiente manera:

    ```python
    threads.thread_join()
    ```
## Ejemplo Práctico
A continuación, se muestra un ejemplo completo que crea y ejecuta dos hilos en MicroPython:

```python
#    __,_,
#   [_|_/ 
#    //
#  _//    __
# (_|)   |@@|
#  \ \__ \--/ __
#   \o__|----|  |   __
#       \ }{ /\ )_ / _\
#       /\__/\ \__O (__
#      (--/\--)    \__/
#      _)(  )(_
#     `---''---`

import _threads as threads
import time

def hilo_1():
    for i in range(5):
        print("Hilo 1 - Iteración", i)
        time.sleep(1)

def hilo_2():
    for i in range(5):
        print("Hilo 2 - Iteración", i)
        time.sleep(1)

threads.start_new_thread(hilo_1, ())
threads.start_new_thread(hilo_2, ())

threads.thread_join()
```
Este programa creará dos hilos que ejecutan las funciones hilo_1 y hilo_2 simultáneamente, imprimiendo mensajes en la consola.

## Recursos Adicionales
Para obtener más información y detalles sobre cómo trabajar con hilos en [MicroPython](https://micropython.org/) utilizando la biblioteca [_threads](https://docs.micropython.org/en/latest/library/_thread.html), consulta la documentación oficial de MicroPython y la documentación específica de la biblioteca _threads.



