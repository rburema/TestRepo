import sys
import json

print(sys.argv[1])
data = json.load(sys.argv[1])

for pr in data:
	print(pr["id"])
