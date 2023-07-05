# Proyecto: Tiro Parabólico

## Descripción
En este proyecto, exploraremos el concepto de tiro parabólico y su aplicación en la física. Analizaremos cómo un objeto lanzado bajo la influencia exclusiva de la gravedad sigue una trayectoria en forma de parábola. Utilizaremos las ecuaciones de la cinemática para calcular diversas propiedades del movimiento y realizar simulaciones.

## Evento físico a simular: Tiro Parabólico
El tiro parabólico es un movimiento en dos dimensiones en el cual un objeto es lanzado en un ángulo respecto a la horizontal y sigue una trayectoria parabólica bajo la influencia de la gravedad. Algunos ejemplos de tiro parabólico en la vida cotidiana incluyen lanzar una pelota de baloncesto o un proyectil.

### Breve Historia asociada(origen)
El tiro parabólico es un fenómeno importante en la física y tiene numerosas aplicaciones en el mundo real, desde deportes hasta trayectorias de proyectiles. Mediante el uso de las ecuaciones y las simulaciones, pudimos comprender cómo cambian la altura, el alcance y el tiempo de vuelo al variar diferentes parámetros como el ángulo de lanzamiento y la velocidad inicial. Estas conclusiones nos ayudan a comprender mejor el movimiento de los objetos en el aire y su comportamiento bajo la influencia de la gravedad.

### Matemática empleada
Para describir el tiro parabólico, utilizamos las siguientes ecuaciones:

- **Altura:** La altura del objeto en función del tiempo se puede calcular utilizando la ecuación:
y(t) = y0 + v0y * t - (1/2) * g * t^2

- donde:
  - `y(t)` es la altura en el tiempo `t`
  - `y0` es la altura inicial
  - `v0y` es la componente vertical de la velocidad inicial
  - `g` es la aceleración debido a la gravedad
  - `t` es el tiempo

- **Alcance horizontal:** El alcance horizontal del objeto se puede calcular utilizando la ecuación:
R = v0x * (2 * v0y / g)
- donde:
  - `R` es el alcance horizontal
  - `v0x` es la componente horizontal de la velocidad inicial
  - `v0y` es la componente vertical de la velocidad inicial
  - `g` es la aceleración debido a la gravedad

- **Tiempo de vuelo:** El tiempo de vuelo, que es el tiempo que el objeto permanece en el aire, se puede calcular utilizando la ecuación:
T = (2 * v0y) / g
- donde:
  - `T` es el tiempo de vuelo
  - `v0y` es la componente vertical de la velocidad inicial
  - `g` es la aceleración debido a la gravedad

### Como se resuelve

Supongamos que queremos calcular la distancia alcanzada por un proyectil lanzado con un ángulo de 45 grados y una velocidad inicial de 20 metros por segundo.

Dadas las siguientes fórmulas del tiro parabólico:

Alcance horizontal (R) = (v^2 * sin(2θ)) / g
Altura máxima (H) = (v^2 * sin^2(θ)) / (2 * g)
Donde:

v es la velocidad inicial
θ es el ángulo de lanzamiento
g es la aceleración debido a la gravedad
Conocemos los valores:

v = 20 m/s
θ = 45 grados
g = 9.8 m/s^2 (aproximadamente, la aceleración debido a la gravedad en la Tierra)
Ahora podemos calcular la distancia alcanzada y la altura máxima utilizando las fórmulas mencionadas:

Calculamos el alcance horizontal (R):

R = (20^2 * sin(2 * 45)) / 9.8

R = (400 * sin(90)) / 9.8

R = 400 / 9.8

R ≈ 40.82 metros

Calculamos la altura máxima (H):

H = (20^2 * sin^2(45)) / (2 * 9.8)

H = (400 * 0.5^2) / (2 * 9.8)

H = 200 / (2 * 9.8)

H ≈ 10.20 metros

Entonces,  un proyectil disparado en un ángulo de 45 grados con una velocidad inicial de 20 metros por segundo tendría una distancia horizontal de unos 40,82 metros y  una altura máxima de unos 10,20 metros.

