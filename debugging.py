#def divisor(num):
 #   divisior = []
  #  for i in range(1,num + 1):
   #     if num % i == 0:    #1 el uso del debuggin con el numero uno para encontrar el error 
    #        divisior.append(i)
    #return divisior
def division(num):
    ## uso del try raise
    try:
        if num < 0:
            raise ValueError("ingresa un numero positivo")
        division = [i for i in range(1,num+1) if num % i == 0]
        return division
    except ValueError as ve:
        print(ve)
        return str(num) + "  number is not positive"

def run():
    
    #divisior = lambda num: [i for i in range(1, num+ 1 ) if num % i == 0]
   
   ## uso de try except
    try:
        num = int(input("Ingrese un numero: "))
        print(division(num))
        print("termino el programa ")
    except ValueError:
        print("Debes colocar un numero")





if __name__ == '__main__':
    run()
