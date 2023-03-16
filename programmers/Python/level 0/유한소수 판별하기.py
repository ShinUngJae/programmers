import math

def solution(a, b):
    b2 = b // math.gcd(a, b)
    
    while b2 > 1 :
        if b2 % 2 == 0 :
            b2 = b2 // 2
        elif b2 % 5 == 0 :
            b2 = b2 // 5
        else :
            return 2
        
    return 1