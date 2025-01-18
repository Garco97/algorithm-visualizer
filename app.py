import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
from algorithms import bubble_sort, quick_sort
# Datos iniciales
data= list(range(1, 51))
random.shuffle(data)
states = []  # Para capturar los pasos del algoritmo
bar_rects = []
# Función para inicializar el gráfico
def init():
    global bar_rects
    for rect, value in zip(bar_rects, data):
        rect.set_height(value)
    return bar_rects

# Función para actualizar cada frame de la animación
def update(frame):
    global bar_rects
    for rect, value in zip(bar_rects, states[frame]):
        rect.set_height(value)
    return bar_rects
def init_fig():
    global bar_rects
    # Configuración inicial de la animación
    fig, ax = plt.subplots()
    fig.patch.set_facecolor('black')  # Fondo negro
    # Barras verdes y ajustadas para eliminar espacio entre ellas
    bar_width = 1.0  # Ancho completo
    bar_rects = ax.bar(range(len(data)), data, align="edge", color='green', width=bar_width)

    # Ocultar ejes y ajustar márgenes
    ax.axis('off')  # Quitar ejes
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)  # Ajustar márgenes para ocupar toda la ventana
    return fig
def run_algorithm(bar_rects, states, interval):
    bar_rects = []
    fig = init_fig()
    ani = animation.FuncAnimation(fig, update, frames=len(states),
                              init_func=init, blit=True, interval=interval, repeat=False)
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 2: exit()
    algorithm = int(sys.argv[1])
    print(algorithm)
    if algorithm == 0:
        bubble_sort(data.copy(), states)
        run_algorithm(bar_rects, states, 1)
    elif algorithm == 1:
        quick_sort(data.copy(), 0, len(data) - 1, states)
        run_algorithm(bar_rects, states, 100)
    else:
        exit()
