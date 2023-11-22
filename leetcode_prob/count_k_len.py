from collections import Counter


input = "John is the son of John second. Second son of John second is William second."
input2 = "Welcome to the world. of Geeks " \
"This portal has been created to provide well written well." \
"thought and well explained solutions for selected questions. " \
"If you like Geeks for Geeks. and would like to contribute " \
"here is your. chance You can write article and mail your article " \
" to contribute at geeksforgeeks org See your article appearing on " \
"the Geeks for Geeks main page and help thousands of other Geeks. " \

output = input.lower().split()
for word in output:
     if word.endswith("."):
          output.insert(output.index(word), word.rstrip("."))
          output.remove(word)
print(output)


out = Counter(output)
res = Counter(output).most_common(4)

print(out)
print(res)

allcount = dict(out)
print("All count", (allcount))

mostcommon = dict(res)
print("Most common", (mostcommon))






