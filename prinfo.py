import sys
import json

print(sys.argv[1])

data = None
with open(sys.argv[1]) as f:
    data = json.load(f)

for pr in data:
	print(pr["id"])
