s = 'aaaabbbccza'
prev = s[0]
c=1
i=1
output = ''
while i < len(s):
    if s[i]==prev:
        c+=1
    else:
        output = output + str(c)+prev
        prev=s[i]
        c=1
    if i==len(s)-1:
        output = output + str(c)+prev
        prev=s[i]
    i+=1

print(output)

