def run():
    divisior = lambda num: [i for i in range(1, num+ 1 ) if num % i == 0]
    
    num = (input("Ingrese un numero: "))
    assert num.isnumeric(), "Ingresar un numero "
    print(divisior(int(num)))
    print("termino el programa ")
   
        





if __name__ == '__main__':
    run()
