'''
Given a value N, if we want to make change for N cents, and we have infinite supply of each of S = { S1, S2, .. , Sm} valued coins, how many ways can we make the change? The order of coins doesn’t matter.
For example, for N = 4 and S = {1,2,3}, there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}. So output should be 4. For N = 10 and S = {2, 5, 3, 6}, there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}. So the output should be 5.
'''
'''
solucion = []
def coinChange(N,currencies):
  counter = 0
  solucion_actual = []
  j = 0
  for i in range(0,len(currencies)):
    
    while j+i <= N:
      while counter < N:
        solucion_actual.append(i)
        counter = counter + currencies.at(i) + currencies.at(j)
        if (counter == N):
          solucion.append(solucion_actual)
      j = j + 1
      counter = 0
      solucion_actual = []
    j = 0
  print(solucion)
print(coinChange(4,{1,2,3}))
'''
#expected output = [1,1,1,1] [2,2]

'''
1,1,1,1
1,1,2
1,1,3
1,2,1 no la vamos a tener en cuenta
1,2,2
1,2,3
1,3
opciones del 1
2,2
2,3
opciones del 2
3
opciones del 3
'''
#iteramos cada elemento con el mismo
       #si esa llega a N entonces esa es una solucion
       #si no llega a N y la suma actual es menor entonces se sigue con el siguiente



print("Solucion 24/02/2022:")
lista_sol =[]
def coins (N, array,solucion_actual):
  if (sum(solucion_actual) == N):
        lista_sol.append(solucion_actual)
  elif (sum(solucion_actual) < N):
    for i in array:
      if (sum(solucion_actual+[arr[1]]) <= N): #casos en los que se necesitan muchos i. ej: 1,1,1,1,1
        coins(N,array,solucion_actual+[i])     #se llama por ejemplo si 1,1 se pasa el array completo para hacer 1,1,1
        array = array[1:]                      #despues de que se hallan hecho todos los casos donde i,i,i,i se quita ese i
                                               #(para que no hayan respuestas como : 1,2 y 2,1, solo se cogen los items que son
                                               #mayores que i, debido a que los menores e iguales ya se han procesado)
      else:
        coins(N,array[1:],solucion_actual+[i]) #(para que no hayan respuestas como : 1,2 y 2,1, solo se cogen los items que son
                                               #mayores que i, debido a que los menores e iguales ya se han procesado)

N = 200
arr= [1,2,4,4]

coins(N,arr,[])
print(len(lista_sol))




print("Solucion de geeks for geeks:")

# Recursive Python3 program for
# coin change problem.
 
# Returns the count of ways we can sum
# S[0...m-1] coins to get sum n
def count(S, m, n ):
 
    # If n is 0 then there is 1
    # solution (do not include any coin)
    if (n == 0):
        return 1
 
    # If n is less than 0 then no
    # solution exists
    if (n < 0):
        return 0;
 
    # If there are no coins and n
    # is greater than 0, then no
    # solution exist
    if (m <=0 and n >= 1):
        return 0
 
    # count is sum of solutions (i)
    # including S[m-1] (ii) excluding S[m-1]
    return count( S, m - 1, n ) + count( S, m, n-S[m-1] );
 
# Driver program to test above function

print(count(arr,len(arr), N))

def divisiblePorUnArray(numero,lista):
  lista.sort()
  for i in lista:
    iterador = 1
    constante = numero
    while constante > 0:
      for j in lista:
        if (constante%j == 0):
          return True
      constante = constante - i*iterador
  return False
  
def checkio(vueltas, listaValoresMonedas):
   minMonedas = [0]*(vueltas+1)
   for centavos in range(vueltas+1):
      conteoMonedas = centavos
      for j in [m for m in listaValoresMonedas if m <= centavos]:
            if minMonedas[centavos-j] + 1 < conteoMonedas:
               conteoMonedas = minMonedas[centavos-j]+1
      minMonedas[centavos] = conteoMonedas
   if divisiblePorUnArray(vueltas,listaValoresMonedas):
      return minMonedas[vueltas]
   return None

if __name__ == '__main__':
    print("Mi solucion pasada (hace lo mismo pero la solucion requerida era diferente):")
    print(checkio(N, arr))
    print('Done')
