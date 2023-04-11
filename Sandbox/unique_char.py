# S1 = ['L','E','E','T','C','O','D','E','L']
# unique = {}
#
# for i in S1:
#     #unique[i] = unique.get(i, 0) + 1
#     unique[i] = i
#
# print(unique)

# for k,v in dict(unique).items():
#     if v>1:
#         unique.pop(k)
#         print("Popped value ", k, v)
#
# print(unique)


my_dict = {2: 'USA (+1)', 3: 'UK (+44)', 4: 'Algeria (+213)', 5: 'Andorra (+376)', 6: 'Angola (+244)'}
my_dict_key = list(my_dict.keys())
my_dict_val = list(my_dict.values())
#print("key value is ", list(my_dict.keys())[list(my_dict.values()).index('Angola (+244)')])
key = my_dict_key[my_dict_val.index('Angola (+244)')]
print("key value is ", key )