from difflib import SequenceMatcher

name1 = 'Harshshith'
name2 = 'RushHarsh'

Seq = SequenceMatcher(None, name1, name2)

match = Seq.find_longest_match(0, len(name1), 0, len(name2))

print(match.a)

if (match.size!=0):
    print(name1[match.a: match.a + match.size])
else:
    print('No longest common sub-string found')
