from functools import reduce
def run():
    pass


    # Uso de filter
   
    my_list = [1,3,4,6,9,11,13,15,21]
    # ejemplo de list_comprehesion
    #odd = [i for i in my_list if i % 2 !=0]
    
    # filter recibe dos parametros: una funcion y un iterable(lista,agregar mas ejemplos)
    # colocando encima list 
    #odd = list(filter(lambda x: x % 2 !=0, my_list ))

    #print(odd)

    # Uso de map
    map_list =[1, 2, 3, 4, 5]

    #example list_comprehesion
    #odde = [ i**2  for i in map_list ]

    #odde = list(map(lambda x: x**2, map_list))

    #print(odde)

    # Uso de reduce
    reduce_list =[2,2,2,2,2]
    
    #all_multiplied = 1
    #for i in reduce_list:
    #    all_multiplied = all_multiplied * i
    
    # lambda recibe dos parametros se toma a y b en la primera iteracion 
    # pasando por la funcion a*b  y el resultado de la funcion 
    # pasara como "a" en la segunda iteracion
    all_multiplied = reduce(lambda a,b: a*b, reduce_list)

    print(all_multiplied)

if __name__ == '__main__':
    run()