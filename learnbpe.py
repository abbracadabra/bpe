in_fp = r'sss.txt'
out_fp = r'xxx.txt'

wordmap = {}
pairlist = []

with open(in_fp,encoding='utf-8') as f:
    for line in f:
        for w in line.split():
            if w not in wordmap:
                wordmap[w+' '] = (list(w),1)
            else:
                wordmap[w+' '][1] += 1

while True:
    pairmap = {}
    maxnqueue = [] # a list to store most frequent 10 pair
    for word, (toks,count) in wordmap.items():
        for i in range(len(toks) - 1):
            pair = toks[i] + toks[i + 1]
            if pair not in pairmap:
                pairmap[pair] = count
            else:
                pairmap[pair] += count
            pc = pairmap[pair]
            for j,(_p, _) in enumerate(maxnqueue):
                if _p==pair:
                    del maxnqueue[j]
                    break
            if len(maxnqueue) == 0:
                maxnqueue.append((pair, pc))
            elif pc <= maxnqueue[0][1]:
                if len(maxnqueue) < 10:
                    maxnqueue.insert(0, (pair, pc))
            else:
                for z in range(len(maxnqueue)):
                    if pc > maxnqueue[z][1] and (z + 1 >= len(maxnqueue) or pc <= maxnqueue[z + 1][1]):
                        maxnqueue.insert(z + 1, (pair, pc))
                        maxnqueue = maxnqueue[-10:]
                        break
    maxnqueue = maxnqueue[::-1]
    if maxnqueue[0][1]<5: # break if the most frequent pair appear less than 5 times
        break
    pairlist += [tup[0] for tup in maxnqueue]
    for word, (toks,count) in wordmap.items():
        i=0
        while i<len(toks)-1:
            pair = toks[i] + toks[i + 1]
            for _p, _pc in maxnqueue:
                if pair == _p:
                    del toks[i]
                    del toks[i]
                    toks.insert(i,_p)
                    i-=1
                    break
            i+=1


with open(out_fp, "a",encoding='utf-8') as f:
    for _p in pairlist:
        f.write(_p+'\n')








