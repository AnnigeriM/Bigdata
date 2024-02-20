from itertools import groupby
from operator import itemgetter

a =["cat","dog","cow","lion","fox","shark","snake","bear"]

for l, wds in groupby(sorted(a), key=itemgetter(0)):
    print(l)
    for w in wds:
        print("",w)
        print()