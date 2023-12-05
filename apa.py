import random
import matplotlib.pyplot as plt
import sys 
import time
from statistics import mean 


limit = sys.getrecursionlimit() 
  
print('Before changing, limit of stack =', limit)  
  
# New limit - IMPORTANTE !!!!!!
# NAO DA PRA PASSAR DE 10 OverflowError: Python int too large to convert to C int
Newlimit = 10**9
  

sys.setrecursionlimit(Newlimit)  

limit = sys.getrecursionlimit() 
  
print('After changing, limit of stack =', limit)



def simulate_swaps(sorted_list, percentage):
    swaps = int(len(sorted_list) * percentage / 100)
    for _ in range(swaps):
        idx1, idx2 = random.sample(range(len(sorted_list)), 2)
        sorted_list[idx1], sorted_list[idx2] = sorted_list[idx2], sorted_list[idx1]
    return sorted_list

def quicksort_first_pivot(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        lesser = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort_first_pivot(lesser) + [pivot] + quicksort_first_pivot(greater)
    
def quicksort_middle_pivot(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot_index = (1 + len(arr)) // 2
        pivot = arr[pivot_index]
        lesser = [x for x in arr[:pivot_index] if x <= pivot] + [x for x in arr[pivot_index + 1:] if x <= pivot]
        greater = [x for x in arr[:pivot_index] if x > pivot] + [x for x in arr[pivot_index + 1:] if x > pivot]
        return quicksort_middle_pivot(lesser) + [pivot] + quicksort_middle_pivot(greater)


## DEFINIÇÔES

# no meu pc morreu quando passava de 10⁷
list_sizes = [10**i for i in range(2, 7)]
percentages = [5, 25, 45]

# DICT DE RESULTADOS
'''
será algo como:

resultados = {
    "tamanho_100": {
        "perc_5": {
            "quicksort_x": <tempo_medio>
        }
    }
}
'''
resultados = {}

for size in list_sizes:
    key = "size_" + str(size)
    resultados[key] = {}
    
    for percentage in percentages:
        key_2 = "perc_" + str(percentage)
        resultados[key][key_2] = {}
        
        sorted_list = list(range(1, size + 1))
        disordered_list = simulate_swaps(sorted_list, percentage)
        
        
        # REPRODUZIR ESSE TRECHO P/ OUTROS METODOS
        name_method = "first_pivot"
        times = []
        
        for i in range(10):
            inicio = time.time()
            quicksort_first_pivot(disordered_list)
            fim = time.time()
            
            total = fim - inicio
            times.append(total)
            
        average_time = mean(times)
        
        resultados[key][key_2][name_method] = average_time
        
        # REPRODUZIR ESSE TRECHO P/ OUTROS METODOS
        

print(resultados)

########################## EXEMPLO ##########################
'''array_1 = [5, 1, 4, 8, 10, 3]


print(quicksort_first_pivot(array_1))
print(quicksort_middle_pivot(array_1))'''

########################## FIM EXEMPLO ##########################

# gerar os graficos aq dps

#plt.show()