### Aplicaciones 
#### Ejemplo de aplicación: Deportes de lanzamiento. 
El tiro parabólico está muy extendido en varios deportes de lanzamiento, donde el objetivo de los atletas es lanzar objetos lo más lejos posible o alcanzar ciertos objetivos. Algunos ejemplos de deportes que involucran  tiro parabólico incluyen: 
 
1.-  **Lanzamiento de jabalina**
En  atletismo, la jabalina es una prueba en la que los atletas lanzan una jabalina lo más lejos posible. Para lograrlo, deben aplicar el concepto de tiro parabólico. Los lanzadores ajustan el ángulo y la velocidad del lanzamiento para que la jabalina siga una trayectoria parabólica y viaje lo más lejos posible. 
 
2.-  **Lanzamiento de Bala**
En el lanzamineto de bala, los atletas intentan lanzar una bola de metal pesado lo más lejos posible. Al igual que  el lanzamiento de jabalina, el lanzamiento parabólico se utiliza para optimizar la distancia recorrida. Los atletas ajustan su técnica y la fuerza aplicada para que la bala siga una trayectoria parabólica para un alcance máximo. 
Estos ejemplos son solo algunos de cómo se aplica el tiro parabólico a los deportes. En cualquier caso, los atletas deben comprender las ecuaciones y principios del tiro parabólico para optimizar sus tiros y lograr mejores resultados en términos de distancia, precisión y rendimiento

## Programación 
### Descripción de herramientas utilizadas 
En el proyecto Tiro Parabólico usamos diferentes tipos de software: 
- Python 2.7.15: Python es un lenguaje de programación interpretado de alto nivel que se usa para desarrollar todo tipo de aplicaciones, ejemplos: Instagram, Netflix, Spotify, los desarrolladores usan Python porque es poderoso y fácil de aprender, y puede ejecutarse en muchas plataformas diferentes.
- Visual Estudio Code: Visual Studio Code es un editor de código gratuito y fácil de usar que lo  ayuda a codificar rápidamente. Se puede usar cualquier lenguaje de programación sin cambiar el editor. Visual Studio Code es compatible con muchos lenguajes, incluidos Python, Java, C, JavaScript y más.
- Github: GitHub es un sitio "social coding". Te permite subir repositorios de código para almacenarlo en el sistema de control de versiones, gestión de proyectos y equipos, así como oportunidades para la creación de redes.
- Librerías: Math y Pygame para realizar cálculos trigonométricos necesarios para las fórmulas de nuestro proyecto ( cos, sin, tan ) 

### Guia de Instalación 
### 1. Python

Python es un lenguaje de programación ampliamente utilizado. Sigue estos pasos para instalar Python:

