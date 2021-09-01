from os import linesep
from typing import Text


def read():
    number = []
    with open("./archivos/number.txt", "r",encoding="utf-8") as f:
        for line in f:
            number.append(int(line))
        print(number)



def write():
    names = ['Erika', 'Santiago ','Andrés', 'Guadalupe','Diana']
    ## el modo de apertura es escritura( sobreescritura )
    with open("./archivos/names.txt", 'w',encoding="utf-8") as f:
        for i in names:
            f.write(i)
            f.write("\n")


def run():
    read()
    write()




if __name__ == '__main__':
    run()