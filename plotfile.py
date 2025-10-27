fname = "mbox-short-1.txt"
d = {}
fh = open(fname)
for line in fh:
    words = line.split()
    if len(words) < 1:
        continue
    first_word = words[0]
    if first_word == 'From':
        d['From'] = d.get('From', 0) + 1
    elif first_word == 'From:':
        d['From:'] = d.get('From',0) + 1
    else:
        d['other']  = d.get('other',0) + 1

for key, value in d.items():
    print("There are ", value, " counts of ", key)

 
        

        
    
