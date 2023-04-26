import sys
import json

print(sys.args[1])
data = json.load(sys.args[1])

for pr in data:
	print(pr["id"])
