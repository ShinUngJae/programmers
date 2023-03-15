def solution(id_pw, db):
    db_dict = {i[0] : i[1] for i in db}
    try :
        if db_dict[id_pw[0]] == id_pw[1] :
            return "login"
        else :
            return "wrong pw"
    except :
        return "fail"
    

# 다른 사람의 코드
def solution(id_pw, db):
    if db_pw := dict(db).get(id_pw[0]):
        return "login" if db_pw == id_pw[1] else "wrong pw"
    return "fail"