in_fp = r'sss.txt'
out_fp = r'xxx.txt'
pair_fp = r''

pairmap = set()
with open(pair_fp,encoding='utf-8') as f:
    for line in f:
        pairmap.add(line)

with open(in_fp,encoding='utf-8') as f:
    for line in f:
        for w in line.split():
            w+=' '
            chars = list(w)
            while i
