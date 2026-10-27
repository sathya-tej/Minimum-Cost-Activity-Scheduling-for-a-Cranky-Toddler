from itertools import combinations

def no_overlap(chosen):
    chosen=sorted(chosen,key= lambda a:a[1])
    for i in range(1,len(chosen)):
        if chosen[i-1][1]>chosen[i][0]:
            return False
    return True

def all_covered(chosen,cranky):
    for i in cranky:
        covered=False
        for j in range(len(chosen)):
            if i>=chosen[j][0] and i<=chosen[j][1]:
                covered=True
                break
        if not covered:
            return False
    return True

def brute_force(activities,cranky):
    INF=float('inf')
    best=INF
    n=len(activities)

    for k in range(n+1):
        for subset in combinations(activities,k):
            if no_overlap(subset) and all_covered(subset,cranky):
                cost=sum(s[2] for s in subset)
                best=min(best,cost)
    return best

activities=[(480,600,5),(510,570,3),(630,690,4),(480,720,20),(690,750,1)]
cranky=[540,660]

print(brute_force(activities,cranky))
print(brute_force([(8, 9, 2), (10, 11, 3), (12, 13, 4)],[8.5, 10.5, 12.5]))
print(brute_force([(8, 9, 2), (10, 11, 3), (12, 13, 4)],[]))