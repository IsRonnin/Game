'''def mdk(func):
    def inner(*args):
        print("decorated")
        answ = {}
        [answ.update({args[a] : "good"}) if args[a] >= 100 else answ.update({args[a] : "bad"}) for a in range(len(args))]
        return answ
    
    return inner

@mdk
def ret_n(*args):
    for i in args:
        print(i)
    return list(args)

integ = 1000
print(ret_n(integ, 125, 215))

def table_things(**kwargs):
    print(kwargs.items())
    for name, value in kwargs.items():
        print( '{0} = {1}'.format(name, value))
'''
from collections import Counter as cont
# 0 index 1 game_name 2 publisher 

bd = [[0, 'doom', 'xbox'], [1, 'doom', 'microsoft'], [2, 'nfs', 'ms'], [5, 'nfs', 'xbox']]
print(cont([a[1] for a in bd]))
c = cont([a[1] for a in bd])
ans = {}
[[ans.update({bd[ji][1]: c[ki]}) for ji in range(len(bd))]for ki in c.keys()]
print(ans)