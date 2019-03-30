import argparse
parser = argparse.ArgumentParser()
parser.add_argument("pairs",help="filepath that stores pairs")
parser.add_argument("input")
parser.add_argument("output")
args = parser.parse_args()
in_fp = args.input
out_fp = args.output
pair_fp = args.pairs

# in_fp = r'sss.txt'
# out_fp = r'out.txt'
# pair_fp = r'xxx1.txt'


pairmap = set()
with open(pair_fp,encoding='utf-8') as f:
    for line in f:
        pairmap.add(line.strip('\n'))

f = open(in_fp,encoding='utf-8')
out_f = open(out_fp, "a",encoding='utf-8')
for line in f:
    for w in line.split():
        w += '▁'
        toks = list(w)
        flag=True
        mergecount=1
        while mergecount>0:
            mergecount = 0
            i = 0
            while i < len(toks) - 1:
                pair = toks[i] + toks[i + 1]
                if pair in pairmap:
                    mergecount += 1
                    del toks[i]
                    del toks[i]
                    toks.insert(i, pair)
                    i -= 1
                i += 1
        for t in toks:
            out_f.write(t+' ')
    out_f.write('\n')
f.close()
out_f.close()


