import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from PIL import Image

# Cargar la imagen del pez
fish_image = Image.open('fish.png')

# Crear una figura y un eje
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 5)
ax.set_aspect('equal')
ax.axis('off')  # Ocultar los ejes para una mejor visualización

# Crear la imagen del pez como un objeto OffsetImage
fish_offset_image = OffsetImage(fish_image, zoom=0.1)
fish_ab = AnnotationBbox(fish_offset_image, (0, 2.5), frameon=False)
ax.add_artist(fish_ab)

# Función para actualizar la animación
def update(frame):
    x = frame
    y = 2.5 + 0.5 * np.sin(frame)  # Movimiento ondulante en el eje y
    fish_ab.xy = (x, y)
    return fish_ab,

# Crear la animación
ani = animation.FuncAnimation(fig, update, frames=np.linspace(0, 10, 200), interval=50, blit=True)

# Mostrar la animación
plt.show()
