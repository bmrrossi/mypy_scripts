from imp import source_from_cache
import shutil

source = './f1.txt'
destination = './files'

shutil.move(source, destination)