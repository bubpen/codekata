def solution(id_pw, db):
    if id_pw in db:
        return 'login'
    id_list = []
    for i in range(len(db)):
        id_list.append(db[i][0])
    if id_pw[0] not in id_list:
        return 'fail'
    else:
        return 'wrong pw'
    return answer