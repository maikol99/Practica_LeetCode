

def birthdayCakeCandles(candles):
    
    maximo = candles[0]
    
    for num in candles:
        if num > maximo:
            maximo = num
       
       
    count_suma = 0     
    for num in candles:
        if num == maximo:
            count_suma += 1
    
    return count_suma


