import os
from zipfile import ZipFile

from cupshelpers import Printer


os.chdir("./server/uploads")
file_list = os.listdir()
# print( file_list )
teste_list = [0,2,"asdasd"]
for file in file_list:
    if ".zip" not in file:
        continue
    with ZipFile(file, "r") as zip:
        teste_list += zip.namelist()
        print( teste_list )