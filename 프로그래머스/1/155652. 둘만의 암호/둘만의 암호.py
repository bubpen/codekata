def solution(s, skip, index):
    alp = ''.join([c for c in 'abcdefghijklmnopqrstuvwxyz' if c not in skip])
    alp_len = len(alp)
    
    
    return ''.join(alp[(alp.index(c)+index)%alp_len] for c in s)