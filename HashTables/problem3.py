count_dict = {}
with open('poem.txt', 'r') as f:
    for row in f:
        for word in row.split(' '):
            word = word.replace('\n','').replace(',','').replace('.','')
            if word in count_dict.keys():
                count_dict[word] += 1
            else:
                count_dict[word] = 1
for x in count_dict:
    print(x,':', count_dict[x])