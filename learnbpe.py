import argparse
parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("output")
args = parser.parse_args()
in_fp = args.input
out_fp = args.output

# in_fp = r'sss.txt'
# out_fp = r'xxx1.txt'

import numpy as np

wordmap = {}
pairlist = []

with open(in_fp,encoding='utf-8') as f:
    for line in f:
        for w in line.split():
            w += '▁'
            if w not in wordmap:
                wordmap[w] = [list(w),1]
            else:
                wordmap[w][1] += 1

while True:
    pairmap = {}
    for word, [toks,count] in wordmap.items():
        for i in range(len(toks) - 1):
            pair = toks[i] + toks[i + 1]
            if pair not in pairmap:
                pairmap[pair] = count
            else:
                pairmap[pair] += count
            pc = pairmap[pair]
    ls_pair = []
    ls_c = []
    for pair, count in pairmap.items():
        if count>=5:
            ls_pair.append(pair)
            ls_c.append(count)
    if len(ls_pair)==0:
        break
    ix_ord = np.argsort(ls_c)[::-1][:100]
    maxnqueue = [ls_pair[ix] for ix in ix_ord]
    pairlist += maxnqueue
    for word, [toks,count] in wordmap.items():
        i=0
        while i<len(toks)-1:
            pair = toks[i] + toks[i + 1]
            for _p in maxnqueue:
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








