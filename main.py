
def intersect(s1, s2):
    ret = [x for x in s1 for y in s2 if x==y]
    return sorted(ret)

#print intersect([1,2,4], [1,2,3])

def union(s1, s2):
    
    z = [x for x in s2 if x not in s1]
    ret = s1 + z
    return sorted(ret)
    
#print union([1,2,4], [1,2,3])

def diff(s1, s2):
    inter = intersect(s1,s2)
    z = [x for x in s1 if x not in inter]
    return z

#print diff([1,2,4], [1,2,3])
#print diff([1,2,3], [1,2,4])

def sym_diff(s1, s2):
    inter = intersect(s1,s2)
    z = [x for x in s1 if x not in inter]
    y = [x for x in s2 if x not in inter]
    return sorted(z + y)

#print sym_diff([1,2,4], [1,2,3])

def product(s1, s2):
    ret = [(x,y) for x in s1 for y in s2]
    return ret

print product(['red','blue'], [1,2,4])
