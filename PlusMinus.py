

def plusMinus(arr):
    # Write your code here
    n = len(arr)
    sum_positive = 0
    sum_negative = 0
    cero = 0
    
    for i in range(n):
        if arr[i] > 0:
            sum_positive += 1
        elif arr[i] < 0: 
            sum_negative += 1
        else:
            cero += 1
           
    print(sum_positive / n)
    print(sum_negative / n)
    print(cero / n)
    