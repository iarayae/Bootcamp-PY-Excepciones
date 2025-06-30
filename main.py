from foto import Foto
from error import DimensionError

try:
    f = Foto(1200, 1300, "imagen.jpg")
    f.ancho = 3000  # debería lanzar excepción
except DimensionError as e:
    print("Excepción atrapada:", e)

try:
    f.alto = 0  # también inválido
except DimensionError as e:
    print("Excepción atrapada:", e)