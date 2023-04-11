s = '9564659'

start = 0
end = len(s)-1
print(end)
c = True
while start < end:
    if s[start] != s[end]:
        c = False
    start = start + 1
    end = end - 1

if c:
    print("PALINDROME")
else:
    print("NOT PALINDROME")
