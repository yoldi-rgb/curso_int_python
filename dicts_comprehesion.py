import math

def run():
    #dicts = {}

    #for i in range(1,10):
     #   if i % 3 != 0:
      #      dicts[i] = i**2
        
    dicts = {i: i**3 for i in range(1,101) if i % 3 != 0}    

    print(dicts)


    #challenge = {i : math.sqrt(i) for i in range(1,11)}
    #print(challenge)

if __name__ == '__main__':
    run()