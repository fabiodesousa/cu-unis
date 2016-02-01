import json
from collections import defaultdict

histogram = defaultdict(int)
with open('/u/5/n/nl2418/cu-unis/unis.json') as data_file:
    unis = json.load(data_file)
for uni in unis.keys():
    info = unis[uni]
    histogram[info.get('Dept','')] +=1 
for key in sorted(histogram.keys()):
    print key, histogram[key]
