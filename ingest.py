import os
import json
import csv
import subprocess
import sys

os.system("ls /u/*/*/ > raw.txt")
r = open("raw.txt")

out_json = ("j" in sys.argv[1])
count = 0
total = 128000

results = {} if out_json else []
f = open('unis.json','wb') if out_json else open('unis.csv','wb')
keys = set()
for line in r:
    count +=1
    unis = filter(lambda x: ":" not in x, line.split())
    for uni in unis:
        print 1.0*count/total
        if uni.isdigit() or not any(char.isdigit() for char in uni):
            break

        com = 'lookup '+ uni
        print com

        p = subprocess.Popen(["lookup", uni], stdout=subprocess.PIPE,stdin=subprocess.PIPE)
        p.stdin.write('q')
        out, err = p.communicate()
        data = str(out)
        
        if not data or data[0] != "-":
            break
        else:
            row = {}
            k = None
            v = ''
            for chunk in data.split('\n'):
                for part in chunk.replace("--","").split():
                    if ":" in part:
                        if k is not None:
                            row[k] = v.replace('\n', ' ').replace(',', '')
                            v = ''
                        k = part.strip().replace(":","")
                        keys.add(k)
                    else:
                        v  = v + " " + part
            if out_json:
                results[uni] = row
            else:
                results.append(row)

if out_json:
    json.dump(results, f)
else:
    w = csv.DictWriter(f, keys)
    w.writerows(results)
    f.close()
