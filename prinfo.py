import sys
import json

print(sys.argv[1])

data = None
with open(sys.argv[1]) as f:
    data = json.load(f)

print(len(data))