1.  Ve al sitio web oficial de Python en [https://www.python.org/](https://www.python.org/).
 
![enter image description here](https://cdn.discordapp.com/attachments/968204410515775528/1124505950359920751/image.png)

2.  Haz clic en el enlace "Downloads" o "Descargas".
3.  Selecciona la versión más reciente de Python que sea compatible con tu sistema operativo (Windows, macOS o Linux).
5.  Descarga el instalador adecuado para tu sistema operativo.
6.  Ejecuta el instalador descargado y sigue las instrucciones del asistente de instalación.

![enter image description here](https://cdn.discordapp.com/attachments/968204410515775528/1124506171605274664/image.png)

7.  Haz clic en "Install" o "Instalar" para comenzar la instalación.
8.  Una vez completada la instalación, puedes abrir una terminal y ejecutar el comando `python --version` para verificar que Python se ha instalado correctamente.

### 2. GitHub

GitHub es una plataforma de desarrollo colaborativo y control de versiones. Sigue estos pasos para instalar GitHub:

1.  Ve al sitio web oficial de GitHub en [https://github.com/](https://github.com/).
2.  Haz clic en el botón "Sign up" o "Registrarse" si aún no tienes una cuenta de GitHub. Completa el proceso de registro para crear una cuenta.

![enter image description here](https://cdn.discordapp.com/attachments/968204410515775528/1124506787719172227/image.png)

3.  Una vez registrado, ve al enlace de descarga de GitHub Desktop en [https://desktop.github.com/](https://desktop.github.com/).

![enter image description here](https://cdn.discordapp.com/attachments/968204410515775528/1124506321333526638/image.png)

4.  Descarga el instalador de GitHub Desktop para tu sistema operativo.
5.  Ejecuta el instalador descargado y sigue las instrucciones del asistente de instalación.
6.  Durante la instalación, puedes dejar las opciones predeterminadas seleccionadas.
7.  Haz clic en "Install" o "Instalar" para comenzar la instalación.
8.  Una vez completada la instalación, puedes abrir GitHub Desktop e iniciar sesión con tu cuenta de GitHub para comenzar a utilizarlo.

### 3. Visual Studio Code

Visual Studio Code es un editor de código fuente muy popular y versátil. Sigue estos pasos para instalar Visual Studio Code:

1.  Ve al sitio web oficial de Visual Studio Code en [https://code.visualstudio.com/](https://code.visualstudio.com/).

![enter image description here](https://cdn.discordapp.com/attachments/968204410515775528/1124506994901012500/image.png)

2.  Haz clic en el botón "Download" o "Descargar".
3.  Selecciona el instalador adecuado para tu sistema operativo (Windows, macOS o Linux).
4.  Descarga el instalador y ejecútalo.
5.  Sigue las instrucciones del asistente de instalación.
6.  Durante la instalación, puedes dejar las opciones predeterminadas seleccionadas.
   
![enter image description here](https://cdn.discordapp.com/attachments/968204410515775528/1124507351454584912/image.png)

7.  Haz clic en "Next" o "Siguiente" para comenzar la instalación.
8.  Una vez completada la instalación, puedes abrir Visual Studio Code y comenzar a utilizarlo como tu editor de código preferido.

### Guia de Uso (Imágenes, Video tutorial)

1. Comprende los datos: Asegúrate de tener claro cuál es la velocidad inicial con la que se lanza el objeto y el ángulo de lanzamiento. La velocidad inicial es la magnitud de la velocidad con la que el objeto es lanzado, mientras que el ángulo de lanzamiento se refiere a la dirección en la que se lanza en relación con la horizontal.
2. El programa te pedirá 2 valores, los cuales calculara automáticamente, Velocidad inicial y Angulo.

![enter image description here](https://cdn.discordapp.com/attachments/960530424063488033/1123673736533508146/image.png)

3. Ya que los datos fueron ingresados se abrirá una ventana mostrando una simulación de la pelota lanzada, así mismo en la consola donde explicamos los datos, aparecerán toda la información correspondientes a las medidas y distancias, la altura máxima y distancia recorrida aparecerán cuando termine de caer la pelota.

![enter image description here](https://cdn.discordapp.com/attachments/960530424063488033/1123674186649452655/image.png)

### Enlace a Video con la explicacion del codigo desarrollado y del fenómeno físico desarrollado 

[...](https://youtu.be/GEsoHhCtTec)

## Conclusiones
Mientras realizábamos este proyecto, nos costó mucho simular la caída de la pelota con un tiro parabólico en el codigo. A medida que estudiamos las ecuaciones y los conceptos involucrados en este tipo de movimiento, nos dimos cuenta de que hay una serie de factores que deben tenerse en cuenta que dificultan la simulación precisa de una pelota que se deja caer. Uno de los mayores desafíos fue tener en cuenta las fluctuaciones gravitatorias que afectan la trayectoria real de la pelota en comparación con el modelo idealizado de un tiro parabólico. A pesar de las dificultades que han surgido, la parábola sigue siendo una ayuda importante en la física y en varios campos de aplicación. Al comprender y aplicar ecuaciones de lanzamiento parabólico, podemos analizar y predecir el movimiento de objetos en situaciones reales, como disparar un proyectil o deportes de lanzamiento. Con la ayuda de estas aplicaciones podemos calcular la trayectoria óptima, la distancia recorrida y la precisión necesaria para alcanzar los objetivos deseados. En conclusión, aunque tuvimos dificultad con el codigo para simular la caída de la pelota con un tiro parabólico, pudimos entender la importancia y utilidad de este concepto en varios campos. Al comprender el tiro parabólico, podemos analizar y predecir el movimiento de objetos en situaciones cotidianas y científicas, lo que nos brinda una mejor comprensión del mundo que nos rodea y nos permite optimizar el rendimiento en diversas actividades y aplicaciones prácticas.




