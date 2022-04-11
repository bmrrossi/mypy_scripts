from zipfile import ZipFile

file_name = "purepython.zip"

with ZipFile(file_name, 'r'):
    zip.printdir()
    print('Extracting all the files now...')
    zip.extractall()
    print('Done!')