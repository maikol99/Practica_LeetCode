def kidsWithCandies(candies, extracandies):
    
    max_candies = candies[0]
    for i in candies:
        if i > max_candies:
            max_candies = i
            
    
    resultado = []
    
    for i in candies:
        if i + extracandies >= max_candies:
            resultado.append(True)
        else:
            resultado.append(False)
    
    
    return resultado

print(kidsWithCandies([2, 3, 5, 1, 3], 3))
