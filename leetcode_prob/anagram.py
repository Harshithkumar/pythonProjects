strs = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']


def group_anagrams(strs):
    anagram_groups = {}
    for word in strs:
        sorted_word = ''.join(sorted(word))
        print(sorted_word)
        if sorted_word not in anagram_groups:
            anagram_groups[sorted_word] = []
        anagram_groups[sorted_word].append(word)

    return list(anagram_groups.values())


result = group_anagrams(strs)
print(result)