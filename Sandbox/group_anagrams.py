from collections import defaultdict
from time import time

start = time()
def group_anagrams(a):
    dfdict = defaultdict(list)
    #print(dfdict)
    for i in a:
        sorted_i = " ".join(sorted(i))
        #print("sorted_i -> ", sorted_i)
        dfdict[sorted_i].append(i)
        #print(dfdict.keys() , dfdict.values())
    return dfdict.values()


anagrams_list = ["tea", "eat", "bat", "ate", "arc", "car"]
print(group_anagrams(anagrams_list))

end = time()

exe_time = end - start
print("Execution Time = ", exe_time)