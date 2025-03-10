# Linguo - En Construcción

<p align="center">
<img src="images/banner.jpg"  height=300>
</p>

Este proyecto es ideal para quienes buscan mejorar su vocabulario en inglés de manera interactiva y práctica, combinando la generación automática de audios con una aplicación gráfica intuitiva. Con pocas modificaciones se puede usar para otros idiomas.

# Índice

* [Linguo 1.0](#Linguo-1.0) 
* [Linguo 2.0](#Linguo-2.0) 
* [Linguo 2.0 Francés](#Linguo-2.0-Francés) 
* [Programa para Windows](#Programa-para-Windows) 
* [Autor](#Autor)


# Linguo 1.0

<p align="center">
<img src="images/linguo_1.jpg"  height=350>
</p>

Este proyecto contiene dos programas principales. El primer código genera archivos de audio para cada palabra en un archivo CSV de vocabulario, utilizando la biblioteca gTTS para sintetizar la pronunciación en inglés. Además, limpia y capitaliza el contenido del archivo CSV antes de generar los audios en formato MP3. Cada archivo de audio se guarda en la carpeta "audio", asegurando que los nombres sean compatibles eliminando caracteres no alfanuméricos y reemplazando espacios con guiones bajos. Para ello, se utiliza la función limpiar_nombre, que elimina caracteres especiales y formatea los nombres de archivo. El código itera sobre la primera columna del archivo CSV y, para cada palabra, genera un archivo de audio en la carpeta destino.

El segundo código implementa una interfaz gráfica con Tkinter para facilitar el aprendizaje de vocabulario en inglés. Permite visualizar palabras en inglés, revelar su traducción al español y reproducir su pronunciación. La aplicación carga el vocabulario desde un archivo CSV utilizando la función cargar_diccionario, que almacena las palabras y sus traducciones en una lista de tuplas. La interfaz se adapta dinámicamente al tamaño de la ventana gracias a la función ajustar_tamanio, que modifica la fuente y el espaciado de los elementos en función del tamaño de la ventana. También se incluyen funciones para navegar entre palabras (siguiente_palabra y anterior_palabra), mostrar la traducción (mostrar_traduccion) y reproducir el audio (pronunciar), verificando previamente si el archivo de audio existe. Además, se ha añadido soporte para mostrar un icono en la interfaz y manejar eventos de redimensionamiento.

# Linguo 2.0

<p align="center">
<img src="images/linguo_1i.jpg"  height=350>
</p>

Los cambios en esta nueva versión del código incluyen:

- Integración de pygame.mixer para la reproducción interna de archivos MP3, eliminando la necesidad de un reproductor externo.

- Nuevo botón de información (mostrar_info), que muestra detalles sobre la aplicación y su funcionamiento en una ventana emergente.

- Mejoras en la interfaz, incluyendo una barra de título con un icono personalizado y un diseño optimizado para mejorar la experiencia del usuario.



# Linguo 2.0-Francés

<p align="center">
<img src="images/linguo_1f.jpg"  height=350>
</p>

Aquí te contamos las principales modificaciones:

- Soporte para francés 🇫🇷: Ahora el sistema genera archivos de audio en francés gracias a gTTS, permitiendo el aprendizaje de este idioma con una correcta pronunciación.

- Compatibilidad con caracteres especiales: Se ha mejorado la carga y procesamiento del archivo CSV para asegurar que palabras con acentos y caracteres propios del francés sean correctamente reconocidas y guardadas.


# Programa para Windows

auto-py-to-exe
pyinstaller


<br>[Volver al Índice](#Índice)

# Autor

José R. Guignan
- Mail: joserguignan@gmail.com
- Linkedin: [https://www.linkedin.com/in/jrguignan/](https://www.linkedin.com/in/jrguignan)
- Portafolio: [https://jrguignan.github.io/](https://jrguignan.github.io/)
