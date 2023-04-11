s1 = 'DURGASOFTWAREi'

vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

count = {}

for ch in s1:
    if ch in vowels:
        count[ch] = count.get(ch,0)+1

print(count)   # this will be print in unsorted way

print(sorted(count.items()))  ## this will be print in sorted way


for k,v in sorted(count.items()):
    print('{} occurs {} times'.format(k,v))
