import shutil, os
from pathlib import Path

p = Path.home()

source = p/'folders'
destination = p/'backup'

shutil.copytree(source, destination)