s = 'x4d3m2a5'
s1 = ''
s2 = []


num_char = 'xxxbbbrr'

c = 0
print(len(num_char))

def alphanum(s, s1):
    for i in s:
        if i.isdigit():
            s1+=i
        else:
            s2.append(i)

    print(s1)
    print(s2)

    s3 = ''
    j=0
    s4 = ''
    while j<=len(s1)-1:
      s3 = s3 + (s2[j]*int(s1[j]))
      j+=1
    print(s3)

    print(s4.join(sorted(s3)))


def numalpha(a):
    for j in range(len(a)-1):
        c=0
        prev = a[j]
        if a[j]==a[j+1]:
            c+=1
            prev = prev + a[j]
    print(c,prev)

numalpha(num_char)

