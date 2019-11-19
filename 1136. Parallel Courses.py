class Solution:
    def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
        child = collections.defaultdict(list)
        parents = [0]*N
        for x,y in relations:
            child[x].append(y)
            parents[y-1] += 1

        result = 0
        can_take = []
        for key,val in enumerate(parents):
            if val == 0: can_take.append(key+1)

        taken = 0
        while can_take:
            result += 1
            temp = []
            taken += len(can_take)
            for x in can_take:
                for y in child[x]:
                    parents[y-1] -= 1
                    if parents[y-1] == 0: temp.append(y)
            can_take = temp

        if taken != N: return -1
        else: return result
