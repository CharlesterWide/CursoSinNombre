import fichero2
from fichero2 import imprimeName2
from modulo import fichero3


def imprimeName1():
    print("Fichero 1 __name__:",__name__)
    
if __name__ == "__main__":
    imprimeName1()
    fichero2.imprimeName2()
    fichero3.imprimeName3()