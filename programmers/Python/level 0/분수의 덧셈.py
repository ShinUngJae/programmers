import math

def solution(numer1, denom1, numer2, denom2) :
    gcd = math.gcd(denom1, denom2)
    denom = gcd * (denom1 // gcd) * (denom2 // gcd)
    numer = numer1 * (denom // denom1) + numer2 * (denom // denom2)

    return [numer // math.gcd(numer, denom), denom // math.gcd(numer, denom)]


# 다른 사람의 풀이
from fractions import Fraction

def solution(denum1, num1, denum2, num2):
    answer = Fraction(denum1, num1) + Fraction(denum2, num2)
    return [answer.numerator, answer.denominator]