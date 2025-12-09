



def diagonalDifference(arr):
    
    n = len(arr)
    
    sum_diagonal1 = 0
    sum_diagonal2 = 0
    
    for i in range(n):
        sum_diagonal1 += arr[i][i]
        sum_diagonal1 += arr[i][n - 1 - i]
        
    return abs(sum_diagonal1 - sum_diagonal2)

