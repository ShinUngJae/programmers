def solution(price):
    return int(price * ((price >= 500000) * 0.8 + (300000 <= price < 500000) * 0.9 + (100000 <= price < 300000) * 0.95 + (price < 100000)))