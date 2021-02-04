# def word_count(str):
#     counts = dict()
#     words = str.split()

#     for word in words:
#         if word in counts:
#             counts[word] += 1
#         else:
#             counts[word] = 1

#     return counts

# valu=word_count('Mahesh Mahesh Mahesh jerry jerry')

valu='Mahesh Mahesh jerry jerry sams'


words = valu.split()
count ={}

for i in words:
    if i in count:
        count[i] +=1
    else:
        count[i] =1

print(count)


for m in [max(count.values())]:
    for key,val in count.items():
        if val == m:
            print(key,val)




