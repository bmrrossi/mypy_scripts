import shutil, os
from pathlib import Path

p = Path.home()

source = p/'spam.txt'
destination = p/'folder/spam.txt'

shutil.copy(source, destination)