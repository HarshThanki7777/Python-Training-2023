def sum_of_positive_integers(n):
    if n < 1:
        return "n should be a positive integer."
    else:
        sum_value = (n * (n+1)) //2
        return sum_value
    
print(sum_of_positive_integers(5))   # 15 (1 + 2 + 3 + 4 + 5 = 15)
print(sum_of_positive_integers(10))  # 55 (1 + 2 + 3 + ... + 9 + 10 = 55)
print(sum_of_positive_integers(0))   # n should be a positive integer.