s1 = 'DDREREOKOKPPAA'
d = { }

for ch in s1:
    d[ch] = d.get(ch,0)+1     # get(ch,0) represents ch is the char location, 0 -> is the value which will be added
                                #to +1
print(d)

output=''
for k,v in d.items():
    output = output + str(v) + k  #this will give the o/p in numalpha
print(output)


for x,y in d.items():
    output = output + str(x) + y  #this will give the o/p in alphanum. If we need sorted use sorted(d.items())
print(output)