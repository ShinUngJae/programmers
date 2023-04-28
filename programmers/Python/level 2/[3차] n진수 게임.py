def solution(n, t, m, p):
    
    temp_list = [str(i) for i in range(0, 10)] + [chr(i) for i in range(65, 71)]
    num_list = {int(i) : j for i, j in zip(range(0, 16), temp_list)}
    
    num = 0
    answer = ""
    
    while len(answer) <= t * m :
        
        if num == 0 :
            temp = "0"
        else :
            temp = ''
            num2 = num
            while num2 != 0 :
                temp =  num_list[num2 % n] + temp
                num2 = num2 // n
                
        answer += temp
        num += 1
            
    return "".join([answer[i] for i in range(len(answer)) if i % m == p - 1])[: t]