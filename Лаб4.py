import math

def f(x):
    if x <= 0 or x == 1 or x**4 == x:
        return "Invalid X"
    
    numerator = x + math.sin(x)  
    denominator = math.log(abs(x - x**4), 10) 
    
    if denominator == 0:
        return "Invalid denominator"
    
    log_base_4 = math.log(x) / math.log(4)  
    return numerator / denominator + log_base_4

x = float(input("x: "))
result = f(x)

print("f(x) =", result)
