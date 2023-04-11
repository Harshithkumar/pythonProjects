fullname = input("Enter any full name   ")
List = []
List = fullname.split()
sname = ''

print(List[0].title())
for i in range(1,len(List)):
    s=List[i]
    print(s)
    sname+= s[0].upper() + '.'
    print(s[0].upper() + '.')
sname =  List[0].title() + ' ' + sname

print(sname)

