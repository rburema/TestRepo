import sys
import json

print(sys.argv[1])

data = None
with open(sys.argv[1]) as f:
    data = json.load(f)

print(len([x for x in data if x["base"]["repo"]["id"] != x["head"]["repo"]["id"] and not x["draft"] ]))
