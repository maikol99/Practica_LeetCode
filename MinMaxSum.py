


def MinMaxSum(arr):
    
    minimo = arr[0]
    maximo = arr[0]
    
    
    for num in arr:
        if num < min:
            min = num
        if num > maximo:
            maximo = num
            
    sum_total = 0
    for num in arr:
        sum_total += num
        
    suma_minima = sum_total - maximo
    
    suma_maxima = sum_total - minimo
    
    
    print(suma_minima, suma_maxima)