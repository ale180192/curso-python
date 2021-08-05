import sys
import os

PATH_ENTRYPOINT_FILE = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(PATH_ENTRYPOINT_FILE)
sys.path.append(PATH_ENTRYPOINT_FILE)
print(sys.path)