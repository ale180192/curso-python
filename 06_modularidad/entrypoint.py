import sys
import os

PATH_ENTRYPOINT_FILE = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(PATH_ENTRYPOINT_FILE)
sys.path.append(BASE_DIR)
print(sys.path)


import carrito_compra
print(carrito_compra.IVA_BRA)




